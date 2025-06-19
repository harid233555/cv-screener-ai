import streamlit as st
import requests

st.title("AI CV Screener")
jd_text = st.text_area("Paste Job Description")
uploaded_file = st.file_uploader("Upload CV (PDF)")

if uploaded_file and jd_text:
    files = {'file': uploaded_file}
    data = {'job_description': jd_text}
    res = requests.post("http://localhost:8000/screen", files=files, data=data)
    if res.ok:
        output = res.json()
        st.success(f"Candidate: {output['candidate']}")
        st.info(f"Score: {output['score']}")
        st.info(f"Similarity: {output['similarity']:.2f}")
    else:
        st.error("Error occurred while processing the CV.")
