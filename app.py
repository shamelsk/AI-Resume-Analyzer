import streamlit as st
from pdf_parser import extract_text_from_pdf
from analyzer import analyze_resume
from report_generator import create_report

# ---------------- Page Configuration ---------------- #

st.set_page_config(
    page_title="ResumeIQ AI",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- Sidebar ---------------- #

with st.sidebar:

    st.title("🤖 ResumeIQ AI")

    st.markdown("---")

    st.subheader("✨ Features")

    st.markdown("""
- 📄 Upload Resume
- 🤖 AI Resume Analysis
- 📊 Resume Score
- 💪 Strengths
- ⚠ Weaknesses
- 📚 Missing Skills
- 💼 Recommended Roles
""")

    st.markdown("---")

    st.subheader("🛠 Tech Stack")

    st.markdown("""
- Python
- Streamlit
- Google Gemini
- PyMuPDF
""")

# ---------------- Main Page ---------------- #

st.title("📄 ResumeIQ AI")

st.caption(
    "Analyze your resume using Google's Gemini AI and receive instant professional feedback."
)

st.subheader("📄 Upload Resume")

uploaded_resume = st.file_uploader(
    "Upload your Resume (PDF)",
    type=["pdf"]
)


# ---------------- PDF Extraction ---------------- #

if uploaded_resume is not None:

    with st.spinner("Extracting Resume..."):
        resume_text = extract_text_from_pdf(uploaded_resume)

    if resume_text.strip() == "":

        st.error("No text could be extracted from this PDF.")

    else:

        st.success("Resume uploaded successfully!")

        with st.expander("View Extracted Resume"):

            st.text_area(
                "Resume Text",
                resume_text,
                height=350
            )
        
        if st.button(
            "🚀 Analyze Resume",
            use_container_width=True,
            type="primary"
        ):

            with st.spinner("🤖 AI is analyzing your resume..."):

                analysis = analyze_resume(resume_text)

            st.success("✅ Analysis completed!")

            st.divider()

            left, center, right = st.columns([1,2,1])

            with center:

                overall = analysis["overall_score"]

                st.metric(
                    label="📊 Overall Resume Score",
                    value=f"{overall}/100"
                )

                st.progress(overall / 100)

                if overall >= 85:
                  st.success("🌟 Excellent Resume")

                elif overall >= 70:
                  st.warning("👍 Good Resume")

                else:
                  st.error("⚠ Resume Needs Improvement")

            st.divider()

            st.subheader("📈 Detailed Analysis")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("ATS Score", analysis["ats_score"])
                st.progress(analysis["ats_score"]/100)

                st.metric("Projects", analysis["projects_score"])
                st.progress(analysis["projects_score"]/100)

            with col2:
                st.metric("Skills", analysis["skills_score"])
                st.progress(analysis["skills_score"]/100)

                st.metric("Experience", analysis["experience_score"])
                st.progress(analysis["experience_score"]/100)

            with col3:
                st.metric("Education", analysis["education_score"])   
                st.progress(analysis["education_score"]/100)   

            st.divider()

            col1, col2 = st.columns(2)

            with col1:

                st.subheader("💪 Strengths")

                for item in analysis["strengths"]:
                    st.success(item)

            with col2:

                st.subheader("⚠ Weaknesses")

                for item in analysis["weaknesses"]:
                    st.error(item)    

            st.divider()

            st.subheader("📚 Missing Skills")

            cols = st.columns(3)

            for i, skill in enumerate(analysis["missing_skills"]):
                cols[i % 3].info(skill)  

            st.divider()

            st.subheader("💡 AI Suggestions")

            for suggestion in analysis["suggestions"]:
                st.write(f"✅ {suggestion}")  

            st.divider()

            st.subheader("💼 Recommended Job Roles")

            for role in analysis["recommended_roles"]:
                st.success(f"🎯 {role}") 

            pdf_path = create_report(analysis)

            with open(pdf_path, "rb") as file:

              st.download_button(
                label="📄 Download AI Report",
                data=file,
                file_name="Resume_Report.pdf",
                mime="application/pdf",
                use_container_width=True
              )      

            st.toast(
              "Resume analyzed successfully!",
              icon="🎉"
            )             

