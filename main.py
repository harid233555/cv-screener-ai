from fastapi import FastAPI, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from app.parser import parse_resume
from app.matcher import get_similarity
from app.scorer import score_candidate

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/screen")
async def screen_cv(file: UploadFile, job_description: str = Form(...)):
    with open("temp.pdf", "wb") as f:
        f.write(await file.read())
    resume_data = parse_resume("temp.pdf")
    skills_text = " ".join(resume_data.get("skills") or [])
    similarity = get_similarity(skills_text, job_description)
    score = score_candidate(resume_data, job_description.split(), 2)
    return {
        "candidate": resume_data.get("name"),
        "similarity": similarity,
        "score": score
    }
