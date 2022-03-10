from flask import *
import Utils
import os
import sys

file = Utils.score_file()
app = Flask(__name__, template_folder="./")


@app.route("/")
def score_server():
    try:
        f = open(f"./{file}", "r")
        score = f.read()
        return render_template("score.html", score=score)
        f.close()
    except:
        return render_template("error.html", Error="Error")


sys.stdout = open(os.devnull, "w")

app.run(host='localhost', port=1234)
