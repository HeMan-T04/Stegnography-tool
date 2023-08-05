import streamlit as st
from Components import footer
st.set_page_config(layout="wide")
if __name__ == "__main__":
    st.markdown(footer,unsafe_allow_html=True)
    st.write("<h1 style='font-size: 50px;'><b>Web Based Steganography Tool</b></h1>",unsafe_allow_html=True)
    st.write("<div style='text-align: justify;'><p>In today's digital era, information security has become a critical concern. To protect sensitive data from unauthorized access, various techniques have been developed, and one such technique is steganography. Steganography is the art and science of concealing information within different types of media, such as images, audio, video, and text, without arousing suspicion. With the widespread use of the internet and digital communication channels, web-based steganography tools have gained significant importance. These tools provide a convenient and accessible platform for users to embed secret messages within seemingly innocent files, making it challenging for adversaries to detect and intercept sensitive information.</p><p>The goal of this project is to design and develop a comprehensive web-based steganography tool that supports multiple types of media, including images, audio, video, and text. This tool enables users to encode and decode secret messages in various file formats, thereby ensuring secure communication and data transfer.</p><p>The web-based nature of this tool offers several advantages. Firstly, it eliminates the need for users to install any specialized software on their devices, as the tool can be accessed through a web browser. This convenience increases accessibility and makes it easier for individuals with limited technical expertise to utilize steganography techniques for secure communication. Additionally, a web-based steganography tool allows for seamless integration with other web services and applications. This integration opens up possibilities for embedding and extracting secret messages within popular social media platforms, email services, or cloud storage solutions, enhancing the versatility and utility of the tool.</p></div>",unsafe_allow_html=True)
    st.write("<h2 style='font-size: 30px;'><b>Features</b></h2>",unsafe_allow_html=True)
    st.markdown("<ul style='text-align:justify'><li><h5 style='padding-bottom:0.3rem'>Image Steganography:</h5><p>Image steganography is the practice of hiding confidential data within a cover image. One well-known approach to image steganography is the Least Significant Bit (LSB) method. The idea behind LSB embedding is that if we change the last bit value of a pixel, there won’t be much visible change in the color. For example, 0 is black. Changing the value to 1 won’t make much of a difference since it is still black, just a lighter shade. <br/>LSB methods are vulnerable to changes resulting from lossy compression or image processing. Therefore, it is best to use lossless image compression formats like PNG when applying LSB techniques for image steganography. Lossless compression ensures that the original data can be recovered exactly when the image is decompressed, which is important for retrieving the hidden data.</p></li><li><h5>Audio Steganography</h5><p>Coming Soon....</p></li><li><h5>Video Steganography</h5><p>Coming Soon....</p></li><li><h5>Text Steganography</h5><p>Coming Soon....</p></li></ul>",unsafe_allow_html=True)
    st.write("<h2 style='font-size: 30px;'><b>About Developers</b></h2>",unsafe_allow_html=True)
    st.write("<h3 style='font-size: 20px;'><b>Hemant Kathuria</b></h3>",unsafe_allow_html=True)
    st.markdown('''
    - A passionate developer
    - Playing CTF's at spare time
    - A heavy Cybersecuirty Enthusiast 
    - Future Goal till now: To go in Digital Forensics
    - Currently learning Streamlit, Opencv, Google Proffessional Certificate, Nptel Ethical Hacking (Ya, I am multitasking)
    - Current Project: Web based Stegnography tool(is in the repos)
    - Currently Using : Endeavour OS and Windows 11(Dual Booted)(Don't Prefer Windows much just for gaming)
    - I’m currently open for an Intern or a new job opportunity, this is [my resume](https://drive.google.com/file/d/19ZK1cttBAOpZuFLkPsQp1OolMOC5VRTa/view?usp=sharing) ''',unsafe_allow_html=True)
    st.markdown('''## <b> Let's Connect..!</b><br/><div align='left'><ul><li><a href="https://www.linkedin.com/in/hemant-kathuria-638977232/" target="_blank"><img src="https://img.shields.io/badge/linkedin:  HeManT04-%2300acee.svg?color=405DE6&style=for-the-badge&logo=linkedin&logoColor=white" alt=linkedin style="margin-bottom: 5px;"/></a></li><li><a href="https://twitter.com/He_man_T04" target="_blank"><img src="https://img.shields.io/badge/twitter:  HeManT04-%2300acee.svg?color=1DA1F2&style=for-the-badge&logo=twitter&logoColor=white" alt=twitter style="margin-bottom: 5px;"/></a></li><li><a href="mailto:hemantkathuria04@gmail.com" target="_blank"><img src="https://img.shields.io/badge/gmail:  HeManT04-%23EA4335.svg?style=for-the-badge&logo=gmail&logoColor=white" t=mail style="margin-bottom: 5px;" /></a></li><li><a href="https://drive.google.com/file/d/19ZK1cttBAOpZuFLkPsQp1OolMOC5VRTa/view?usp=sharing" target="_blank"><img src="https://img.shields.io/badge/Resume:  HeManT04-%23EA4335.svg?style=for-the-badge&logo=R&logoColor=white" t=mail style="margin-bottom: 5px;" /></a></li></ul></div>''',unsafe_allow_html=True)

