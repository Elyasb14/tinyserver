from flask import Flask, render_template, request, send_file
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    dirs = [dir for dir in os.listdir('data')]
    for dir in dirs:
        files = sorted([file for file in f'data/{dir}'])
    return render_template('index.html', dirs=dirs, files=files)

@app.route('/select', methods = ['POST', 'GET'])
def select():
    files = request.form.get('files')
    return send_file(f'data/{files}')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
