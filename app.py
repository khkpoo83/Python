from flask import Flask,jsonify,request,render_template

app=Flask(__name__, static_url_path='/static')


@app.route('/')
def main():
    return render_template('/login.html')

@app.route('/<int:repeat>')
def arg(repeat):
    return render_template('/login.html',rpt=repeat)

@app.route('/login')
def login():
    id=request.args.get('id')
    pwd=request.args.get('pwd')
    if id=='khkpoo@gmail.com' and pwd=='1234':
        rst={"Auth":"Successed"}
        return jsonify(rst)
    else:
        rst={"Auth":"Failed"}
        return jsonify(rst)
    
@app.route('/search')
def search():
    return '<b> Search </b>'

if __name__=='__main__':
    app.run(
        host='127.0.0.1',
        port='8080',
        debug=True
    )