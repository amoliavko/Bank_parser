from flask import render_template, request, redirect, url_for, send_from_directory
from app import app
from app.form import LoadFile
import pandas as pd
import os
from werkzeug.utils import secure_filename
from app.parsers import BcbParser, BcbForeignParser, ProcreditbankParser, AvalParser, Centercredit, PrivatParser, UkrEximParser, VtbParser


MAX_FILE_SIZE = 1024 * 1024 * 50 + 1
ALLOWED_EXTENSIONS = set(['txt', 'xls', 'xlsx'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    args = {'method': 'GET'}
    form = LoadFile()
    if form.is_submitted() and request.method == 'POST':
            file = request.files['file']
            if bool(file.filename):
                bank_select = form.bank_select.data
                args['method'] = 'POST'

                if bank_select =='Bsbbank':
                    filename = secure_filename(file.filename)
                    file_address = os.path.join('static', filename)
                    file.save(file_address)
                    out = BcbParser.file_parser(file_address)

                    df = pd.DataFrame(out)
                    df = df.rename(columns={0:'Банк',	1:'Дата', 2:'Дебет', 3:'Кредит', 4:'Валюта', 5:'Назначение', 6:'Агент', 7:'Счет', 8:'ЄДРПОУ'})
                    writer =pd.ExcelWriter('static/result.xlsx', engine='xlsxwriter')
                    df.to_excel(writer, sheet_name='Sheet1', index=False)
                    writer.save()
                    link = os.path.join('static', 'result.xlsx')

                    return render_template("load_successful.html", file=out, link=link)

                if bank_select =='Aval':
                    filename = secure_filename(file.filename)
                    file_address = os.path.join('static', filename)
                    file.save(file_address)
                    out = AvalParser.file_parser(file_address)

                    df = pd.DataFrame(out)
                    writer =pd.ExcelWriter('static/result.xlsx', engine='xlsxwriter')
                    df.to_excel(writer, sheet_name='Sheet1', index=False)
                    writer.save()
                    link = os.path.join('static', 'result.xlsx')

                    return render_template("load_successful.html", file=out, link=link)

                if bank_select =='Centercredit':
                    filename = secure_filename(file.filename)
                    file_address = os.path.join('static', filename)
                    file.save(file_address)
                    out = Centercredit.file_parser(file_address)

                    df = pd.DataFrame(out)
                    writer =pd.ExcelWriter('static/result.xlsx', engine='xlsxwriter')
                    df.to_excel(writer, sheet_name='Sheet1', index=False)
                    writer.save()
                    link = os.path.join('static', 'result.xlsx')

                    return render_template("load_successful.html", file=out, link=link)


                if bank_select =='Privat':
                    filename = secure_filename(file.filename)
                    file_address = os.path.join('static', filename)
                    file.save(file_address)
                    out = PrivatParser.file_parser(file_address)

                    df = pd.DataFrame(out)
                    writer =pd.ExcelWriter('static/result.xlsx', engine='xlsxwriter')
                    df.to_excel(writer, sheet_name='Sheet1', index=False)
                    writer.save()
                    link = os.path.join('static', 'result.xlsx')

                    return render_template("load_successful.html", file=out, link=link)


                if bank_select =='Procreditbank':
                    filename = secure_filename(file.filename)
                    file_address = os.path.join('static', filename)
                    file.save(file_address)
                    out = ProcreditbankParser.file_parser(file_address)

                    df = pd.DataFrame(out)
                    writer =pd.ExcelWriter('static/result.xlsx', engine='xlsxwriter')
                    df.to_excel(writer, sheet_name='Sheet1', index=False)
                    writer.save()
                    link = os.path.join('static', 'result.xlsx')

                    return render_template("load_successful.html", file=out, link=link)

                if bank_select =='Vtb':
                    filename = secure_filename(file.filename)
                    file_address = os.path.join('static', filename)
                    file.save(file_address)
                    out = VtbParser.file_parser(file_address)

                    df = pd.DataFrame(out)
                    writer =pd.ExcelWriter('static/result.xlsx', engine='xlsxwriter')
                    df.to_excel(writer, sheet_name='Sheet1', index=False)
                    writer.save()
                    link = os.path.join('static', 'result.xlsx')

                    return render_template("load_successful.html", file=out, link=link)


                if bank_select =='BsbbankForeign':
                    filename = secure_filename(file.filename)
                    file_address = os.path.join('static', filename)
                    file.save(file_address)
                    out = BcbForeignParser.file_parser(file_address)

                    df = pd.DataFrame(out)
                    writer =pd.ExcelWriter('static/result.xlsx', engine='xlsxwriter')
                    df.to_excel(writer, sheet_name='Sheet1', index=False)
                    writer.save()
                    link = os.path.join('static', 'result.xlsx')

                    return render_template("load_successful.html", file=out, link=link)

                if bank_select =='Alfa':
                    filename = secure_filename(file.filename)
                    file_address = os.path.join('static', filename)
                    file.save(file_address)
                    out = BP.file_parser(file_address)

                    df = pd.DataFrame(out)
                    writer =pd.ExcelWriter('static/result.xlsx', engine='xlsxwriter')
                    df.to_excel(writer, sheet_name='Sheet1', index=False)
                    writer.save()
                    link = os.path.join('static', 'result.xlsx')

                    return render_template("load_successful.html", file=out, link=link)


                if bank_select =='UkrExim':
                    filename = secure_filename(file.filename)
                    file_address = os.path.join('static', filename)
                    file.save(file_address)
                    out = UkrEximParser.file_parser(file_address)

                    df = pd.DataFrame(out)
                    writer =pd.ExcelWriter('static/result.xlsx', engine='xlsxwriter')
                    df.to_excel(writer, sheet_name='Sheet1', index=False)
                    writer.save()
                    link = os.path.join('static', 'result.xlsx')

                    return render_template("load_successful.html", file=out, link=link)

                else:
                    pass
    return render_template("index.html", args=args, form=form)
