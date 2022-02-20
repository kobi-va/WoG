from flask import *
import Utils
import os

linux_home = (os.path.expanduser('~'))


file = Utils.score_file()
if os.name == "nt":
    app = Flask(__name__, template_folder="../WoG_Project")
else:
    app = Flask(__name__, template_folder=f"{linux_home}/WoG_Project")


@app.route("/")
def score_server():
    if os.name == "nt":
        f = open(file, "r")
    else:
        f = open(f"{linux_home}/WoG_Project/{file}", "r")
    score = f.read()
    return render_template("score.html", score=score)


app.run(host='localhost', port=1234)
