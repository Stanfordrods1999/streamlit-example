from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
from streamlit_webrtc import webrtc_streamer
import threading

lock = threading.Lock()
img_container = {"img": None}
frame_rate = 1
is_true=False

def video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")
    with lock:
        img_container["img"] = img
    return frame
  
ctx = webrtc_streamer(key="example", video_frame_callback=video_frame_callback,
                       media_stream_constraints={"video": {"frameRate": {"ideal": frame_rate}}},
    video_html_attrs=({
        "controls": False,
        "autoPlay": True,
    })
while ctx.state.playing:
  with lock:
    img = img_container["img"]
    if img is not None:
      is_true=True
  print(frame_rate,is_true)  
