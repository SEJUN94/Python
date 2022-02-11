from day11.daomember import DaoMember
from flask.templating import render_template
from flask import Flask
from flask.globals import request
from flask.json import jsonify

app = Flask(__name__)
de = DaoMember()

@app.route('/memberlist')
def memberlist():
    memberlist = de.myselect();
    return render_template('memberlist.html', memberlist=memberlist)

@app.route('/myinsert', methods=['POST'])
def myinsert():
    data = request.get_json()
    m_id = data['m_id']
    m_name = data['m_name']
    tel =data['tel']
    addr = data['addr']
    cnt = de.myinsert(m_name, tel, addr)
    print(data)
    
    result = "fail"
    if cnt == 1:
        result = "success"
    
    return jsonify(result = result)

@app.route('/myupdate', methods=['POST'])
def myupdate():
    data = request.get_json()
    m_id = data['m_id']
    m_name = data['m_name']
    tel =data['tel']
    addr = data['addr']
    cnt = de.myupdate(m_id, m_name, tel, addr)
    print(data)
    
    result = "fail"
    if cnt == 1:
        result = "success"
    
    return jsonify(result = result)

@app.route('/mydelete', methods=['POST'])
def mydelete():
    data = request.get_json()
    m_id = data['m_id']
    cnt = de.mydelete(m_id)
    
    result = "fail"
    if cnt == 1:
        result = "success"
    
    return jsonify(result = result)



if __name__ == '__main__':
    app.run()