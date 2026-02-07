import re


def get_lines(text):
    return [l.strip() for l in text.split("\n") if l.strip()]


def extract_name(text):
    lines = get_lines(text)

    for line in lines[:5]:
        if "@" not in line and not re.search(r"\d", line):
            return line
    return None


def extract_email(text):
    match = re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+", text)
    return match.group(0) if match else None


def extract_phone(text):
    match = re.search(r"(\+?\d[\d\-\s]{8,}\d)", text)
    return match.group(0) if match else None


def extract_skills(text):
    match = re.search(
        r"skills(.*?)(education|experience|projects|$)", text, re.S | re.I
    )

    if not match:
        return []

    skill_text = match.group(1)
    skills = re.split(r",|\n|•|-", skill_text)

    return [s.strip() for s in skills if len(s.strip()) > 1]


def extract_projects(text):
    match = re.search(
        r"projects(.*?)(education|experience|skills|certifications|$)",
        text,
        re.S | re.I,
    )

    if not match:
        return []

    project_text = match.group(1)

    # split lines / bullets
    raw_items = re.split(r"\n|•|\||\u2022", project_text)

    cleaned = []

    for item in raw_items:
        item = item.strip()

        # remove leading dashes or symbols
        item = re.sub(r"^[\-–—:\s]+", "", item)

        # remove extra spaces
        item = re.sub(r"\s+", " ", item)

        # ignore too short / useless lines
        if len(item) < 4:
            continue

        # skip common headings
        if item.lower() in ["projects", "project"]:
            continue

        cleaned.append(item)

    return cleaned


def parse_resume(text):
    return {
        "name": extract_name(text),
        "email": extract_email(text),
        "phone": extract_phone(text),
        "skills": extract_skills(text),
        "projects": extract_projects(text),
    }
