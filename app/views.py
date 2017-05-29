from flask import render_template, request, redirect, url_for, send_from_directory
from app import app
from app.form import LoadFile
from pandas import read_csv, read_excel
import os
from werkzeug.utils import secure_filename


MAX_FILE_SIZE = 1024 * 1024 * 50 + 1


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=["POST", "GET"])
def index():
    args = {"method": "GET"}
    form = LoadFile()
    if form.is_submitted():
        if request.method == "POST":
            file = request.files["file"]
            if bool(file.filename):
                bank_select = form.bank_select.data
                args["method"] = "POST"

                if bank_select =="Avangard":
                    lf1 = read_csv(file, encoding='cp1251')
                    filename = secure_filename(file.filename)
                    file_address = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                    file.save(file_address)
                    return send_from_directory(file_address, filename)
  #                  return redirect(url_for('index', filename=filename))
  #                  return render_template("load_successful.html", bank_select=bank_select, file=link)
                else:
                    pass
    return render_template("index.html", args=args, form=form)
