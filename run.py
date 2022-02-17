from flask import Flask, Response
from video import VideoCamera

app = Flask(__name__)


@app.route('/')
def index():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


def gen(camera):
    while True:
        frame = camera.get_frame_with_box(0, 0, 100, 100)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
