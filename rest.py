from flask import Flask, request, render_template, send_file
import os
import zipfile
import os

app = Flask(__name__)

@app.route('/')
def first():
    return render_template('main.html')
@app.route('/', methods=['POST'])
def post():
    text_id = request.form['id']
    text_k = request.form['keywords']
    args2 = "rm myVideo/*"
    os.system(args2)

    args1 = "python imagestovideo.py "+ str(text_id)  + " "+str(text_k) 
    os.system(args1) 
    zipFolder = zipfile.ZipFile('myVideo.zip','w', zipfile.ZIP_DEFLATED) 
    for root, directs, files in os.walk('myVideo/'):
        for f in files:
            zipFolder.write('myVideo/' + str(f))
    zipFolder.close()

    os.system(args2)    
    return send_file('myVideo.zip', mimetype ='zip', attachment_filename = 'myVideo.zip', as_attachment=True)

if __name__ == '__main__':

    app.run(host = '0.0.0.0', port = 8240)
