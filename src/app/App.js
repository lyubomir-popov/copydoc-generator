import React, { Component } from "react";
import uuidv4 from "uuid/v4";

import GlobalNav from "./components/GlobalNav";
import Strip from "./containers/Strip";
import Nav from "./components/Nav";
import GhostStrip from "./containers/GhostStrip";
import Footer from "./components/Footer";
import { stripExamples } from "./data";

const moveItem = (origArr, fromIndex, toIndex) => {
  const arr = [...origArr];
  const el = arr[fromIndex];
  arr.splice(fromIndex, 1);
  arr.splice(toIndex, 0, el);
  return arr;
};

class App extends Component {
  state = {
    strips: [],
    editing: true,
    markup: ""
  };

  container = React.createRef();

  addStrip = strip => {
    const { strips } = this.state;
    const newStrip = {
      id: uuidv4(),
      ...strip
    };
    this.setState({ strips: [...strips, newStrip] });
  };

  removeStrip = id => {
    const { strips } = this.state;
    this.setState({ strips: strips.filter(strip => strip.id !== id) });
  };

  moveStrip = (id, dir) => {
    const { strips } = this.state;
    const fromIndex = strips.findIndex(strip => strip.id === id);
    const toIndex = dir === "up" ? fromIndex - 1 : fromIndex + 1;

    if (toIndex >= 0 && toIndex <= strips.length - 1) {
      this.setState({ strips: moveItem(strips, fromIndex, toIndex) });
    }
  };

  changeStripType = (id, type) => {
    const { strips } = this.state;
    const newStrips = strips.map(strip => {
      if (strip.id === id) {
        return {
          ...strip,
          type,
          name: stripExamples.find(strip => strip.type === type).name
        };
      }
      return strip;
    });

    this.setState({ strips: newStrips });
  };

  changeStripName = (id, name) => {
    const { strips } = this.state;
    const newStrips = strips.map(strip => {
      if (strip.id === id) {
        return {
          ...strip,
          name
        };
      }
      return strip;
    });

    this.setState({ strips: newStrips });
  };

  toggleEditing = () => {
    const { editing } = this.state;
    this.setState({ editing: !editing });
  };

  generateStrips = () => {
    const { strips, editing } = this.state;

    return strips.map((strip, index) => (
      <Strip
        key={strip.id}
        strip={strip}
        editing={editing}
        remove={this.removeStrip}
        changeType={this.changeStripType}
        changeName={this.changeStripName}
        move={strips.length >= 2 ? this.moveStrip : undefined}
        canMoveUp={index !== 0}
        canMoveDown={index !== strips.length - 1}
      />
    ));
  };

  generateMarkup = () => {
    const { container } = this;
    if (container.current) {
      this.setState({ markup: container.current.innerHTML });
    }
  };

  render = () => {
    const { editing, markup } = this.state;

    return (
      <div className="App">
        <GlobalNav
          editing={editing}
          toggleEditing={this.toggleEditing}
          generateMarkup={this.generateMarkup}
        />
        <div>
          <Nav />
          <div ref={this.container}>{this.generateStrips()}</div>
          {editing && <GhostStrip addStrip={this.addStrip} />}
          <Footer />
        </div>
        {markup && (
          <div className="row">
            <pre>
              <code>{markup}</code>
            </pre>
          </div>
        )}
      </div>
    );
  };
}

export default App;
