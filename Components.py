# Card Components
def create_card(url, title,align,link):
    c1='''
        <style>
        </style>
        <a href="'''+link+'''" target="_self">
        <div style=" margin-'''+align+''':10vw;">
        <div>
        <img src="
        '''+url+'''" alt='image'  style="object-fit: cover; width: 100%; height:25rem;border-top-right-radius: 20px;border-top-left-radius: 20px;">
        <div style='background-color: #1a202b; padding: 10px; border-bottom-right-radius: 20px;border-bottom-left-radius: 20px; width: 100%;margin-bottom:1rem;'>
        <h5 style='text-align: center; font-style: italic; font-size: 20px;'>'''+title+'''</h5>
        </div>
        </div>
        </div></a>'''
    return c1
# Logo component
logo='''
<style>
a:link , a:visited{
color:inherit;
background-color: transparent;
}

a:hover,  a:active {
background-color: transparent;
}

.logo {
position: fixed;
top: 1;
zindex:2147483647;
left:100;
text-align: left;
}
</style>
<div class="logo">
<img src="https://firebasestorage.googleapis.com/v0/b/stegproject-99219.appspot.com/o/logo-e78ff0ab.webp?alt=media&token=03ddd35d-006c-40cd-9ced-86b7ef0d7c9f" width="150" height="150"></div>
'''
# footer component


# Work in progress component
work_in_progress='''<div style='display:flex; justify-content: center;margin-top:2rem;'><img src='https://firebasestorage.googleapis.com/v0/b/stegproject-99219.appspot.com/o/wip.gif?alt=media&token=fe840370-1ac6-4ac7-a585-b96198698ba8' style='border-radius: 1rem'></div><h4 style='text-align: center;'><b>Work in Progress</b></h4>'''
'''& <a style='text-align: center;' href="https://github.com/HeMan-T04" target="_blank">Dinesh Thakur</a>'''