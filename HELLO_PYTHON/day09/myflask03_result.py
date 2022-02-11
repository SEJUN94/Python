from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/para', methods=['POST','GET'])
def para():
    # a = reuest.args.get("a")
    a = request.form['a']
    return 'param'+a


@app.route('/view')
def view():
    a = "999"
    b = ["홍길동","전우치","이순신"]
    c = {'e_id':1,'e_name':1,'sex':1,'age':1}
    d = [
            {'e_id':2,'e_name':2,'sex':2,'age':2},
            {'e_id':3,'e_name':3,'sex':3,'age':3},
        ]
    return render_template('view.html', a=a,b=b,c=c,d=d)

    
if __name__ == '__main__':
    app.run()