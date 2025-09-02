import streamlit as st
import os
import pickle
from sentence_transformers import SentenceTransformer, util
import plotly.graph_objects as go
# Load trained model (replace with your path)
# from streamlit_extras.metric_cards import style_metric_cards
# import streamlit as st
# from streamlit_extras.progress_bar import radial_progress
#added streamlit 
st._config.set_option("server.address", "0.0.0.0")
st._config.set_option("server.port", 8080)


import os
import boto3
# s3 addedcv
def download_model_from_s3():
    s3 = boto3.client("s3")
    bucket = "resumeats1"
    prefix = "model5/"

    # local dir matches prefix name
    local_dir = os.path.join(os.getcwd(), prefix.strip("/"))
    os.makedirs(local_dir, exist_ok=True)

    response = s3.list_objects_v2(Bucket=bucket, Prefix=prefix)
    if "Contents" not in response:
        print(f"⚠️ No files in {bucket}/{prefix}")
        return

    for obj in response["Contents"]:
        key = obj["Key"]
        if key.endswith("/"):
            continue

        local_path = os.path.join(local_dir, os.path.relpath(key, prefix))
        os.makedirs(os.path.dirname(local_path), exist_ok=True)
        s3.download_file(bucket, key, local_path)
        print(f"⬇️ {key} → {local_path}")

    print("✅ Done")
    
    
    # s3 = boto3.client("s3")
    # bucket = "resumeats1"
    # prefix = "artifacts/model_trainer/model5"

    # local_dir = "artifacts/model_trainer/model5"
    # os.makedirs(local_dir, exist_ok=True)

    # # download all files
    # for obj in s3.list_objects_v2(Bucket=bucket, Prefix=prefix)['Contents']:
    #     key = obj["Key"]
    #     local_path = os.path.join(local_dir, os.path.relpath(key, prefix))
    #     os.makedirs(os.path.dirname(local_path), exist_ok=True)
    #     s3.download_file(bucket, key, local_path)





# def download_from_s3(bucket, prefixes):
#     """
#     Download all files from multiple S3 prefixes into local folders.
#     """
#     s3 = boto3.client("s3")

#     for prefix in prefixes:
#         # local target folder (same structure as S3)
#         local_dir = os.path.join(os.getcwd(), prefix.strip("/"))
#         os.makedirs(local_dir, exist_ok=True)

#         print(f"🔍 Looking for files in s3://{bucket}/{prefix}")

#         response = s3.list_objects_v2(Bucket=bucket, Prefix=prefix)

#         if "Contents" not in response:
#             print(f"⚠️ No objects found in s3://{bucket}/{prefix}")
#             continue

#         for obj in response["Contents"]:
#             key = obj["Key"]

#             # skip "directories"
#             if key.endswith("/"):
#                 continue

#             filename = os.path.basename(key)
#             local_path = os.path.join(local_dir, filename)

#             print(f"⬇️ Downloading {key} → {local_path}")
#             s3.download_file(bucket, key, local_path)

#     print("✅ Download complete.")
@st.cache_resource
def load_model():
    if not os.path.exists("artifacts/model_trainer/model5"):
        bucket_name = "resumeats1"
        prefixes = ["artifacts/", "model5/"]
        # download_from_s3(bucket_name, prefixes)
        
        download_model_from_s3()
    return SentenceTransformer("artifacts/model_trainer/model5")

# git push --set-upstream origin main

# @st.cache_resource
# def load_model():
#     return SentenceTransformer("artifacts/model_trainer/model5")

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
