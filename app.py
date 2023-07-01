from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    files = os.listdir('data')
    return render_template('index.html', files=files)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
