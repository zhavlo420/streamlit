import streamlit as st
import requests
from streamlit_lottie import st_lottie


st.sidebar.success("Select Page from above")

def lot(url1):
    r=requests.get(url1)
    if r.status_code!=200:
        return None
    return r.json()


lotte3=lot("https://assets10.lottiefiles.com/packages/lf20_g4nzoqba.json")


with st.container():

        st.header("Contact📧")
        st.write("##")
    
contactform="""

<form action="https://formsubmit.co/zylodaweeb@gmail.com" method="POST">
<input type="hidden" name="_captcha" value="false">
<input type="text" name="name" placeholder="ur name" required>
<input type="email" name="email" placeholder="ur email here" required>
<textarea name="message" name="message" placeholder="message here" required> </textarea> 
<button type="submit">Send</button>
</form>
"""
st.markdown(contactform,unsafe_allow_html=True)



st_lottie(lotte3,height=500,key="cont")
