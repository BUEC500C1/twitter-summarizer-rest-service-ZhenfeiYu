import sys
from flask import Flask, render_template, request, send_file
import os
import zipfile

application = Flask(__name__)

@application.route('/') #creates the flask html route
def root():
    return render_template('main.html')
@application.route('/', methods=['POST']) #creates the flask html route
def post():
    text1 = request.form['username'] #getting usernames
    text2 = request.form['searchword'] 
    args2 = "rm myVideo/*"
    os.system(args2)
    args1 = "python get_video.py "+ str(text1)  + " "+str(text2) 
    os.system(args1) 
    zipFolder = zipfile.ZipFile('myVideo.zip','w', zipfile.ZIP_DEFLATED) #making the zip and sending it to the user!!!
    for root, directs, files in os.walk('/myVideo'):
        for f in files:
            zipFolder.write('/myVideo' + str(f))
    zipFolder.close()
    os.system(args2)    
    return send_file('myVideo.zip', mimetype ='zip', attachment_filename = 'myVideo.zip', as_attachment=True)

if __name__ == '__main__':

    application.run(host = '0.0.0.0', port = 8240)

