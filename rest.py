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
    text2 = request.form['searchword'] 
    args = "python3 get_video.py"+" "+str(text1)+" "+str(text2)
    os.system(args)
    # zipFolder = zipfile.ZipFile('myVideo.zip','w', zipfile.ZIP_DEFLATED)
    # for root, directs, files in os.walk(text1):
    #     for f in files:
    #         print(f)
    return send_file(str(text1)+'/'+str(text1)+'.avi', attachment_filename = str(text1)+'.avi', as_attachment=True)
            # zipFolder.write('myVideo/' + str(f))
    # zipFolder.close()
    

if __name__ == '__main__':

    application.run(host = '0.0.0.0', port = 5000)

