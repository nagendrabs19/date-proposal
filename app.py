from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/question")
def question():
    return render_template("question.html")

@app.route("/activity")
def activity():
    return render_template("activity.html")

@app.route("/date")
def date():
    return render_template("date.html")

@app.route("/final")
def final():
    return render_template("final.html")


if __name__ == "__main__":
    app.run(debug=True)