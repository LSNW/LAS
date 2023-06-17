"use strict";

const e = React.createElement;

class SubmitButton extends React.Component {
  state = {
    text: "Split",
  };

  handleClick = () => {
    this.setState({ text: "Splitting" });
  };

  render() {
    return (
      <button type="submit" onClick={this.handleClick}>
        {this.state.text}
      </button>
    );
  }
}

const domContainer = document.querySelector("#submit-button");
ReactDOM.render(e(SubmitButton), domContainer);
