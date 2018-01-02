from flask import Flask, request, Markup, render_template, flash
import json
import os

app = Flask(__name__)

def get_title_options():
    with open('classics.json') as classics_data:
        classics = json.load(classics_data)
    titles = []
    for t in classics:
        if t["bibliography"]["title"] not in titles:
            if len(t["bibliography"]["title"]) < 80:
                titles.append(t["bibliography"]["title"])
            else:
                titles.append(t["bibliography"]["title"][:80] + "...")
    options = ""
    for o in titles:
        options += Markup("<option value=\"" + o + "\">" + o + "</option>")
    return options

def get_title_data(title, info):
    with open('classics.json') as classics_data:
        classics = json.load(classics_data)
    i = str(info) + ":"
    b = " "
    d = " "
    for n in classics:
        if n["bibliography"]["title"] == title:
            if info == "Reading Difficulty Information":
                b = "<h4> Flesch Reading Ease: " + str(n["metrics"]["difficulty"]["flesch reading ease"]) + "<br> Automated Readability Index: " + str(n["metrics"]["difficulty"]["automated readability index"]) + "<br> Coleman Liau Index: " + str(n["metrics"]["difficulty"]["coleman liau index"]) + "<br> Gunning Fog: " + str(n["metrics"]["difficulty"]["gunning fog"]) + "<br> Linsear Write Formula: " + str(n["metrics"]["difficulty"]["linsear write formula"]) + "<br> Dale Chall Readability Score: " + str(n["metrics"]["difficulty"]["dale chall readability score"]) + "<br> Flesch Kincaid Grade: " + str(n["metrics"]["difficulty"]["flesch kincaid grade"]) + "<br> Smog Index: " + str(n["metrics"]["difficulty"]["smog index"]) + "<br> Difficult Words: " + str(n["metrics"]["difficulty"]["difficult words"]) + "</h4>"
            if info == "Statistics Information":
                b = "<h4> Polysyllables: " + str(n["metrics"]["statistics"]["polysyllables"]) + "<br> Characters: " + str(n["metrics"]["statistics"]["characters"]) + "<br> Average Sentence Length: " + str(n["metrics"]["statistics"]["average sentence length"]) + "<br> Words: " + str(n["metrics"]["statistics"]["words"]) + "<br> Sentences: " + str(n["metrics"]["statistics"]["sentences"]) + "<br> Syllables: " + str(n["metrics"]["statistics"]["syllables"]) + "<br> Average Sentence per Word: " + str(n["metrics"]["statistics"]["average sentence per word"]) + "<br> Average Letter per Word: " + str(n["metrics"]["statistics"]["average letter per word"]) + "</h4>"
            if info == "Sentiments Information":
                b = "<h4> Polarity: " + str(n["metrics"]["sentiments"]["polarity"]) + "<br> Subjectivity: " + str(n["metrics"]["sentiments"]["subjectivity"]) + "</h4>"
            if info == "Publication Information":
                b = "<h4> Date of Publication: " + str(n["bibliography"]["publication"]["month name"]) + " " + str(n["bibliography"]["publication"]["day"]) + ", " + str(n["bibliography"]["publication"]["year"]) + "</h4"
            if info == "Author Information":
                b = "<h4> Name: " + str(n["bibliography"]["author"]["name"]) + "<br> Birth: " + str(n["bibliography"]["author"]["birth"]) + "<br> Death: " + str(n["bibliography"]["author"]["death"]) + "</h4>"
            if info == "Subjects Information":
                b = "<h4> Subjects: " + str(n["bibliography"]["subjects"]) + "</h4>"
            if info == "Congress Classification Information":
                b = "<h4> Congress Classifications: " + str(n["bibliography"]["congress classifications"]) + "</h4>"
    d = Markup("<h3>" + title + " " + i + "</h3>" + b)
    return d

# def get_genre_data(genre):
#     with open('classics.json') as classics_data:
#         classics = json.load(classics_data)

def get_level_options():
    n = Markup("<option value= 0> Kindergarten </option>")
    for o in range(1, 13):
        i = "Grade " + str(o)
        e = str(o)
        n += Markup("<option value=\"" + e + "\">" + i + "</option>")
    return n

def get_level_data(level):
    with open('classics.json') as classics_data:
        classics = json.load(classics_data)
    list = "nope"
#     for a in classics:
#         if int(a["metrics"]["automated readability index"])-1 > int(level):
# #         +int(a["metrics"]["coleman liau index"])+int(a["metrics"]["gunning fog"])+int(a["metrics"]["flesch kincaid grade"]))/4 > (level -1) and ((a["metrics"]["automated readability index"]-1)+a["metrics"]["coleman liau index"]+a["metrics"]["gunning fog"]+a["metrics"]["flesch kincaid grade"])/4 < (level + 1):
#             list += str(a["bibliography"]["title])
    return level

@app.route("/")
def render_main():
        return render_template('home.html')

@app.route("/bytitle")
def render_t1():
    if 'title' in request.args:
        return render_template('tab1.html', options = get_title_options(), data = get_title_data(request.args['title'], request.args['info']))
    else:
        return render_template('tab1.html', options = get_title_options())

@app.route("/bygenre")
def render_t2():
#         if 'class' in request.args:
#         return render_template('tab2.html', data = get_genre_data(request.args['genre']))
#     else:
        return render_template('tab2.html')

@app.route("/bylevel")
def render_t3():
    if 'level' in request.args:
        return render_template('tab3.html', options = get_level_options(), data = get_level_data(request.args['level']))
    else:
        return render_template('tab3.html', options = get_level_options())


if __name__=="__main__":
    app.run(debug=False)

    
