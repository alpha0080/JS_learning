import os
import json

from flask import Flask, render_template, request
from flask_dropzone import Dropzone

#basedir = os.path.abspath(os.path.dirname(__file__))
uploadFileList = []
app = Flask(__name__)

app.config.update(
    UPLOADED_PATH= 'uploads/',
	DROPZONE_ALLOWED_FILE_CUSTOM  = True,
	DROPZONE_ALLOWED_FILE_TYPE='image/*, .json , .png, .jpg , .atlas' ,
    DROPZONE_MAX_FILE_SIZE=2048,
    DROPZONE_MAX_FILES=99999,
)
 #   DROPZONE_REDIRECT_VIEW='completed'

dropzone = Dropzone(app)


@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        f = request.files.get('file')
        f.save(os.path.join(app.config['UPLOADED_PATH'], f.filename))
      #  print f.filename
        uploadFileList.append(f.filename)
    return render_template('upload.html')



@app.route('/completed')
def completed():
   # print uploadFileList
    eventFiles = uploadFileList
    uploadFileList = []
    return '<h1>The Redirected Page</h1><p>%sUpload completed.</p>'%eventFiles


@app.route('/hello/')
def hello():
    return render_template('hello.html')

@app.route('/pixiSpine')
def pixiSpine():
    if len(uploadFileList) == 0:
        pass
    else:
        for i in uploadFileList:
            if i.split(".")[1] == "json":
                spineJson = i
            elif i.split(".")[1] == "png":
                spineSpriteImage = i
            elif i.split(".")[1] == "atlas":
                spineSpriteAtlas = i
           # data = "test test test"
        effectName = getEffectName(spineJson)

        return render_template('pixiSpine.html',uploadFileList = uploadFileList, effectName = effectName,spineJson=spineJson)


        
def getEffectName(jsonFile):
    path = 'c:/webServer/uploads/'
    fileName = path + jsonFile
    #print fileName

    with open(fileName) as data_file:    
        data = json.load(data_file)
   # print len(data.keys())
    return data["animations"].keys()[0]

if __name__ == '__main__':
    app.run(debug=True)