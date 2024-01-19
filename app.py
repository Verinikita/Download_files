from flask import Flask, render_template, request, flash, redirect, url_for
from werkzeug.utils import secure_filename
from zipfile import ZipFile
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './downlo'

ALLOWED_EXTENSIONS = {'zip'}
@app.route('/procesar_zip', methods=['POST'])
def procesar_zip():
    zip_file = request.data  # El contenido del archivo .zip se encuentra en request.data
return 'OK', 200 
def AlphaFoldXploR_read(zfile):
    with ZipFile(zfile, 'r') as fz:
        for zip_info in fz.infolist():
            if zip_info.filename[-1] == '/':
                continue
            tab = os.path.basename(zip_info.filename)
            if tab.endswith(".json"):
                zip_info.filename = os.path.basename(zip_info.filename)
                lista1 = fz.extract(zip_info, "archivos_json")

    with ZipFile(zfile, 'r') as fz:
        for zip_info in fz.infolist():
            if zip_info.filename[-1] == '/':
                continue
            tab = os.path.basename(zip_info.filename)
            if tab.endswith(".pdb"):
                zip_info.filename = os.path.basename(zip_info.filename)
                lista2 = fz.extract(zip_info, "archivos_pdb")
