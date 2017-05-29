from flask import Flask
from flask_wtf.csrf import CsrfProtect

UPLOAD_FOLDER = '/media/a_m/Wdisk/Python/Projects/Bank_parser/app/uploaded_file'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'csv', 'xls', 'xlsx'])

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#app.config['ALLOWED_EXTENSIONS'] = ALLOWED_EXTENSIONS
app.config.from_object('config')
CsrfProtect(app)

from app import views