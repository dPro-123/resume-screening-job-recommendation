# =========================
# Hybrid match score
# =========================

def calculate_hybrid_score(
    skill_match_score,
    semantic_similarity_score,
    skill_weight=0.6,
    semantic_weight=0.4
):
    """
    Calculate the final hybrid resume-job match score.

    Parameters
    ----------
    skill_match_score : float
        Percentage of required skills matched.

    semantic_similarity_score : float
        TF-IDF cosine similarity percentage.

    skill_weight : float
        Weight assigned to skill matching.

    semantic_weight : float
        Weight assigned to semantic similarity.

    Returns
    -------
    float
        Final hybrid match score.
    """

    if skill_weight + semantic_weight != 1:
        raise ValueError(
            "Weights must sum to 1."
        )

    hybrid_score = (
        skill_weight * skill_match_score
        + semantic_weight * semantic_similarity_score
    )

    return round(hybrid_score, 2)