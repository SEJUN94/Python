from flask import Flask
from flask.globals import request
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/para')
def para():
    a = request.args.get("a")
    return 'param'+a
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)