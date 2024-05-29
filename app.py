from flask import Flask, render_template, request

from load_model import predict
from gcp_bucket import upload_file

import sqlite3 as sqlite

from io import BytesIO

app = Flask(__name__)

def get_db_connection():
    conn = sqlite.connect('./db/database.db')
    conn.row_factory = sqlite.Row
    return conn

@app.errorhandler(404)
def not_found(error):
    return 'Ruta no encontrada'
     
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/registrar-archivo', methods=['GET', 'POST'])
def registarArchivo():
        error = None
        if request.method == 'POST':

            file     = request.files['archivo']
            filename = file.filename
            if filename.endswith(".pdf"):
                with BytesIO() as buffer:
                    file.save(buffer)
                    buffer.seek(0)
                    result = predict(buffer)
                    url = upload_file(buffer)

                data = { 'filename': filename, 'tag': result[0], 'url': url}
                conn = get_db_connection()
                conn.execute('INSERT INTO results (filename, tag, url) VALUES (?, ?, ?)', tuple(data.values()))
                conn.commit()
                conn.close()
                return render_template('predict.html', **data)
            else:
                error = 'No es un archivo PDF'
        return render_template('index.html', error = error)
    
@app.route('/all', methods=['GET'])
def all_results():
    conn = get_db_connection()
    results = conn.execute('SELECT * FROM results').fetchall()
    conn.close()
    return render_template('results.html', results = results)

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0', port=8000)