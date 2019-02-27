import React, { Component } from "react";
import PropTypes from "prop-types";

import { stripTypes, stripExamples } from "../data";

class GhostStrip extends Component {
  handleSelect = e => {
    const { addStrip } = this.props;
    const strip = stripExamples.find(
      example => example.type === e.target.value
    );

    if (strip) {
      addStrip(strip);
    }
  };

  render = () => {
    return (
      <section className="strip-container">
        <div className="p-strip is-shallow" />
        <div className="strip-controls">
          <select value="" onChange={e => this.handleSelect(e)}>
            <option value="" disabled>
              Add a new strip
            </option>
            {stripTypes.map(option => (
              <option key={option.name} value={option.name}>
                {option.label}
              </option>
            ))}
          </select>
        </div>
      </section>
    );
  };
}

GhostStrip.propTypes = {
  addStrip: PropTypes.func.isRequired
};

export default GhostStrip;
