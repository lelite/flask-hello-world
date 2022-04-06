from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return f'<a href="dtxuexi://appclient/page/study_feeds">学习强国</a>'
