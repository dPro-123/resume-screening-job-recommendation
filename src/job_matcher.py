
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


def score_job(resume_skills, resume_text, job):
    """
    Calculate the complete resume-job matching score.
    """

    # 1. Compare skills
    skill_comparison = compare_skills(
        resume_skills,
        job["extracted_skills"]
    )

    matched_skills = skill_comparison["matched_skills"]
    missing_skills = skill_comparison["missing_skills"]
    extra_skills = skill_comparison["extra_skills"]

    # 2. Calculate skill match percentage
    skill_match_score = calculate_skill_match_percentage(
        matched_skills,
        job["extracted_skills"]
    )

    # 3. Calculate semantic similarity
    semantic_score = calculate_semantic_similarity(
        resume_text,
        job["clean_description"]
    )

    # 4. Calculate hybrid score
    hybrid_score = calculate_hybrid_score(
        skill_match_score,
        semantic_score
    )

    # 5. Store all results
    result = {
        "job_id": job["job_id"],
        "job_title": job["job_title"],
        "domain": job["domain"],
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "extra_skills": extra_skills,
        "skill_match_score": skill_match_score,
        "semantic_score": semantic_score,
        "hybrid_score": hybrid_score
    }

    return result