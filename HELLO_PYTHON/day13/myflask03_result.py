from flask import Flask
from flask.templating import render_template
from daostock import DaoStock1

app = Flask(__name__,static_url_path='',static_folder="static")
ds = DaoStock1()

@app.route('/stock')
def stock():
    a=[]
    b=[]
    mylist = ds.mys_names()
    for n in mylist:
        s_name = n['s_name']
        prices = ds.myprices(s_name)
        print(s_name,prices)
        a.append(s_name)
        b.append(prices)
        
    return render_template('line-charts.html',a=a,b=b)

@app.route('/jqplot')
def jqplot():
    return render_template('jqplot.html')
                
    
if __name__ == '__main__':
    app.run(debug=True)