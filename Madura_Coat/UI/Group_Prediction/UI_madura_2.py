import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import pickle
st.markdown("<h1 style='text-align:center;colour:white;'>CKD Stage </h1>",unsafe_allow_html=True)

# st.text_input("En",placeholder="heeloo")

# import streamlit as st
col1,col2,col3,col4=st.columns(4)
with col1:
    st.markdown("<h3><u>Lifestyles</h3>",unsafe_allow_html=True)
    Age=st.text_input("Age")
    Bmi=st.text_input("BMI")
    Diabetes=st.text_input("Diabetes")
    Hypertension=st.text_input("Hypertension")
    Current_Stage=st.text_input("Current_Stage",help="if you don't had ckd type nil")

with col2:
    st.markdown("<h3><u>Requirements</h3>",unsafe_allow_html=True)
    Gfr=st.text_input("eGFR")
    Acr=st.text_input("ACR",help="Albumin to Cretinine Ratio")
    albumin=st.text_input("Albumin")
    cretinine=st.text_input("Cretinine")
    sodium=st.text_input("Sodium")

with col3:
    st.markdown("<h3 style='color:white'><u>Requirements</h3>",unsafe_allow_html=True)
    haemoglobin=st.text_input("Haemoglobin")
    phosphate=st.text_input("Phosphate")
    potassium=st.text_input("Potassium")
    calcium=st.text_input("Calcium")
    bicarbonate=st.text_input("Bicarbonate")

with col4:
    st.markdown("<h3 style='color:white'>Life</h3>",unsafe_allow_html=True)
    m1=st.text_input("Medicine A")
    m2=st.text_input("Medicine B")
    m3=st.text_input("Medicine C")
    m4=st.text_input("Medicine D")
    m5=st.text_input("Medicine E")

st.write("---")
col=st.columns(7)
s=[]
with col[3]:
    enter=st.button("Predict",type='primary')
if enter:
    #'Age', 'BMI', 'Diabetes', 'Hypertension', 'Albumin to Creatinine Ratio',
    #   'Glomerular Filtration Rate', 'Serum Creatinine Level',
     #  'Hemoglobin Level', 'Serum Calcium Level', 'Serum Phosphate Level',
      ##'Serum Bicarbonate Level', 'Stage', 'Med_1', 'Med_2', 'Med_3', 'Med_4',
       #'Med_5'
    s2=[Age,Bmi,Diabetes,Hypertension,Acr,Gfr,cretinine,haemoglobin,calcium,phosphate,potassium,sodium,albumin,bicarbonate,Current_Stage,m1,m2,m3,m4,m5]
    s3=[]
    for i in s2:
        s3.append(float(i))
    with open('Mark2','rb') as file:
        model=pickle.load(file)
    value=model.predict([s3])
    stage=value[0]
    if(stage==0):a=int(s3[-6])+1
    if(stage==1):a=int(s3[-6])-1
    if(stage==0):st.write("<h5 style=color: red;text-align: center;'>Progression to stage </h5>",a,unsafe_allow_html=True)
    if(stage==1):st.write("<h5 style=color: green;text-align: center;'>Regression to stage </h5>",a,unsafe_allow_html=True)
    # if(stage==3):st.write("<h5 style='background-color: yellow;border-radius: 10px; color: black;text-align: center;'>It's a third stage</h5>",unsafe_allow_html=True)
    # # with col[]:
    # if(stage==4):st.write("<h5 style='background-color: orange;border-radius: 10px; color: black;text-align: center;'>It's a fourth stage</h5>",unsafe_allow_html=True)
    # if(stage==5):st.write("<h5 style='background-color: red;border-radius: 10px; color: black;text-align: center;'>It's a fifth stage</h5>",unsafe_allow_html=True)