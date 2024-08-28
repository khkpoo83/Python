from flask import Flask

app=Flask(__name__)


@app.route('/<username>')
def main(username):
    return '<b> Main '+username+' </b>'

@app.route('/news')
def news():
    return '<b> News </b>'

@app.route('/search')
def search():
    return '<b> Search </b>'

if __name__=='__main__':
    app.run(
        host='127.0.0.1',
        port='8080',
        debug=True
    )