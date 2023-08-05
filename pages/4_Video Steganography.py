import cv2
import numpy as np
import streamlit as st
import os
import time
from Components import footer, work_in_progress
st.set_page_config(layout="wide")
st.markdown(footer,unsafe_allow_html=True)

if __name__ == "__main__":
    st.markdown("# Video Steganography")
    tab1, tab2 = st.tabs(["Encode", "Decode"])
    with tab1:
        st.write(work_in_progress,unsafe_allow_html=True)
    with tab2:
        st.write(work_in_progress,unsafe_allow_html=True)
    