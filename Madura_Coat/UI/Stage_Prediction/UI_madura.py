import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import pickle
st.markdown("<h1 style='text-align:center;colour:white;'>CKD Stage </h1>",unsafe_allow_html=True)

# st.text_input("En",placeholder="heeloo")

# import streamlit as st
col1,col2=st.columns(2)
c = st.container()
gfr=col1.text_input("eGFR")
cre=col1.text_input("Creatinine")
cal=col1.text_input("Calcium")
phos=col1.text_input("Phosphate")
potas=col1.text_input("Potassium")
acr=col2.text_input("ACR")
albu=col2.text_input("Albumin")
bicar=col2.text_input("Bicarbonate")
sodi=col2.text_input("Sodium")
hae=col2.text_input("Haemoglobin")

st.write("---")
col=st.columns(7)
s=[]
with col[3]:
    enter=st.button("Predict",type='primary')
if enter:
    s2=[acr,gfr,cre,hae,cal,phos,potas,sodi,albu,bicar]
    s3=[]
    for i in s2:
        s3.append(float(i))
    with open('neighbor','rb') as file:
        model=pickle.load(file)
    value=model.predict([s3])
    stage=value[0]
    if(stage==1):st.write("<h5 style='background-color: llightgreen;border-radius: 10px; color: black;text-align: center;'>It's a first stage</h5>",unsafe_allow_html=True)
    if(stage==2):st.write("<h5 style='background-color: palegoldenyellow;border-radius: 10px; color: black;text-align: center;'>It's a second stage</h5>",unsafe_allow_html=True)
    if(stage==3):st.write("<h5 style='background-color: yellow;border-radius: 10px; color: black;text-align: center;'>",unsafe_allow_html=True)
    # with col[]:
    if(stage==4):st.write("<h5 style='background-color: orange;border-radius: 10px; color: black;text-align: center;'>It's a fourth stage</h5>",unsafe_allow_html=True)
    if(stage==5):st.write("<h5 style='background-color: red;border-radius: 10px; color: black;text-align: center;'>It's a fifth stage</h5>",unsafe_allow_html=True)