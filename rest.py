import sys
from flask import Flask, render_template, request, send_file
import os
import zipfile

application = Flask(__name__)

@application.route('/') 
def root():
    return render_template('main.html')
@application.route('/', methods=['POST']) 
def post():
    text1 = request.form['username'] 
    # text2 = request.form['searchword'] 
    args = "python3 queue_work.py"
    os.system(args)
    zipFolder = zipfile.ZipFile('myVideo.zip','w', zipfile.ZIP_DEFLATED)
    for root, directs, files in os.walk('User/yzf/hw5/myVideo/'):
        for f in files:
            print(f)
            zipFolder.write('User/yzf/hw5/myVideo/' + str(f))
    zipFolder.close()
   
    return send_file('myVideo.zip', mimetype ='zip', attachment_filename = 'myVideo.zip', as_attachment=True)

if __name__ == '__main__':

    application.run(host = '0.0.0.0', port = 8240)



