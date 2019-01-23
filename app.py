# coding=utf-8
from flask import Flask, render_template, request, session, jsonify, make_response, redirect as r
from flask_httpauth import HTTPBasicAuth
from flask_bcrypt import Bcrypt

import config as c
app = Flask(__name__)
app.secret_key = c.secret_key

bcrypt = Bcrypt(app)
auth = HTTPBasicAuth()
@auth.get_password
def get_password(username):
    if username == "username":
        return "password"
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)



@app.route('/main')
@auth.login_required
def main():

    return render_template('main.html')

@app.route('/DoSomething', methods=['POST'])
def predictvalues():

    print(request.form)

    #Do something with the values sent from the HTML template
    value1=request.form['box1']
    value2="just some more test data"


    #Then return it to HTML

    return jsonify({'status': 'OK', 'value1':value1, 'value2': value2});

if __name__ == "__main__":
	#app.run(threaded=True)
	app.run(host='0.0.0.0', port=5000)