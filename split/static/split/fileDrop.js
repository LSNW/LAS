"use strict";

const e = React.createElement;

class FileBox extends React.Component {
  state = {
    text: "Select or Drop File",
  };

  handleChange = (e) => {
    this.setState({ text: e.target.files[0].name });
  };

  render() {
    return (
      <div>
        <input name="avfile" type="file" onChange={this.handleChange} />
        <div className="file-box">
          <h5 id="file-upload-filename">{this.state.text}</h5>
        </div>
      </div>
    );
  }
}

const domContainer = document.querySelector("#file-dropbox");
ReactDOM.render(e(FileBox), domContainer);
