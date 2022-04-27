from flask import Flask
import json

app = Flask (__name__)

@app.route ("/")
def page_index():
    
    with open("candidates.json", "r", encoding="utf_8") as file:
        candidates = json.load(file)
    result = ""
    for candidate in candidates:
        result += "Имя: " + candidate["name"]+ "\n"
        result += "Позиция кандидата: " + candidate["position"]+ "\n"
        result += "Навыки: " + candidate["skills"]+ "\n"
        result += "\n"

    return f"<pre>\n{result}\n</pre>"

@app.route("/candidates/<int:x>")
def page_candidate (x):
    x -= 1
    with open("candidates.json", "r", encoding="utf_8") as file:
        candidates = json.load(file)
    result =""
    if x >= len(candidates):
        result+="Не найдено"
        return result
    candidate = candidates[x]
    
    result += f"<img src = \"{candidate['picture']}\">"
    result +="\n"
    result += "<pre>\n"
    result += "Имя: " + candidate["name"]+ "\n"
    result += "Позиция кандидата: " + candidate["position"]+ "\n"
    result += "Навыки: " + candidate["skills"]+ "\n"
    result += "\n</pre>"
       
    return result


@app.route("/skills/<x>")
def page_skills (x):
    with open("candidates.json", "r", encoding="utf_8") as file:
        candidates = json.load(file)
    result = ""
    for candidate in candidates:
        skills = candidate["skills"].split(", ")
        if x in skills:
            result += "Имя: " + candidate["name"]+ "\n"
            result += "Позиция кандидата: " + candidate["position"]+ "\n"
            result += "Навыки: " + candidate["skills"]+ "\n"
            result += "\n"
                    
    
    if result == "":
        result +="Не найдено"

    return f"<pre>\n{result}\n</pre>"



app.run ()