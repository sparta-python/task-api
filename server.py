from flask import Flask
from flask import request
from flask import render_template
from flask import jsonify
from flask import flash
from flask import redirect
import secrets

import api_get

app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(32)


@app.route("/")
def show_form():
    return render_template("index.html")


@app.route("/post")
def post():
    print(request.json)
    data = "ok"
    return jsonify(data)


@app.route("/post", methods=["GET", "POST"])
def upload_image():
    if request.method == "POST":
        animal = request.form["animal"]
        if animal == "cat":
            outanimal = api_get.cat()

        elif animal == "dog":
            outanimal = api_get.dog()

        elif animal == "fox":
            outanimal = api_get.fox()
        
        else:
            outanimal = ""

        return render_template("post.html", outanimal=outanimal)

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
