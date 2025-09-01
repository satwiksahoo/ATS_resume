import streamlit as st
import os
import pickle
from sentence_transformers import SentenceTransformer, util
import plotly.graph_objects as go
# Load trained model (replace with your path)
# from streamlit_extras.metric_cards import style_metric_cards
# import streamlit as st
# from streamlit_extras.progress_bar import radial_progress

st._config.set_option("server.address", "0.0.0.0")
st._config.set_option("server.port", 8080)

@st.cache_resource
def load_model():
    return SentenceTransformer("artifacts/model_trainer/model5")

model = load_model()

st.set_page_config(page_title="ATS Resume Scorer", page_icon="📄", layout="centered")

st.title("📄 ATS Resume Scorer")
st.write("Upload your resume and paste a job description to get your ATS match score.")

# Upload resume (PDF)
uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

# Enter JD
job_description = st.text_area("Paste Job Description", height=200)

# Submit button
if st.button("Get ATS Score"):
    if uploaded_file is not None and job_description.strip() != "":
        # Save uploaded file temporarily
        resume_path = os.path.join("uploads", uploaded_file.name)
        os.makedirs("uploads", exist_ok=True)
        with open(resume_path, "wb") as f:
            f.write(uploaded_file.read())

        # Extract resume text (dummy example - replace with your PDF parser)
        import fitz  # PyMuPDF
        doc = fitz.open(resume_path)
        resume_text = ""
        for page in doc:
            resume_text += page.get_text("text")
        
        # Encode texts
        resume_emb = model.encode(resume_text, convert_to_tensor=True)
        jd_emb = model.encode(job_description, convert_to_tensor=True)

        # Cosine similarity as ATS score
        
        
        score = util.cos_sim(resume_emb, jd_emb).item()
        # ats_score = round(score * 100, 2)
        ats_score = round((score + 1) / 2 * 100, 2)
        

        st.success(f"✅ Your ATS Score: **{ats_score}%**")
 


    else:
        st.error("Please upload a PDF resume and paste a job description.")
