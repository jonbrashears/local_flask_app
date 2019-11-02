from flask import Flask, flash, redirect, render_template, request, session, abort
from flask_restful import Api, Resource, reqparse
import os

app = Flask(__name__)
api = Api(app)

IMAGE_FOLDER = os.path.join('static', 'kitties')

app.config['UPLOAD_FOLDER'] = IMAGE_FOLDER

@app.route("/")
def index():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'Louise.jpg')
    return render_template("index.html", user_image = full_filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0')

