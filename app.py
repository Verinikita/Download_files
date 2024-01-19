from flask import Flask, render_template, request, flash, redirect, url_for
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

ALLOWED_EXTENSIONS = {'zip'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def AlphaFoldXploR_read(folder):
    for name, handle in folder:
        if name.endswith(".json"):
            with handle as file:
                content = file.read_text()
                # Procesa el contenido del archivo JSON según tus necesidades
                print(f'Contenido de {name}: {content}')

        if name.endswith(".pdb"):
            with handle as file:
                content = file.read_text()
                # Procesa el contenido del archivo PDB según tus necesidades
                print(f'Contenido de {name}: {content}')

@app.route('/procesar_zip', methods=['POST'])
def procesar_zip():
    zip_file = request.data  # El contenido del archivo .zip se encuentra en request.data
    # Llama a tu función de procesamiento de archivos .zip aquí
    AlphaFoldXploR_read(zip_file)
    return 'OK', 200

if __name__ == '__main__':
    app.run(debug=True)
