import sys
import streamlit as st
# import streamlit_authenticator as stauth
from streamlit.components.v1 import html
import yaml
from yaml import SafeLoader
from hidePage import hidePage
from extractPage import extractPage
from LogsPage import LogsPage
from Components import footer, work_in_progress
st.set_page_config(page_title='Text Steganography',page_icon='https://firebasestorage.googleapis.com/v0/b/stegproject-99219.appspot.com/o/favicon.ico?alt=media&token=ba72f22f-3188-4e27-9ed7-19ddad766f0a', layout = 'wide', initial_sidebar_state = 'auto')
st.markdown(footer,unsafe_allow_html=True)


with open('config.yaml') as coverFile:
    config = yaml.load(coverFile, Loader=SafeLoader)

# authenticator = stauth.Authenticate(
#     config['credentials'],
#     config['cookie']['name'],
#     config['cookie']['key'],
#     config['cookie']['expiry_days'],
#     config['preauthorized']
# )

css = f'''
        <style>
        *{{
            box-sizing: "border-box"
        }}
        header {{visibility: hidden;}}
        span.css-10trblm{{

        }}
        img[alt="logo"]{{
            width: 50px;
            height: 50px;
             (.9)
            }}
        .block-container{{
            padding-top:0px;
            margin-top:0px;

        }}
        button[role="tab"]>div>p{{
            font-size:1.4rem;
            margin-bottom: 1rem;
        }}
        button[role="tab"]{{
            background: none;
        }}
        .row-widget.stButton,.row-widget.stDownloadButton{{
            display:flex;
            justify-content:center;
        }}
        div[data-baseweb="tab-highlight"]{{
        }}
        div[data-testid="stVerticalBlock"]{{


        }}
        div[role="tablist"]{{
            padding-top:0rem;
            margin: 10px 0px;
        }}
        div[data-testid="stCaptionContainer"]{{
            font-size:1.1rem;
        }}
        </style>
        '''
st.title(
    "Binary Steganography", anchor="binary-steganography")
st.caption("Steganography is the technique of hiding secret data within an ordinary, non-secret, file or message in order to avoid detection this tool hides your secret data in a exe/elf executable file ")
st.markdown(css, unsafe_allow_html=True)



# name, authentication_status, username = authenticator.login('Login', 'main')

# if authentication_status:
#     hideTab, extractTab, logs = st.tabs(["Hide", "Extract",'logs'])
#     with hideTab:
#         hidePage(username)
#     with extractTab:
#         extractPage()
#     with logs:
#         LogsPage(username)
#     authenticator.logout('Logout', 'sidebar')
# elif authentication_status == False:
#     st.error('Username/password is incorrect', icon="⁉️")
# elif authentication_status == None:
#     st.warning('Login to continue', icon="⚠️")
hideTab, extractTab = st.tabs(["Encode", "Decode"])
with hideTab:
    hidePage()
with extractTab:
    extractPage()