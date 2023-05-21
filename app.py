import streamlit as st
# import firebase_admin
# from firebase_admin import credentials, storage
from PIL import Image, ImageDraw, ImageFont

# Initialize Firebase Admin SDK
# cred = credentials.Certificate("credentials.json")
# firebase_admin.initialize_app(cred)

# Streamlit app
def main():
    st.title("Image Text Encryption")

    # File upload
    uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Get user input for the line to encrypt
        text = st.text_input("Enter the line to encrypt")

        if st.button("Encrypt"):
            # Encrypt the text in the image
            encrypted_image = encrypt_text_in_image(image, text)

            # Display the encrypted image
            st.image(encrypted_image, caption="Encrypted Image", use_column_width=True)

            # Download the encrypted image
            download_button(encrypted_image, "Download Encrypted Image")

def encrypt_text_in_image(image, text):
    # Convert the image to RGBA mode
    image = image.convert("RGBA")

    # Create a new transparent image
    encrypted_image = Image.new("RGBA", image.size, (0, 0, 0, 0))

    # Create a drawing context
    draw = ImageDraw.Draw(encrypted_image)

    # Define the font
    font = ImageFont.truetype("Roboto-Black.ttf", 20)  # Replace with your font file path

    # Calculate the position to place the text in the center
    text_width, text_height = draw.textsize(text, font=font)
    x = (image.width - text_width) // 2
    y = (image.height - text_height) // 2

    # Draw the text on the image
    draw.text((x, y), text, font=font, fill=(255, 0, 0, 128))

    # Composite the encrypted text image onto the original image
    encrypted_image = Image.alpha_composite(image, encrypted_image)

    return encrypted_image

def download_button(image, text):
    # Create a download link for the image
    with open("encrypted_image.png", "wb") as file:
        image.save(file, "PNG")

    st.download_button(text, "encrypted_image.png")

if __name__ == "__main__":
    main()
