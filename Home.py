import streamlit as st
import time
from urllib.parse import urlencode
from Components import create_card, footer
st.set_page_config(page_title='Web Based Steganography Tool', page_icon='https://firebasestorage.googleapis.com/v0/b/stegproject-99219.appspot.com/o/favicon.ico?alt=media&token=ba72f22f-3188-4e27-9ed7-19ddad766f0a',layout = 'wide', initial_sidebar_state = 'auto')
# st.set_page_config(layout="wide")
st.markdown(footer,unsafe_allow_html=True)

if __name__ == "__main__":
    # with st.spinner('Wait for it...'):
    #     time.sleep(2)
    st.write("",unsafe_allow_html=True)
    st.write("<div style='display:flex;justify-content: center'><img style='postion:fixed; top:0; right:0;display: inline-block; vertical-align: top;' src='https://firebasestorage.googleapis.com/v0/b/stegproject-99219.appspot.com/o/logo-e78ff0ab.webp?alt=media&token=03ddd35d-006c-40cd-9ced-86b7ef0d7c9f' width=100><h1 style='text-align: center; font-size: 50px;'><b>Web Based Steganography Tool</b></h1></div>",unsafe_allow_html=True)
    st.write("<p style='text-align: center; font-style: italic; font-size: 20px;'>All in one solution to send messages hidden in regular stuff</p>",unsafe_allow_html=True)
    # st.markdown('<a href="/Image_Steganography" target="_self">Next page</a>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.write(create_card('''https://firebasestorage.googleapis.com/v0/b/stegproject-99219.appspot.com/o/imagesteg.png?alt=media&token=17510005-2b8c-4a08-aa1d-7c1b0b14e44f''','''Image Steganography''','''left''','''/Image_Steganography'''),unsafe_allow_html=True)
    with col2:
        st.write(create_card('''https://firebasestorage.googleapis.com/v0/b/stegproject-99219.appspot.com/o/Audio_steg.png?alt=media&token=e2abfc52-3a94-4348-969c-3227850db7fb''','''Audio Steganography''','''right''','''/Audio_Steganography'''),unsafe_allow_html=True)
    col3,col4 = st.columns(2)
    with col3:
        st.write(create_card('''https://firebasestorage.googleapis.com/v0/b/stegproject-99219.appspot.com/o/videosteg.png?alt=media&token=7a21c4ad-cb8e-41bf-96e9-9ef39127085b''','''Video Steganography''','''left''','''/Video_Steganography'''),unsafe_allow_html=True)
    with col4:
        st.write(create_card('''https://firebasestorage.googleapis.com/v0/b/stegproject-99219.appspot.com/o/textsteg.png?alt=media&token=3561afd0-7ef0-4a5c-ac0a-3b0011961018''','''Text Steganography''','''right''','''/Text_Steganography'''),unsafe_allow_html=True)
