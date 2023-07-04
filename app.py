from flask import Flask, render_template, request, send_file
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    files = sorted(os.listdir('data'))
    return render_template('index.html', files=files)

@app.route('/select', methods = ['POST', 'GET'])
def select():
    files = request.form.get('files')
    return send_file(f'data/{files}')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
