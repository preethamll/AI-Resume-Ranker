import pandas as pd
from utils import extract_text

def clean(text):
    if not text:
        return []
    return text.lower().replace(",", " ").replace(".", " ").split()

def score_resume(resume_text, jd_text):

    resume_words = set(clean(resume_text))
    jd_words = set(clean(jd_text))

    if len(jd_words) == 0:
        return 0

    matches = resume_words.intersection(jd_words)
    score = (len(matches) / len(jd_words)) * 100

    return round(score, 2)

def rank_resumes(resume_paths, job_desc):

    jd_text = job_desc.lower()

    resume_scores = []
    
    for path in resume_paths:
        resume_text = extract_text(path)
        print("====== EXTRACTED RESUME TEXT ======")
        print(resume_text)

        score = score_resume(resume_text, jd_text)
        resume_scores.append((path, score))

    df = pd.DataFrame(resume_scores, columns=["Resume", "Score"])
    df = df.sort_values(by="Score", ascending=False)

    df.to_csv("outputs/resume_scores.csv", index=False)

    return df

