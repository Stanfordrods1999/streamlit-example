from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
from streamlit_webrtc import webrtc_streamer
import threading
from streamlit_javascript import st_javascript

js_code = """
window.addEventListener('beforeunload', (event) => {
  event.preventDefault();
  event.returnValue = true;
  });"""

return_value = st_javascript(js_code)

st.markdown(return_value)
