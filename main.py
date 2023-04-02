import streamlit as st
import pandas as pd

df = pd.read_csv("data.csv")

st.set_page_config(layout="wide")

st.title("Company Name")
content = """It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. 
The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. 
Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. 
Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like)."""
st.write(content)


st.title("Our Team")

col1, col2, col3 = st.columns(3)

with col1:
    for index, row in df[:4].iterrows():
        st.image("images/" + row["image"])
        st.subheader(f'{row["first name"].title()+" "+row["last name"].title()}')
        st.write(row["role"])

with col2:
    for index, row in df[4:8].iterrows():
        st.image("images/" + row["image"])
        st.subheader(f'{row["first name"].title()+" "+row["last name"].title()}')
        st.write(row["role"])

with col3:
    for index, row in df[8:].iterrows():
        st.image("images/" + row["image"])
        st.subheader(f'{row["first name"].title()+" "+row["last name"].title()}')
        st.write(row["role"])