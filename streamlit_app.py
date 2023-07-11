from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
from streamlit_webrtc import webrtc_streamer
import threading
from streamlit_javascript import st_javascript

js_code = """window.addEventListener('beforeunload', function(event) {
  // Check if the user is closing the tab
  if (!event.clientY) {
    // User is closing the tab
    return true;
    // Perform any necessary actions here
    // ...
  }
});"""

return_value = st_javascript(js_code)

st.markdown(return_value)
