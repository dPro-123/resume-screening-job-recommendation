
from src.preprocessing import preprocess_text
from src.skill_extraction import extract_skills


def process_job(job):
    """
    Preprocess a job description and extract its skills.
    """

    raw_text = job["description"]

    clean_text = preprocess_text(raw_text)

    extracted_skills = extract_skills(clean_text)

    processed_job = job.copy()

    processed_job["clean_description"] = clean_text
    processed_job["extracted_skills"] = extracted_skills

    return processed_job


def process_all_jobs(jobs):
    """
    Process every job in the job dataset.
    """

    processed_jobs = []

    for job in jobs:
        processed_job = process_job(job)
        processed_jobs.append(processed_job)

    return processed_jobs