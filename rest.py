from flask import Flask, flash, request,redirect,url_for, render_template, send_from_directory
import os
import zipfile
import subprocess
from twitter import get_tweets
from get_video import tweet2video

project_root = os.path.dirname(__file__)
template_path = os.path.join(project_root, './')
app = Flask(__name__, template_folder=template_path, static_folder='static')
app.secret_key = "super secret key"

UPLOAD_FOLDER = '/uploads'
DOWNLOAD_FOLDER = './output'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER

app = Flask(__name__)

@app.route('/')
def first():
    return render_template('main.html')
@app.route('/', methods=['POST'])
def post():
    if request.method == 'POST':
        text = request.form['text']
        if text == '':
            flash('Please type in ONE keyword.')
            return redirect(request.url)
        get_tweets(text,text)
        tweet2video(text,text)
        return redirect(url_for('download', filename=text))
    return render_template('main.html')

@app.route('/downloads/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    file = filename + 'better.mp4'
    if request.method == 'POST':
        return send_from_directory(app.config['DOWNLOAD_FOLDER'], filename=file, as_attachment=True)
    return render_template('file.html', filename=filename)


@app.route('/uploads/<path:filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['DOWNLOAD_FOLDER'], filename, as_attachment=True)

if __name__ == '__main__':

    app.run(host = '0.0.0.0', port = 8240)