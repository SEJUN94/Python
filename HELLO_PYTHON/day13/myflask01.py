from flask import Flask
from flask.globals import request
from flask.templating import render_template
from daostock import DaoStock1




app = Flask(__name__,static_url_path='',static_folder="static")


@app.route('/')
def stock():
    a=[]
    b=[]
    ds = DaoStock1()
    mylist = ds.mys_names()
    for n in mylist:
        s_name = n['s_name']
        prices = ds.myprices(s_name)
        print(s_name,prices)
        a.append(s_name)
        b.append(prices)
    
    print(a)
    print(b)
    return render_template('line-charts.html',a=a,b=b)  



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80,debug=True)
    
    
    
    