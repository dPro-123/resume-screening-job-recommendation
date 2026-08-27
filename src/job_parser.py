
def extract_job_description(file_path):
    """
    Read a text-based job description file.
    """

    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

    return text