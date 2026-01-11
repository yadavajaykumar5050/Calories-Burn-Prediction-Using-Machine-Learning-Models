import numpy as np
import pandas as pd
import streamlit as st
import pickle
import base64
# Function to add background
def add_bg_from_local(image_file):
    with open(image_file, "rb") as f:
        data = f.read()
    encoded_img = base64.b64encode(data).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded_img}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Add background image
add_bg_from_local("ft.jpg")   # Change file name as needed

#load model
rfr = pickle.load(open('rfr.pkl','rb'))
X_train = pd.read_csv("X_train.csv")

def pred(Gender,Age,Height,Weight,Duration,Heart_Rate,Body_Temp):
    features = np.array([[Gender,Age,Height,Weight,Duration,Heart_Rate,Body_Temp]])
    prediction=rfr.predict(features).reshape(1,-1)
    return prediction[0]

#web app

st.title("Calories Burn Prediction By Ajay❤️")

Gender = st.selectbox("Gender",X_train["Gender"])
Age = st.selectbox("Age",X_train["Age"])
Height = st.selectbox("Height",X_train["Height"])
Weight = st.selectbox("Weight",X_train["Weight"])
Duration = st.selectbox("Duration",X_train["Duration"])
Heart_rate= st.selectbox("Heart_Rate(bpm)",X_train["Heart_Rate"])
Body_temp=st.selectbox("Body_Temp",X_train["Body_Temp"])

result=pred(Gender,Age,Height,Weight,Duration,Heart_rate,Body_temp)

# style button
st.markdown("""
    <style>
    .stButton>button {
        background-color: #ff4b4b;
        color: white;
        padding: 10px 20px;
        border-radius: 10px;
        border: none;
        font-size: 18px;
    }
    .stButton>button:hover {
        background-color: #d93636;
    }
    </style>
""", unsafe_allow_html=True)

if st.button("predict"):
    st.markdown(
        f"""
        <p style="color: green; font-size: 22px; font-weight: bold;">
            You have consumed this calories: {result}
        </p>
        """,
        unsafe_allow_html=True
    )
    if result:
        st.write("You have consumed this calories:",result)