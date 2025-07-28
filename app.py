import streamlit as st

st.title(" Welcome from My Dating App👋!")
st.write("Thank you so much for visiting. It always means so much to see you!")
import streamlit as st

st.title("<Let's Fill to Get a Bf or Gf>")

name = st.text_input("Please write your name:")
if st.button("Greet"):
    st.success(f"Hello, {name}, Have a Nice Day!")
st.title("Survey")

age = st.selectbox("Your Age:", ["under 18", "18 to 35", " above 35"])
gender = st.selectbox("Gender:", ["Male", "Female", " LGBT", "Other"])
Beauty_Rating = st.slider("Select your beauty level:", 1, 100)
Favorite_foods = st.selectbox("Favorite foods:", ["Spicy", "Sweet", "Sour", "Salty", "Bitter, and Umami"])
Pets = st.text_input("do you have any pets:")
Fav_Memory = st.text_input("What is your favorite childhood memory?")
Relationaship = st.text_input("When was your last relationship?")
Idea_of_First_Date = st.text_input("What's your ideal first date?")
Ex = st.text_input("Are you friends with your exes")
Siblings = st.text_input("Do you have any siblings?")


agree = st.checkbox("I agree to terms")

if st.button("Submit"):
    if agree:
        st.write(f"Age: {age}, Gender: {gender}")
    else:
        st.warning("You need to agree first.")
import pandas as pd
import numpy as np

st.title("📊 Simple Chart Example")

data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['under 18', '18 to 35', 'above 35']
)

st.line_chart(data)
st.bar_chart(data)
st.write(data)

import streamlit as st
from PIL import Image
import pandas as pd

uploaded_file = st.file_uploader("Choose a file", type=["csv", "txt", "png", "jpg", "jpeg"])

if uploaded_file:
    st.write("Filename:", uploaded_file.name)

    if uploaded_file.name.endswith((".csv", ".txt")):
        try:
            df = pd.read_csv(uploaded_file, encoding='latin1', delimiter='\t')
            st.dataframe(df)
        except Exception as e:
            st.error(f"Error reading CSV: {e}")

    elif uploaded_file.name.endswith((".jpg", ".jpeg", ".png")):
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)

st.sidebar.title("Sidebar Example")
username = st.sidebar.text_input("Username")
st.write(f"Welcome, {username}")

    




