from flask.templating import render_template
from flask import Flask

app = Flask(__name__,static_url_path='',static_folder="static")

@app.route('/janggi')
def janggi():
    return render_template('janggi4.html')


@app.route('/tween')
def tween():
    return render_template('tween.html')


if __name__ == '__main__':
    app.run()