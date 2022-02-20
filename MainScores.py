from flask import *
import Utils


file = Utils.score_file()
app = Flask(__name__, template_folder="../WoG_Project")


@app.route("/")
def score_server():
    f = open(file, "r")
    score = f.read()
    return render_template("score.html", score=score)


app.run(host='localhost', port=1234)
