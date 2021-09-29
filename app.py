from __future__ import division, print_function
import os


# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer

# Define a flask app
app = Flask(__name__)

print('Check http://127.0.0.1:5000/')


def model_predict(img_path):
    text = ocr_anpr.predict(img_path)
    return text


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        file_path = file_path.replace('\\', '/')
        f.save(file_path)

        # Make prediction
        result = model_predict(file_path)
        return result
    return None


if __name__ == '__main__':
    app.run(debug=True)

