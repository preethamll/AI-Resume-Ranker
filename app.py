import streamlit as st
import os
from resume_ranker import rank_resumes

st.title("AI Resume Ranker")

job_desc = st.text_area("Enter Job Description:", height=200)

uploaded_files = st.file_uploader("Upload Resumes (PDF only)", type="pdf", accept_multiple_files=True)

if st.button("Rank Resumes"):

    if not job_desc:
        st.error("Please enter job description!")
    elif not uploaded_files:
        st.error("Please upload at least one resume!")
    else:

        # FIX: Create upload folder
        if not os.path.exists("uploads"):
            os.makedirs("uploads")

        paths = []
        for file in uploaded_files:
            path = f"uploads/{file.name}"
            with open(path, "wb") as f:
                f.write(file.getbuffer())
            paths.append(path)

        result = rank_resumes(paths, job_desc)

        st.success("Ranking Completed!")
        st.dataframe(result)
