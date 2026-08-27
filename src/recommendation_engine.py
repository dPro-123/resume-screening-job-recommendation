# =========================
# Imports
# =========================


import pandas as pd
from src.skill_matching import (
    compare_skills,
    calculate_skill_match_percentage
)

from src.semantic_matching import (
    calculate_semantic_similarity
)

from src.match_score import (
    calculate_hybrid_score
)

from src.preprocessing import preprocess_text
from src.skill_extraction import extract_skills
from src.resume_parser import extract_resume_text

# =========================
# Job scoring
# =========================

def score_job(resume_skills, resume_text, job):

    skill_gap = compare_skills(
        resume_skills,
        job["extracted_skills"]
    )

    skill_match_score = calculate_skill_match_percentage(
        skill_gap["matched_skills"],
        job["extracted_skills"]
    )

    semantic_score = calculate_semantic_similarity(
        resume_text,
        job["clean_description"]
    )

    hybrid_score = calculate_hybrid_score(
        skill_match_score,
        semantic_score
    )

    return {
        "skill_match_score": skill_match_score,
        "semantic_score": semantic_score,
        "hybrid_score": hybrid_score
    }

# =========================
# Match strength
# =========================


def get_match_strength(score):

    if score >= 80:
        return "Excellent Match"

    elif score >= 65:
        return "Strong Match"

    elif score >= 50:
        return "Moderate Match"

    else:
        return "Weak Match"
    
# =========================
# Generate recommendations
# =========================


def generate_recommendations(
    resume_skills,
    resume_text,
    processed_jobs,
    top_n=5
):

    results = []

    for job in processed_jobs:

        score = score_job(
            resume_skills,
            resume_text,
            job
        )

        results.append({
            "job_id": job["job_id"],
            "job_title": job["job_title"],
            "domain": job["domain"],
            "skill_match_score": score["skill_match_score"],
            "semantic_score": score["semantic_score"],
            "hybrid_score": score["hybrid_score"]
        })

    results_df = pd.DataFrame(results)

    ranked_jobs = (
        results_df
        .sort_values(
            by="hybrid_score",
            ascending=False
        )
        .reset_index(drop=True)
    )

    domain_scores = (
        results_df
        .groupby("domain")["hybrid_score"]
        .mean()
        .sort_values(ascending=False)
    )

    top_jobs = ranked_jobs.head(top_n)

    recommendations = []

    for _, ranked_job in top_jobs.iterrows():

        job_id = ranked_job["job_id"]

        processed_job = next(
            job for job in processed_jobs
            if job["job_id"] == job_id
        )

        skill_gap = compare_skills(
            resume_skills,
            processed_job["extracted_skills"]
        )

        recommendations.append({
            "job_id": job_id,
            "job_title": ranked_job["job_title"],
            "domain": ranked_job["domain"],
            "skill_match_score": ranked_job["skill_match_score"],
            "semantic_score": ranked_job["semantic_score"],
            "hybrid_score": ranked_job["hybrid_score"],
            "match_strength": get_match_strength(
                ranked_job["hybrid_score"]
            ),
            "matched_skills": skill_gap["matched_skills"],
            "missing_skills": skill_gap["missing_skills"],
            "extra_skills": skill_gap["extra_skills"]
        })

    best_domain = domain_scores.index[0]
    best_domain_score = domain_scores.iloc[0]

    return {
        "recommended_domain": best_domain,
        "domain_score": best_domain_score,
        "domain_scores": domain_scores,
        "recommendations": recommendations,
        "ranked_jobs": ranked_jobs
    }
    
# =========================
# Prepare recommendation output
# =========================
   
def prepare_recommendation_output(final_results):

    output = {
        "recommended_domain": final_results["recommended_domain"],
        "domain_score": round(
            final_results["domain_score"],
            2
        ),
        "recommendations": []
    }

    for job in final_results["recommendations"]:

        output["recommendations"].append({
            "job_title": job["job_title"],
            "domain": job["domain"],
            "skill_match_score": round(
                job["skill_match_score"],
                2
            ),
            "semantic_score": round(
                job["semantic_score"],
                2
            ),
            "hybrid_score": round(
                job["hybrid_score"],
                2
            ),
            "match_strength": job["match_strength"],
            "matched_skills": job["matched_skills"],
            "missing_skills": job["missing_skills"],
            "extra_skills": job["extra_skills"]
        })

    return output
# =========================
# Recommendation pipeline
# =========================

def run_recommendation_pipeline(
    resume_skills,
    resume_text,
    processed_jobs,
    top_n=5
):

    final_results = generate_recommendations(
        resume_skills,
        resume_text,
        processed_jobs,
        top_n=top_n
    )

    app_output = prepare_recommendation_output(
        final_results
    )

    return app_output

# =========================
# Resume processing
# =========================


def process_resume(resume_text):

    cleaned_text = preprocess_text(
        resume_text
    )

    resume_skills = extract_skills(
        cleaned_text
    )

    return {
        "resume_text": cleaned_text,
        "resume_skills": resume_skills
    }
    
def recommend_from_resume(
    resume_text,
    processed_jobs,
    top_n=5
):

    processed_resume = process_resume(
        resume_text
    )

    result = run_recommendation_pipeline(
        processed_resume["resume_skills"],
        processed_resume["resume_text"],
        processed_jobs,
        top_n=top_n
    )

    return result
# =========================
# PDF resume recommendation
# =========================

def recommend_from_resume_file(
    file_path,
    processed_jobs,
    top_n=5
):

    resume_text = extract_resume_text(
        file_path
    )

    result = recommend_from_resume(
        resume_text,
        processed_jobs,
        top_n=top_n
    )

    return result
# =========================
# Format recommendation results
# =========================

def format_recommendation_results(result):
    formatted_jobs=[]
    for job in result["recommendations"]:
        
        formatted_jobs.append({
            "Job Title": job["job_title"],
            "Domain": job["domain"],
            "Skill Match": job["skill_match_score"],
            "Semantic Score": job["semantic_score"],
            "Hybrid Score": job["hybrid_score"],
            "Match Strength": job["match_strength"],
            "Matched Skills": job["matched_skills"],
            "Missing Skills": job["missing_skills"],
            "Extra Skills": job["extra_skills"]
        })

    return {
        "Recommended Domain": result["recommended_domain"],
        "Domain Score": result["domain_score"],
        "Recommendations": formatted_jobs
    }


