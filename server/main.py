from flask import Flask, jsonify, render_template
from flask_cors import CORS, cross_origin
from resumer import Resumer

resumer = Resumer()
app = Flask(__name__)
CORS(app)

@app.route('/api/resume/<string:video_url>', methods=['GET'])
@cross_origin()
def hello_world(video_url):
    resume = resumer.resume_video(video_url)
    return jsonify(resume)


if __name__ == '__main__':
    app.run()
