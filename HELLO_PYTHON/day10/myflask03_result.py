from flask import Flask, render_template
from day10.daoemp import DaoEmp
from flask.json import jsonify
from flask.globals import request

app = Flask(__name__,static_url_path='',static_folder="static")
de = DaoEmp()

@app.route('/emplist')
def emplist():
    emplist = de.myselect();
    return render_template('emplist.html', emplist=emplist)


@app.route('/myinsert', methods=['POST'])
def myinsert():
    data = request.get_json()
    e_id = data['e_id']
    e_name = data['e_name']
    sex = data['sex']
    age = data['age']
    cnt = de.myinsert(e_name, sex, age)
    print(data)
    
    result = "fail"
    if cnt == 1:
        result = "success"

    return jsonify(result = result)

@app.route('/myupdate', methods=['POST'])
def myupdate():
    data = request.get_json()
    e_id = data['e_id']
    e_name = data['e_name']
    sex = data['sex']
    age = data['age']
    cnt = de.myupdate(e_id, e_name, sex, age)
    print(data)
    
    result = "fail"
    if cnt == 1:
        result = "success"

    return jsonify(result = result)

@app.route('/mydelete', methods=['POST'])
def mydelete():
    data = request.get_json()
    e_id = data['e_id']
    cnt = de.mydelete(e_id)
    print(data)
    
    result = "fail"
    if cnt == 1:
        result = "success"

    return jsonify(result = result)
    
    
if __name__ == '__main__':
    app.run()