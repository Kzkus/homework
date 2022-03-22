from flask import Flask
import json
import utils

candidates = utils.load_candidates()

app = Flask(__name__)
@app.route("/")
def page_index():
    for candidate in candidates.values():
        str_candidates += f"{candidate['name']}<br>{candidate['position']}<br>{candidate['skills']}<br><br>"
    return str_candidates

@app.route("/candidates/<int:id>")
def profile(id):
    candidate = candidates[id]
    str_candidates = f"<img src={candidate['picture']}></img><br>{candidate['name']}<br>{candidate['position']}<br>{candidate['skills']}<br><br>"
    return str_candidates

@app.route("/skills/<skill>")
def skills(skill):
    for candidate in candidates.values():
        candidate_skills = candidate['skills'].split(', ')
        candidate_skills = [x.lower() for x in candidate_skills]
        if skill in candidate_skills:
            str_candidates += f"{candidate['name']} <br>{candidate['position']} <br>{candidate['skills']} <br><br>"
    return str_candidates

app.run()