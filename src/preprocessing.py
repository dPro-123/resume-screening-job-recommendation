
import re


def preprocess_text(text):
    """
    Clean and normalize text for resume/job analysis.
    """

    # Convert to lowercase
    text = text.lower()

    # Remove URLs
    text = re.sub(r"https?://\S+|www\.\S+", " ", text)

    # Remove email addresses
    text = re.sub(r"\S+@\S+", " ", text)

    # Keep letters, numbers, spaces, and selected symbols
    text = re.sub(r"[^a-z0-9\s+#.\-]", " ", text)

    # Replace multiple spaces with a single space
    text = re.sub(r"\s+", " ", text).strip()

    return text