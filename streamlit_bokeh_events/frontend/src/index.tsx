import React from "react"
import ReactDOM from "react-dom"
import StreamlitBokehEventsComponent from "./StreamlitBokehEventsComponent"

declare global {
  interface Window {
    Bokeh: any
  }
}

ReactDOM.render(
  <React.StrictMode>
    <StreamlitBokehEventsComponent />
  </React.StrictMode>,
  document.getElementById("root")
)
