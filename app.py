from flask import Flask, render_template

app = Flask(
    __name__,
    template_folder="build",
    static_folder="build/static",
)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload/drive", methods=["POST"])
def upload_to_drive():
    return "UPLOADED"