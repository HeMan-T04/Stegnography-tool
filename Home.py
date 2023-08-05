import streamlit as st
import time
from urllib.parse import urlencode

st.set_page_config(layout="wide")
def create_card(url, title,align,link):
    c1='''
        <a href="'''+link+'''" target="_self">
        <div style=" margin-'''+align+''':15rem;">
        <div>
        <img src="
        '''+url+'''" alt='image'  style="object-fit: cover; width: 100%; height:25rem;border-top-right-radius: 20px;border-top-left-radius: 20px;">
        <div style='background-color: #1a202b; padding: 10px; border-bottom-right-radius: 20px;border-bottom-left-radius: 20px; width: 100%;margin-bottom:1rem;'>
        <h5 style='text-align: center; font-style: italic; font-size: 20px;'>'''+title+'''</h5>
        </div>
        </div>
        </div></a>'''
#     c1='''
#         <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous">
# <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-HwwvtgBNo3bZJJLYd8oVXjrBZt8cqVSpeBNS5n7C8IVInixGAoxmnlMuBnhbgrkm" crossorigin="anonymous"></script>
# <div class="container" style="display:flex; justify-content: '''+align+''';">
# <div class="card text-bg-dark" style="width: 60%;margin-bottom:1rem;">
#   <img src="
#         '''+url+'''" " class="card-img-top" style="display:flex; object-fit: cover; width: 100%; height:20rem;" alt="...">
#   <div class="card-body w-100">
#     <h5 class="card-text"style='text-align: center; font-style: italic;'>'''+title+'''</h5>
#   </div>
# </div></div>'''
    return c1
footer="""<style>
a:link , a:visited{
color:inherit;
background-color: transparent;
}

a:hover,  a:active {
background-color: transparent;
}

.footer {
position: fixed;
left: 0;
zindex:2147483647;
bottom: 0;
width: 100%;
background-color: #0e1117;
color: white;
text-align: right;
padding-right: 3vw;
}
</style>
<div class="footer">
<p>Developed with ❤ by <a style='text-align: center;' href="https://github.com/HeMan-T04" target="_blank">Hemant Kathuria</a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)

if __name__ == "__main__":
    # with st.spinner('Wait for it...'):
    #     time.sleep(2)
    st.write("<h1 style='text-align: center; font-size: 50px;'><b>Web Based Steganography Tool</b></h1>",unsafe_allow_html=True)
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
