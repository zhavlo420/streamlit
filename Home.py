import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image
from streamlit_extras.let_it_rain import rain
from annotated_text import annotated_text
from streamlit_extras.app_logo import add_logo
from streamlit_extras.colored_header import colored_header
from streamlit_extras.stoggle import stoggle
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title="Portfolio", page_icon="👾",layout="wide")
st.sidebar.success("Select Page")
add_logo("pfp.jpg")

rain(
    emoji="🗿",
    font_size=50,
    falling_speed=4,
    animation_length="infinite"
)



def lot(url):
    r=requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()


lotte=lot("https://assets4.lottiefiles.com/packages/lf20_pJvtiSVyYH.json")
lotte2=lot("https://assets6.lottiefiles.com/packages/lf20_w51pcehl.json")
img1=Image.open("Untitled.png")
img2=Image.open("Comp 2 (0-00-00-00).png")
with st.container():
   
    #with m:
        
        st.title("Hey Folks👾,")
       # st.write("---")
        #with l:
        st.subheader("My name is Soham I'm a Computer Science UG")
        #st.write("Pretty Much into VFX/GFX/Programming/Digital Marketing")
        
        from annotated_text import annotated_text, annotation
        annotated_text(
    "Pretty much into ",
    annotation("VFX/GFX/CODING/DIGITAL MARKETING","skills", color="#8ef", border="1px dashed red"),
)
st.write("[Learn More](https://www.linkedin.com/in/soham-dange-0a5310251/)")
st.write("##")
    
   # with r:
        #st.write("##")
       # st_lottie(lotte2,height=200,key="e")


with st.container():
   # st.write("---")
    left_col,right_col=st.columns(2)
    with left_col:
        st.header("Familiar with:")
        #st.write("##")
        
        st.write("HTML,CSS,JS,REACTJS,THREEJS,C++,PYTHON,C++,SQL technologies")
        st.header("Non Tech Firms:")
        st.write("Sony Vegas PRO,AFTER EFFECTS,PHOTOSHOP")


        
        colored_header(
    label="✅ Services i offer as a Freelancer",
    description="",
    color_name="violet-70",
)
        st.write("1️⃣ Video Editing")
        st.write("2️⃣ Youtube Channel Banner,Twitch Overlays")
        st.write("3️⃣ OBS Setup for Streaming")
        st.write("4️⃣ Responsive Websites using(spline,reactjs,threejs)")
        st.write("5️⃣ Data Visualsation(matlab,streamlit,pyplot)")
        st.write("6️⃣ Responsive Python GUI's")
        st.write("7️⃣3D Model/Environment Renders")
       
        colored_header(
    label="",
    description="",
    color_name="light-blue-70",
)
        st.subheader("Feel Free to Reach OUT")
        st.text("DISCORD:")
        st.write("Zhavlo#3739")
        st.write("☑[YouTube](https://www.youtube.com/@zhavlo)")
        with right_col:
            st_lottie(lotte2,height=700,key="poop")
        
        
        img,text=st.columns((1,2))
        with img:
            st.subheader("Projects")
            st.write("☑[Github](https://www.github/com/zhavlo420)")
            
            st.write("☑[VFX/GFX/3D content](https://drive.google.com/drive/folders/1DlXMWuR43Yftl1C6IgKh0Nm6rqU-6dQm?usp=sharing)")
            st.image(img1)
            st.image(img2)
            
stoggle("Surprise MF!",""" https://images.app.goo.gl/KCiJWdJEEpRWaTDe9""")