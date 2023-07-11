from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
from streamlit_webrtc import webrtc_streamer
import threading
from streamlit_javascript import st_javascript

js_code = """
var myEvent = window.attachEvent || window.addEventListener
var chkEvent = window.attachEvent ? 'onbeforeunload':'beforeunload';
  myEvent(chkEvent, function(e) {
    var confirmationMessage = "Are you sure you want to leave the page";
    (e || window.event).returnValue = confirmationMessage;
    return confirmationMessage;
  });
"""

return_value = st_javascript(js_code)

st.markdown(return_value)
