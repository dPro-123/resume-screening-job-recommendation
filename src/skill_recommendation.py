
SKILL_PRIORITY = {
    "python": "High",
    "sql": "High",
    "machine learning": "High",
    "data analysis": "High",
    "data science": "High",
    "deep learning": "Medium",
    "natural language processing": "Medium",
    "scikit-learn": "High",
    "pandas": "High",
    "numpy": "Medium",
    "git": "Medium",
    "github": "Medium",
    "docker": "Medium",
    "aws": "Medium",
    "react": "Medium",
    "node.js": "Medium"
}


def generate_skill_recommendations(missing_skills):
    """
    Generate learning recommendations for missing skills.
    """

    recommendations = []

    for skill in missing_skills:
        priority = SKILL_PRIORITY.get(
            skill,
            "Medium"
        )

        recommendations.append({
            "skill": skill,
            "priority": priority,
            "reason": "Required by the target job"
        })

    return recommendations