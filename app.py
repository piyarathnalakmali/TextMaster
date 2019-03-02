import os
from flask import Flask , render_template , request
from Video import Video
from VideoHandler import VideoHandler

app=Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/documentation')
def documentation():
    return render_template('documentation.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/upload' , methods = ["POST"])
def upload():
    target=os.path.join(APP_ROOT, 'videos/')
    print (target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        print (file)
        filename=file.filename
        destination = "/".join([target,filename])
        print(destination)
        file.save(destination)
        video = Video(filename,destination)
        videoHandler = VideoHandler()
        #print(videoHandler.splitVideo2(video))
        #videoHandler.playVideo(video)
    return render_template('complete.html')


if __name__ == '__main__':
    app.run(debug=True)
