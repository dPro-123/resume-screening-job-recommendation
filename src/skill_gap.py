
def analyze_skill_gap(resume_skills, job_skills):
    """
    Analyze the skill gap between a resume and a job description.

    Returns matched, missing, and extra skills along with
    skill gap percentage.
    """

    resume_set = set(resume_skills)
    job_set = set(job_skills)

    matched_skills = resume_set.intersection(job_set)
    missing_skills = job_set.difference(resume_set)
    extra_skills = resume_set.difference(job_set)

    total_required_skills = len(job_set)

    if total_required_skills == 0:
        skill_gap_percentage = 0.0
    else:
        skill_gap_percentage = (
            len(missing_skills)
            / total_required_skills
        ) * 100

    return {
        "matched_skills": sorted(matched_skills),
        "missing_skills": sorted(missing_skills),
        "extra_skills": sorted(extra_skills),
        "skill_gap_percentage": round(
            skill_gap_percentage,
            2
        )
    }