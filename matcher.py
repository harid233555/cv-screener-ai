from sentence_transformers import SentenceTransformer, util
import torch

model = SentenceTransformer('all-MiniLM-L6-v2')

def get_similarity(cv_text, jd_text):
    emb_cv = model.encode(cv_text, convert_to_tensor=True)
    emb_jd = model.encode(jd_text, convert_to_tensor=True)
    similarity = util.cos_sim(emb_cv, emb_jd)
    return similarity.item()
