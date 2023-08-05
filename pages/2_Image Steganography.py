import cv2
import numpy as np
import streamlit as st
import os
from Components import footer
st.set_page_config(layout="wide")
st.markdown(footer,unsafe_allow_html=True)

def char_generator(message):
  for c in message:
    yield ord(c)
def get_image(image_location):
  img = cv2.imread(image_location)
  return img

def gcd(x, y):
  while(y):
    x, y = y, x % y

  return x

def encode_image(image_location, msg):
  img = get_image(image_location)
  msg_gen = char_generator(msg)
  pattern = gcd(len(img), len(img[0]))
  for i in range(len(img)):
    for j in range(len(img[0])):
      if (i+1 * j+1) % pattern == 0:
        try:
          img[i-1][j-1][0] = next(msg_gen)
        except StopIteration:
          img[i-1][j-1][0] = 0
          return img

def decode_image(img_loc):
  img = get_image(img_loc)
  pattern = gcd(len(img), len(img[0]))
  message = ''
  for i in range(len(img)):
    for j in range(len(img[0])):
      if (i-1 * j-1) % pattern == 0:
        if img[i-1][j-1][0] != 0:
          message = message + chr(img[i-1][j-1][0])
        else:
          # print(message)
          return message
        
if __name__ == "__main__":
    st.markdown("# Image Steganography")
    tab1, tab2 = st.tabs(["Encode", "Decode"])
    
    with tab1:
        st.header("Encode Image")
        with st.form("Encode"):
            img = st.file_uploader("Upload Image(Do not upload a full Black and White photo)", type=["png", "jpg", "jpeg"])
            text_input = st.text_input(
                "Enter text to Encode",
            )
            submitted = st.form_submit_button("Encode")
            if submitted:
                if img is not None:
                    file_details = {"FileName": img.name, "FileType": img.type}
                    with open(os.path.join("Imagedir",img.name),"wb") as f: 
                        f.write(img.getbuffer())
                    encoded_image = encode_image(os.path.join("Imagedir",img.name), text_input)
                    cv2.imwrite(os.path.join("Imagedir","EncodedImage.png"), encoded_image)
                    # st.image("EncodedImage.png", caption="Encoded Image", use_column_width=True)
                    st.success("Image Encoded Successfully")
                    st.markdown("Download Encoded Image")
        if submitted: 
          with open(os.path.join("Imagedir","EncodedImage.png"), "rb") as file:
            st.download_button(             
              label="Download Image",
              data=file,
              file_name='EncodedImage.png',
              mime='image/png',
            )
    with tab2:
      st.header("Decode Image")
      with st.form("Decode"):
        dimg = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])
        submitted = st.form_submit_button("Decode")
        if submitted:
          if dimg is not None:
            file_details = {"FileName": dimg.name, "FileType": dimg.type}
            with open(os.path.join(os.path.join("Imagedir",dimg.name)),"wb") as f: 
              f.write(dimg.getbuffer())
            decoded_image = decode_image(os.path.join("Imagedir",dimg.name))
            print(decoded_image)
            st.success("Image Decoded Successfully")
            st.write("Decoded Message: ",decoded_image)

    # file_location = "image.jpg"
    # secret_message = "Hello from inside the picture!"
    # encoded_image = encode_image(file_location, secret_message)
    # cv2.imwrite("EncodedImage.png", encoded_image)
    # print("Done encoding!")
    # decoded_image = decode_image("EncodedImage.png")
    # print(decoded_image)

