# Card Components
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
    return c1

# footer component
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
padding-right: 4vw;
}
</style>
<div class="footer">
<p>Developed by <a style='text-align: center;' href="https://github.com/HeMan-T04" target="_blank">Hemant Kathuria</a></p>
</div>
"""

# Work in progress component
work_in_progress='''<div style='display:flex; justify-content: center;margin-top:10rem;'><img src='https://firebasestorage.googleapis.com/v0/b/stegproject-99219.appspot.com/o/wip.gif?alt=media&token=fe840370-1ac6-4ac7-a585-b96198698ba8' style='border-radius: 1rem'></div><h4 style='text-align: center;'><b>Work in Progress</b></h4>'''