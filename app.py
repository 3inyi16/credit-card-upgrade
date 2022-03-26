from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return(render_template("index.html", result1="1", result2="1", result3="1"))

    else:
        return(render_template("index.html", result1="2", result2="2", result3='2'))


if __name__ == "__main__":
    app.run()

#http://127.0.0.1:5000