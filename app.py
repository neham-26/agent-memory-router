import streamlit as st

st.set_page_config(
    page_title="AI Memory Router",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 AI Memory Router")

st.write("Welcome to the AI Memory Router Project!")

question = st.text_input("Ask a question")

if st.button("Ask Question"):
    st.success("Button is working!")
    st.write("Your question:", question)