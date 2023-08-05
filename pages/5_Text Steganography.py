import cv2
import numpy as np
import streamlit as st
import os
import time
from Home import footer
st.set_page_config(layout="wide")
st.markdown(footer,unsafe_allow_html=True)
work_in_progress='''<div style='display:flex; justify-content: center;'><img src='https://firebasestorage.googleapis.com/v0/b/stegproject-99219.appspot.com/o/wip.gif?alt=media&token=fe840370-1ac6-4ac7-a585-b96198698ba8' style='border-radius: 1rem'></div><h4 style='text-align: center;'><b>Work in Progress</b></h4>'''

if __name__ == "__main__":
    st.markdown("# Text Steganography")
    tab1, tab2 = st.tabs(["Encode", "Decode"])
    with tab1:
        st.write(work_in_progress,unsafe_allow_html=True)
    with tab2:
        st.write(work_in_progress,unsafe_allow_html=True)
    