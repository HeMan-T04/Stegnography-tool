import streamlit as st
import time
from urllib.parse import urlencode
from Components import create_card, footer, logo
st.set_page_config(page_title='Web Based Steganography Tool', page_icon='https://firebasestorage.googleapis.com/v0/b/stegproject-99219.appspot.com/o/favicon.ico?alt=media&token=ba72f22f-3188-4e27-9ed7-19ddad766f0a',layout = 'wide', initial_sidebar_state = 'auto')
# st.set_page_config(layout="wide")
# st.markdown(footer,unsafe_allow_html=True)

if __name__ == "__main__":
    # with st.spinner('Wait for it...'):
    #     time.sleep(2)
    
    st.write("<div style='display:flex;justify-content: center'><h1 style='text-align: center; font-size: 50px;'><b>Web Based Steganography Tool</b></h1></div>",unsafe_allow_html=True)
    st.write("<p style='text-align: center; font-style: italic; font-size: 20px;'>All in one solution to send messages hidden in regular stuff</p>",unsafe_allow_html=True)
    # st.markdown('<a href="/Image_Steganography" target="_self">Next page</a>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.write(create_card('''https://firebasestorage.googleapis.com/v0/b/stegproject-99219.appspot.com/o/imagesteg.png?alt=media&token=17510005-2b8c-4a08-aa1d-7c1b0b14e44f''','''Image Steganography''','''left''','''/Image_Steganography'''),unsafe_allow_html=True)

    with col2:
        st.write(create_card('''https://firebasestorage.googleapis.com/v0/b/stegproject-99219.appspot.com/o/textsteg.png?alt=media&token=3561afd0-7ef0-4a5c-ac0a-3b0011961018''','''Binary Steganography''','''right''','''/Text_Steganography'''),unsafe_allow_html=True)
