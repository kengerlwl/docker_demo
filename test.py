from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
# 解决跨域请求问题
CORS(app, supports_credentials=True)

@app.route('/')
def index():
    return '<h1>Hello World</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10001, debug=True)
