
from pathlib import Path
import tempfile
import os
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))



import pandas as pd

import streamlit as st

import src.recommendation_engine as recommendation_engine

from src.job_processing import process_all_jobs

st.set_page_config(
    page_title="Resume Job Recommender",
    page_icon="📄",
    layout="wide"
)

# Project root
PROJECT_ROOT = Path(__file__).resolve().parent.parent



JOBS_CSV = PROJECT_ROOT / "data" / "raw" / "jobs.csv"

jobs_df = pd.read_csv(
    JOBS_CSV
)

jobs = jobs_df.to_dict(orient="records")

for job in jobs:

    relative_path = job["file_path"]

    relative_path = relative_path.replace(
        "../",
        "",
        1
    )

    file_path = (
        PROJECT_ROOT / relative_path
    ).resolve()

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        job["description"] = file.read()

processed_jobs = process_all_jobs(jobs)


st.markdown("""
<style>

    /* ============================= */
    /* MAIN APPLICATION BACKGROUND */
    /* ============================= */

    .stApp {
        background: #f8fafc;
        color: #1e293b;
    }

    .main {
        padding-top: 2rem;
    }


    
    /* ============================= */
    /* GENERAL TEXT */
    /* ============================= */

    .stApp p,
    .stApp label {
        color: #1e293b;
    }

    h2, h3 {
        color: #0f172a !important;
    }


    /* ============================= */
    /* METRIC CARDS */
    /* ============================= */

    div[data-testid="stMetric"] {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        padding: 1rem;
        border-radius: 15px;
        box-shadow: 0 5px 20px rgba(0, 0, 0, 0.08);
    }

    div[data-testid="stMetricLabel"] {
        color: #475569 !important;
    }

    div[data-testid="stMetricValue"] {
        color: #0369a1 !important;
    }


    /* ============================= */
    /* EXPANDERS */
    /* ============================= */

    div[data-testid="stExpander"] {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 15px;
        margin-bottom: 12px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.06);
    }


    /* ============================= */
    /* BUTTON */
    /* ============================= */

    .stButton > button {
        background: linear-gradient(
            135deg,
            #2563eb,
            #06b6d4
        );

        color: #ffffff !important;

        border: none;
        border-radius: 10px;
        padding: 0.6rem 1.5rem;

        font-weight: 600;

        transition: 0.3s;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(6, 182, 212, 0.35);
    }


    /* ============================= */
    /* FILE UPLOADER */
    /* ============================= */

    div[data-testid="stFileUploader"] {
        background: #ffffff;
        border-radius: 15px;
        padding: 1rem;
        border: 1px dashed #94a3b8;
    }


    /* ============================= */
    /* SIDEBAR */
    /* ============================= */

    section[data-testid="stSidebar"] {
    background: #eef6ff;
    border-right: 1px solid #dbeafe;
 }

    section[data-testid="stSidebar"] h1 {
    color: #0f172a !important;
    font-size: 1.6rem;
    font-weight: 700;
 }

    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 {
    color: #1e3a8a !important;
    font-weight: 600;
}

    section[data-testid="stSidebar"] p,
    section[data-testid="stSidebar"] span,
    section[data-testid="stSidebar"] label {
    color: #334155 !important;
}

    section[data-testid="stSidebar"] hr {
    border-color: #cbd5e1;
}


    /* ============================= */
    /* ALERTS */
    /* ============================= */

    div[data-testid="stAlert"] {
        border-radius: 12px;
    }


    /* ============================= */
    /* DOWNLOAD BUTTON */
    /* ============================= */

    div[data-testid="stDownloadButton"] button {
        background: #0f766e;
        color: #ffffff !important;
        border: none;
        border-radius: 10px;
        font-weight: 600;
    }

</style>
""", unsafe_allow_html=True)
with st.sidebar:

    st.markdown(
    "# 📄 ResumeMatch AI"
)

    st.markdown(
    "### Smart Resume Analysis. Better Career Decisions."
)

    st.write(
    "Transform your resume into actionable career insights "
    "with AI-powered skill extraction, semantic matching, "
    "and personalized job recommendations."
)
    

    st.divider()

    st.subheader("🔍 How It Works")

    st.write(
        "1. Upload your resume"
    )

    st.write(
        "2. Extract skills and resume information"
    )

    st.write(
        "3. Compare with job descriptions"
    )

    st.write(
        "4. Calculate skill and semantic similarity"
    )

    st.write(
        "5. Generate hybrid match scores"
    )

    st.write(
        "6. Rank suitable jobs"
    )

    st.divider()

    st.caption(
        "Built with Python, NLP, TF-IDF, "
        "Streamlit and Machine Learning."
    )
    

## resume recommendation pdf
st.title("📄 Resume Screening & Job Recommendation")
st.subheader("📤 Upload Your Resume")
st.write(
    "Upload your resume in PDF format to receive "
    "personalized job recommendations."
)

uploaded_file = st.file_uploader(
    "Upload your resume",
    type=["pdf"],
    help="Maximum file size: 5 MB"
)

