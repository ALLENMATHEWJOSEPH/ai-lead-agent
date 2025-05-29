import re

def clean_text(text):
    """Remove unwanted characters and whitespace."""
    if text:
        return re.sub(r'\s+', ' ', text).strip()
    return ""

def is_valid_url(url):
    """Check if a URL is valid and well-formed."""
    return url.startswith("http")

def deduplicate_leads(leads):
    """Remove duplicate companies based on name or URL."""
    seen = set()
    unique = []
    for lead in leads:
        key = lead.get("Company Name", "").lower()
        if key not in seen:
            seen.add(key)
            unique.append(lead)
    return unique

