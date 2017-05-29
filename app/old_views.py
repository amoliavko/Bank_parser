from flask import render_template,request
from app import app

MAX_FILE_SIZE = 1024 * 1024 * 50 + 1
@app.route("/", methods=["POST", "GET"])
def index():
    args = {"method": "GET"}
    if request.method == "POST":
        file = request.files["file"]
        if bool(file.filename):
            file_bytes = file.read(MAX_FILE_SIZE)
            args["file_size_error"] = len(file_bytes) == MAX_FILE_SIZE
        args["method"] = "POST"
    return render_template("index.html", args=args)