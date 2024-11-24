import cv2
import numpy as np
import streamlit as st
import os

# Dummy footer component (replace with your actual footer content if necessary)

st.set_page_config(
    page_title='Image Steganography',
    page_icon='https://firebasestorage.googleapis.com/v0/b/stegproject-99219.appspot.com/o/favicon.ico?alt=media&token=ba72f22f-3188-4e27-9ed7-19ddad766f0a',
    layout='wide',
    initial_sidebar_state='auto'
)

# Utility functions
def char_generator(message):
    for c in message:
        yield ord(c)

def get_image(image_location):
    img = cv2.imread(image_location)
    return img

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

# Corrected GCD-based encoding function
def encode_image_gcd_optimized(image_location, msg, density_factor=2):
    """
    Encodes a message into an image using a modified GCD-based method.
    Args:
        image_location (str): Path to the input image.
        msg (str): Message to encode.
        density_factor (int): Factor to increase encoding density.
    Returns:
        numpy.ndarray: Encoded image.
    """
    img = get_image(image_location)
    msg_gen = char_generator(msg + '\0')  # Add a null character as the end marker
    pattern = gcd(img.shape[0], img.shape[1]) // density_factor  # Adjust density
    print(f"[DEBUG] Optimized GCD Pattern: {pattern}")  # Debug: New pattern

    for i in range(0, img.shape[0], pattern):
        for j in range(0, img.shape[1], pattern):
            try:
                char_to_encode = next(msg_gen)
                img[i, j, 0] = char_to_encode
                print(f"[DEBUG] Encoding Char '{chr(char_to_encode)}' at Pixel ({i},{j})")  # Debug: Show pixel location
            except StopIteration:
                print("[DEBUG] End of Message Reached")  # Debug: Message encoded completely
                return img
    print("[DEBUG] Message fits completely in the image")  # Debug: No truncation
    return img

# Corrected GCD-based decoding function
def decode_image_gcd_optimized(img_loc, density_factor=2):
    """
    Decodes a message from an image using a modified GCD-based method.
    Args:
        img_loc (str): Path to the encoded image.
        density_factor (int): Factor used for encoding density.
    Returns:
        str: Decoded message.
    """
    img = get_image(img_loc)
    pattern = gcd(img.shape[0], img.shape[1]) // density_factor  # Adjust density
    print(f"[DEBUG] Optimized GCD Pattern for Decoding: {pattern}")  # Debug: New pattern
    message = ''

    for i in range(0, img.shape[0], pattern):
        for j in range(0, img.shape[1], pattern):
            char_code = img[i, j, 0]  # Read the blue channel
            if char_code == 0:  # Null character signals the end of the message
                print(f"[DEBUG] End of Message Detected. Full Message: {message}")  # Debug: Show full message
                return message
            message += chr(char_code)
            print(f"[DEBUG] Decoded Char '{chr(char_code)}' from Pixel ({i},{j})")  # Debug: Show decoded character
    print(f"[DEBUG] Entire Image Processed. Full Message: {message}")  # Debug: If loop finishes
    return message


def check_capacity(image_location, msg_length, density_factor=2):
    img = get_image(image_location)
    pattern = gcd(img.shape[0], img.shape[1]) // density_factor
    max_chars = (img.shape[0] // pattern) * (img.shape[1] // pattern)
    print(f"[DEBUG] Image Capacity: {max_chars} characters")  # Debug: Capacity
    if max_chars < msg_length:
        raise ValueError(f"Image too small for the message. Maximum capacity: {max_chars} characters.")


# Algorithm 2: Least Significant Bit (LSB) Steganography
def encode_image_lsb(image_location, msg):
    img = get_image(image_location)
    msg += chr(0)  # Delimiter
    msg_bin = ''.join([format(ord(c), '08b') for c in msg])
    data_index = 0

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            for k in range(3):  # Loop over R, G, B channels
                if data_index < len(msg_bin):
                    img[i, j, k] = (img[i, j, k] & 254) | int(msg_bin[data_index])
                    data_index += 1
    return img

def decode_image_lsb(img_loc):
    img = get_image(img_loc)
    binary_data = ""
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            for k in range(3):  # Loop over R, G, B channels
                binary_data += str(img[i, j, k] & 1)
    all_bytes = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    message = ""
    for byte in all_bytes:
        char = chr(int(byte, 2))
        if char == chr(0):  # Stop at the delimiter
            break
        message += char
    return message

if __name__ == "__main__":
    st.markdown("# Image Steganography")
    tab1, tab2 = st.tabs(["Encode", "Decode"])

    algorithms = {
        "GCD-based": (encode_image_gcd_optimized, decode_image_gcd_optimized),
        "LSB-based": (encode_image_lsb, decode_image_lsb)
    }
    selected_algorithm = st.sidebar.selectbox("Select Steganography Algorithm", list(algorithms.keys()))

    encoded_image_path = None
    decoded_message = None

    with tab1:
        st.header("Encode Image")
        with st.form("Encode"):
            img = st.file_uploader("Upload Image (avoid completely black and white photos)", type=["png", "jpg", "jpeg"])
            text_input = st.text_input("Enter text to Encode")
            submitted = st.form_submit_button("Encode")
            if submitted and img is not None:
                file_details = {"FileName": img.name, "FileType": img.type}
                image_path = os.path.join("pages/Imagedir", "Image.png")
                with open(image_path, "wb") as f:
                    f.write(img.getbuffer())
                encode_fn, _ = algorithms[selected_algorithm]
                encoded_image = encode_fn(image_path, text_input)
                encoded_image_path = os.path.join("pages/Imagedir", "EncodedImage.png")
                cv2.imwrite(encoded_image_path, encoded_image)
                st.success("Image Encoded Successfully")
    
        if encoded_image_path:
            with open(encoded_image_path, "rb") as file:
                st.download_button("Download Encoded Image", data=file, file_name='EncodedImage.png', mime='image/png')

    with tab2:
        st.header("Decode Image")
        with st.form("Decode"):
            dimg = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])
            submitted = st.form_submit_button("Decode")
            if submitted and dimg is not None:
                file_details = {"FileName": dimg.name, "FileType": dimg.type}
                image_path = os.path.join("pages/Imagedir", dimg.name)
                with open(image_path, "wb") as f:
                    f.write(dimg.getbuffer())
                _, decode_fn = algorithms[selected_algorithm]
                decoded_message = decode_fn(image_path)
                st.success("Image Decoded Successfully")
        
        if decoded_message:
            st.write("Decoded Message: ", decoded_message)
