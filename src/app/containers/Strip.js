import React, { Component, Fragment } from "react";
import PropTypes from "prop-types";

import { stripTypes, stripExamples } from "../data";
import StripTypeSelect from "../components/StripTypeSelect";

class Strip extends Component {
  state = {
    border: false
  };

  selectStrip = e => {
    const { strip, changeType } = this.props;
    changeType(strip.id, e.target.value);
  };

  selectName = e => {
    const { strip, changeName } = this.props;
    changeName(strip.id, e.target.value);
  };

  getStripJSX = () => {
    const { strip } = this.props;
    const example = stripExamples.find(
      item => item.type === strip.type && item.name === strip.name
    );

    return example.jsx;
  };

  toggleBorder = () => {
    const { border } = this.state;
    this.setState({ border: !border });
  };

  render = () => {
    const { border } = this.state;
    const { strip, move, remove, canMoveUp, canMoveDown, editing } = this.props;
    const stripNames = stripExamples.reduce((acc, example) => {
      if (example.type === strip.type) {
        acc.push(example.name);
      }
      return acc;
    }, []);

    return (
      <section className="strip-container">
        <div className={`p-strip ${border ? "pseudo-border" : ""}`}>
          {this.getStripJSX()}
        </div>
        {editing && (
          <div className="strip-controls">
            <StripTypeSelect
              selected={strip.type}
              options={stripTypes.map(type => ({
                name: type.label,
                value: type.name
              }))}
              onChange={this.selectStrip}
            />
            <StripTypeSelect
              selected={strip.name}
              options={stripNames.map(name => ({
                name,
                value: name
              }))}
              onChange={this.selectName}
            />
            <div>
              <label className="p-checkbox">
                <span className="p-checkbox__text">Border</span>
                <input
                  className="p-checkbox__input"
                  type="checkbox"
                  onChange={this.toggleBorder}
                  checked={border}
                />
                <span className="p-checkbox__box" />
              </label>
            </div>
            <div>
              <button
                type="button"
                className="p-button--base remove-button u-no-margin"
                onClick={() => remove(strip.id)}
              >
                <i className="p-icon--close" />
              </button>
              {move && (
                <Fragment>
                  {canMoveUp && (
                    <button
                      type="button"
                      className="p-button--base move-up-button u-no-margin"
                      onClick={() => move(strip.id, "up")}
                    >
                      <i className="p-icon--chevron u-mirror--y" />
                    </button>
                  )}
                  {canMoveDown && (
                    <button
                      type="button"
                      className="p-button--base move-down-button u-no-margin"
                      onClick={() => move(strip.id, "down")}
                    >
                      <i className="p-icon--chevron" />
                    </button>
                  )}
                </Fragment>
              )}
            </div>
          </div>
        )}
      </section>
    );
  };
}

Strip.propTypes = {
  strip: PropTypes.shape({
    id: PropTypes.string.isRequired,
    type: PropTypes.string.isRequired,
    name: PropTypes.string.isRequired
  }).isRequired,
  canMoveDown: PropTypes.bool.isRequired,
  canMoveUp: PropTypes.bool.isRequired,
  move: PropTypes.func,
  remove: PropTypes.func.isRequired,
  changeType: PropTypes.func.isRequired,
  changeName: PropTypes.func.isRequired,
  editing: PropTypes.bool.isRequired
};

Strip.defaultProps = {
  move: undefined
};

export default Strip;
