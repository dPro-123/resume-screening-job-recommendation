
def compare_skills(resume_skills, job_skills):
    """
    Compare resume skills with job-required skills.
    """

    resume_set = set(resume_skills)
    job_set = set(job_skills)

    matched_skills = resume_set.intersection(job_set)
    missing_skills = job_set.difference(resume_set)
    extra_skills = resume_set.difference(job_set)

    return {
        "matched_skills": sorted(matched_skills),
        "missing_skills": sorted(missing_skills),
        "extra_skills": sorted(extra_skills)
    }
    
    
def calculate_skill_match_percentage(
    matched_skills,
    job_skills
):
    """
    Calculate the percentage of required job skills
    that are present in the resume.
    """

    total_required_skills = len(set(job_skills))

    if total_required_skills == 0:
        return 0.0

    matched_count = len(set(matched_skills))

    score = (
        matched_count /
        total_required_skills
    ) * 100

    return round(score, 2)    