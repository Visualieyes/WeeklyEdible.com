from flask import Flask, render_template, url_for, request
from werkzeug.utils import redirect

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def register():

    if request.method == "post":
        return redirect(url_for("success"))

    return render_template('register.html')

@app.route("/success", methods=["GET", "POST"])
def index():
    return render_template('success.html')


if __name__ == '__main__':
    app.run(debug=True)