if uploaded_file is not None:
    
    if uploaded_file.size == 0:

        st.error(
            "❌ The uploaded file is empty. "
            "Please upload a valid PDF."
        )

        st.stop()

    if uploaded_file.size > 5 * 1024 * 1024:

        st.error(
            "❌ File size exceeds the 5 MB limit. "
            "Please upload a smaller PDF."
        )

        st.stop()

    else:
     st.success(
        f"✅ {uploaded_file.name} uploaded successfully"
    )

    file_size_mb = uploaded_file.size / (1024 * 1024)

    st.caption(
        f"File size: {file_size_mb:.2f} MB"
    )

    analyze_button = st.button(
        "🔍 Analyze Resume"
    )
    
    if analyze_button:
        
        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".pdf"
        ) as temp_file:

            temp_file.write(
                uploaded_file.getvalue()
            )

            temp_path = temp_file.name

        try:

            with st.spinner(
    "🔍 Analyzing your resume and matching jobs..."
        ):
             result = recommendation_engine.recommend_from_resume_file(
              temp_path,
              processed_jobs,
              top_n=5
    )
        
            
        
            # recommendation results 
            st.subheader("🎯 Recommended Domain")

            st.metric(
              "Best Domain",
               result["recommended_domain"]
)

            st.metric(
                "Domain Score",
                f'{result["domain_score"]:.2f}%'
)
            st.subheader("📊 Resume Analysis Summary")
            summary_col1, summary_col2, summary_col3 = st.columns(3)
            
            with summary_col1:
                st.metric(
                                "Recommended Domain",
                                result["recommended_domain"]
                            )
            
            with summary_col2:
                            st.metric(
                                "Domain Score",
                                f'{result["domain_score"]:.2f}%'
                            )
            
            with summary_col3:
                            st.metric(
                                "Top Jobs Analyzed",
                                len(result["recommendations"])
                            )
            #top job recommendation

            st.subheader("💼 Top Job Recommendations")

            for i, job in enumerate(
                  result["recommendations"],
                  start=1
            ):

              with st.expander(
                       f"{i}. {job['job_title']} — "
                       f"{job['hybrid_score']:.2f}%"
             ):



                col1, col2, col3 = st.columns(3)

                with col1:
                    st.metric(
                        "Hybrid Score",
                        f'{job["hybrid_score"]:.2f}%'
        )
                with col2:
                        st.metric(
                            "Skill Match",
                            f'{job["skill_match_score"]:.2f}%'
                        )
    

                with col3:
                        st.metric(
                            "Semantic Score",
                            f'{job["semantic_score"]:.2f}%'
                        )

                st.write(
                        f"**Match Strength:** {job['match_strength']}"
                    )

                st.write(
                        "**Matched Skills:**",
                        ", ".join(job["matched_skills"])
                    )
                
                
                        
                if job["missing_skills"]:

                          st.warning(
                                "Missing Skills: "
                                    + ", ".join(job["missing_skills"])
    )
                else:

                          st.success(
                          "No missing required skills"
    )

                
            st.divider()
            #download recommendation results
            st.subheader("📥 Download Results")

            download_data = []

            for job in result["recommendations"]:

                download_data.append(
                    {
                        "Job Title": job["job_title"],
                        "Hybrid Score": job["hybrid_score"],
                        "Skill Match Score": job["skill_match_score"],
                        "Semantic Score": job["semantic_score"],
                        "Match Strength": job["match_strength"],
                        "Matched Skills": ", ".join(job["matched_skills"]),
                        "Missing Skills": ", ".join(job["missing_skills"])
                    }
                )
            download_df = pd.DataFrame(download_data)

            csv_data = download_df.to_csv(
               index=False
)

            st.download_button(
               label="📥 Download Job Recommendations",
               data=csv_data,
               file_name="job_recommendations.csv",
               mime="text/csv"
)
            
            # job score interpretation 
            
            st.subheader("📖 Score Interpretation")

            st.write(
    "The Hybrid Score combines skill matching and semantic "
    "similarity between your resume and the job description."
)

            st.info(
    "Higher scores indicate a stronger overall match. "
    "The score is based on the skills detected in your resume "
    "and how semantically similar your resume is to the job."
)
            

            # job match comparison
            st.subheader("📈 Job Match Comparison")

            chart_data = pd.DataFrame({
               "Job": [
                  job["job_title"]
                  for job in result["recommendations"]
    ],
               "Hybrid Score": [
                   job["hybrid_score"]
                   for job in result["recommendations"]
    ]
})

            st.bar_chart(
            chart_data.set_index("Job")
)
            
            # job gap analysis 
            
            st.subheader("📚 Skill Gap Analysis")
            all_missing_skills = {}

            for job in result["recommendations"]:

                for skill in job["missing_skills"]:

                    all_missing_skills[skill] = (
                    all_missing_skills.get(skill, 0) + 1
        )

            if all_missing_skills:

                skill_gap_df = pd.DataFrame(
           {
                  "Skill": list(all_missing_skills.keys()),
                  "Number of Jobs": list(all_missing_skills.values())
        }
    )

                skill_gap_df = skill_gap_df.sort_values(
                    "Number of Jobs",
                     ascending=False
    )

                st.dataframe(
                    skill_gap_df,
                    use_container_width=True,
                    hide_index=True
    )

            else:

               st.success(
                  "🎉 No major skill gaps found in the recommended jobs!"
    )

            
               
            st.session_state["result"] = result
            
            st.info(
    f"📄 Analyzed Resume: **{uploaded_file.name}**"
)
            
        finally:

            os.remove(temp_path)