from pyresparser import ResumeParser

def parse_resume(file_path):
    data = ResumeParser(file_path).get_extracted_data()
    return {
        "name": data.get("name"),
        "skills": data.get("skills"),
        "experience": data.get("total_experience"),
        "degree": data.get("degree"),
        "email": data.get("email"),
        "designation": data.get("designation")
    }
