import re


TECHNICAL_SKILLS = {
    "python",
    "java",
    "c",
    "c++",
    "c#",
    "javascript",
    "typescript",
    "html",
    "css",
    "react",
    "node.js",
    "flask",
    "django",
    "sql",
    "mysql",
    "postgresql",
    "mongodb",
    "pandas",
    "numpy",
    "scikit-learn",
    "tensorflow",
    "pytorch",
    "keras",
    "machine learning",
    "deep learning",
    "natural language processing",
    
    "computer vision",
    "data science",
    "data analysis",
    "statistics",
    "git",
    "github",
    "docker",
    "aws",
    "azure",
    "power bi",
    "tableau"
}

SHORT_SKILLS = {
    "c",
    "c++",
    "c#",
    "r",
    "go"
}


SKILL_ALIASES = {
    "ml": "machine learning",
    "machine-learning": "machine learning",
    "machinelearning": "machine learning",

    "dl": "deep learning",
    "deep-learning": "deep learning",

    "nlp": "natural language processing",
    "natural-language-processing": "natural language processing",

    "sklearn": "scikit-learn",
    "scikit learn": "scikit-learn",

    "react.js": "react",
    "reactjs": "react",

    "node": "node.js",
    "nodejs": "node.js",

    "powerbi": "power bi",
    "power-bi": "power bi"
}


def extract_skills(text):
    """
    Extract technical skills and normalize known aliases.
    """

    text = text.lower()

    found_skills = set()

    # Standard technical skills
    for skill in TECHNICAL_SKILLS:

        if skill in SHORT_SKILLS:
            pattern = rf"(?<![a-z0-9]){re.escape(skill)}(?![a-z0-9])"
        else:
            pattern = rf"\b{re.escape(skill)}\b"

        if re.search(pattern, text):
            found_skills.add(skill)

    # Skill aliases
    for alias, normalized_skill in SKILL_ALIASES.items():

        if alias in SHORT_SKILLS:
            pattern = rf"(?<![a-z0-9]){re.escape(alias)}(?![a-z0-9])"
        else:
            pattern = rf"\b{re.escape(alias)}\b"

        if re.search(pattern, text):
            found_skills.add(normalized_skill)

    return sorted(found_skills)


