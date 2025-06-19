def score_candidate(resume, job_keywords, min_exp):
    matched_skills = len(set(resume.get("skills") or []).intersection(set(job_keywords)))
    experience_score = 1 if resume.get("experience") and resume["experience"] >= min_exp else 0
    score = (matched_skills * 10) + (experience_score * 20)
    return score
