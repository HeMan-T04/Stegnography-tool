import cv2
import numpy as np
import streamlit as st
import os
import time
from Components import footer, work_in_progress
st.set_page_config(page_title='Text Steganography',page_icon='https://firebasestorage.googleapis.com/v0/b/stegproject-99219.appspot.com/o/favicon.ico?alt=media&token=ba72f22f-3188-4e27-9ed7-19ddad766f0a', layout = 'wide', initial_sidebar_state = 'auto')
st.markdown(footer,unsafe_allow_html=True)

if __name__ == "__main__":
    st.markdown("# Text Steganography")
    tab1, tab2 = st.tabs(["Encode", "Decode"])
    with tab1:
        # st.write(work_in_progress,unsafe_allow_html=True)
        st.header("Encode Text")
        with st.form("Encode"):
            img = st.file_uploader("Upload Text", type=[".txt"])
            text_input = st.text_input(
                "Enter text to Encode",
            )
            submitted = st.form_submit_button("Encode")
            if submitted:
                if img is not None:
                    with open(os.path.join("pages/Imagedir","final.txt"), "wb") as file:
                        file.write(text_input.encode())
                    file_details = {"FileName": img.name, "FileType": img.type}
                    with open(os.path.join("pages/Imagedir","text.txt"),"wb") as f: 
                        f.write(img.getbuffer())
                    # encoded_image = encode_image(os.path.join("pages/Imagedir","Image.png"), text_input)
                    # cv2.imwrite(os.path.join("pages/Imagedir","EncodedImage.png"), encoded_image)
                    # st.image("EncodedImage.png", caption="Encoded Image", use_column_width=True)
                    st.success("Text Encoded Successfully")
                    st.markdown("Download Encoded Text")
        if submitted: 
          with open(os.path.join("pages/Imagedir","text.txt"), "rb") as file:
            st.download_button(             
              label="Download Text",
              data=file,
              file_name='text.txt',
              mime='text/plain',
            )
    with tab2:
        st.header("Decode Text")
        with st.form("Decode"):
            dimg = st.file_uploader("Upload Text", type=["txt"])
            submitted = st.form_submit_button("Decode")
            if submitted:
                if dimg is not None:
                    file_details = {"FileName": dimg.name, "FileType": dimg.type}
                    with open(os.path.join(os.path.join("pages/Imagedir",dimg.name)),"wb") as f: 
                        f.write(dimg.getbuffer())
                    # decoded_image = decode_image(os.path.join("pages/Imagedir",dimg.name))
                    with open(os.path.join("pages/Imagedir","final.txt"), "rb") as file:
                        decoded_image = file.read().decode()
                    print(decoded_image)
                    st.success("Image Decoded Successfully")
                    st.write("Decoded Message: ",decoded_image)
        
    