
import pandas as pd
from pathlib import Path


def load_job_dataset(csv_path):
    """
    Load job metadata from CSV.
    """

    df = pd.read_csv(csv_path)

    return df


def load_job_description(file_path):
    """
    Load the complete text of a job description.
    """

    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

    return text


def load_all_jobs(csv_path):
    """
    Load job metadata and complete job descriptions
    for all jobs in the dataset.
    """

    df = pd.read_csv(csv_path)

    jobs = []

    for _, row in df.iterrows():

        job = {
            "job_id": row["job_id"],
            "job_title": row["job_title"],
            "domain": row["domain"],
            "file_path": row["file_path"],
            "required_skills": row["required_skills"].split("|"),
            "description": load_job_description(
                row["file_path"]
            )
        }

        jobs.append(job)

    return jobs