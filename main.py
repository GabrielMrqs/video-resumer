from flask import Flask, jsonify, render_template
from resumer import Resumer

resumer = Resumer()
app = Flask(__name__)


@app.route('/api/resume/<string:video_url>', methods=['GET'])
def hello_world(video_url):
    return resumer.resume_video(video_url)


if __name__ == '__main__':
    app.run()
