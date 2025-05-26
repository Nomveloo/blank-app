import streamlit as st

st.title("🎈 Testing Project")
st.header("Your new project")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
st.selectbox("Your new project", ("First", "Second"))
st.button("Generate")



