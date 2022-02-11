from flask import Flask, redirect, url_for, request, render_template
import webbrowser

app = Flask(__name__)

# webbrowser.open_new_tab('post.html')

@app.route('/')
def index():
    return render_template('post.html')

@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name


@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        user = request.form['myName']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('myName')
        return redirect(url_for('success', name=user))

    
if __name__ == '__main__':
    app.run()