from flask import Flask, redirect, url_for, request,jsonify
app = Flask(__name__)



@app.route('/login/<name>')
def success(name):
   return 'welcome %s' % name


@app.route('/login', methods = ['POST', 'GET'])
def login():
    login_id = "keroro@hotgirl.com"
    password = "1234"

    data = { "id" : login_id , "password" : password }

    return jsonify(data)

@app.route('/')
def index():
    return "test1"



if __name__ == '__main__':
   app.run(debug = True)
