
from flask import Flask, redirect
app = Flask(__name__)

@app.route('/')
def hello():
    resp = redirect("http://localhost:3000")
    resp.set_cookie("abc123", "456")
    return resp
    #return 'Hello duuudddeeee!'


@app.route('/redirect')
def gtfo():
    #return redirect("https://www.google.com")
    resp = redirect("http://localhost:3000")
    resp.set_cookie("abc123", "456")
    return resp


if __name__ == '__main__':
    app.run(debug=True)