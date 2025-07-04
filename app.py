
import streamlit as st
from resume_parser import extract_text_from_pdf
from review_engine import analyze_resume

st.set_page_config(page_title="Resume Review Bot", layout="centered")
st.title("📄 AI-Powered Resume Review Bot")

uploaded_file = st.file_uploader("Upload your resume (PDF only)", type=["pdf"])

if uploaded_file is not None:
    with st.spinner("Reading your resume..."):
        resume_text = extract_text_from_pdf(uploaded_file)

    st.subheader("🧾 Extracted Resume Text")
    st.text_area("Text", resume_text, height=300)

    if st.button("🔍 Analyze Resume"):
        with st.spinner("Analyzing with AI..."):
            feedback = analyze_resume(resume_text)
        st.subheader("🧠 Feedback")
        st.write(feedback)
