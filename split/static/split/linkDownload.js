"use strict";

const e = React.createElement;

class LinkDownloader extends React.Component {
  state = {
    prefix: "https://loader.to/api/button/?url=",
    suffix: "&color=9818b8",
    link: "",
    format: "&f=mp3",
  };

  handleLinkChange = (e) => {
    this.setState({ link: e.target.value });
  };

  handleTypeChange = (e) => {
    this.setState({ format: "&f=" + e.target.value });
  };

  fetchButton() {
    let state = this.state;
    return (
      <iframe
        scrolling="no"
        src={state.prefix + state.link + state.format + state.suffix}
      ></iframe>
    );
  }

  render() {
    return (
      <div>
        <label for="link" id="media-link">
          Media Link:
        </label>
        <input
          name="link"
          type="text"
          id="link-input"
          onChange={this.handleLinkChange}
        />
        <label for="type" id="type-label">
          Select a Filetype:
        </label>
        <select name="type" id="type" onChange={this.handleTypeChange}>
          <option value="mp3">mp3</option>
          <option value="m4a">m4a</option>
          <option value="360">mp4 (360p)</option>
          <option value="720">mp4 (720p)</option>
          <option value="1080">mp4 (1080p)</option>
          <option value="4k">mp4 (4k)</option>
          <option value="8k">mp4 (8k)</option>
        </select>
        {this.fetchButton()}
        Provided by <a href="https://www.loader.to">loader.to</a>
      </div>
    );
  }
}

const domContainer = document.querySelector("#linkdlform");
ReactDOM.render(e(LinkDownloader), domContainer);
