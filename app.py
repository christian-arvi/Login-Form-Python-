from flask import Flask, render_template, request

app = Flask(__name__)

# @app.route('/')
#def hello():
    #return 'Hello,World!'

#@app.route('/hello/<name>')
#def hello_name(name):
    #return render_template('hello.html', name=name)

#@app.route('/login', methods=['GET'])
#def login_form():
    #return render_template('login_form.html')

#@app.route('/login', methods=['POST'])
#def login_user():
    #email = request.form['email']
    #password = request.form['password']
    #return "Email: %s and Password: %s" % (email, password)

@app.route('/login-hw', methods=['GET'])
def login_form_hw():
    return render_template('hw_login.html')

@app.route('/login-hw', methods=['POST'])
def login_user_hw():
    email = request.form['email']
    password = request.form['password']
    if email == "test@flask.app" and password == "password123":
        return render_template('success_login.html', email=email,login=2)
    elif email == "test@flask.app" and password != "password123":
        return render_template('hw_login.html', login=1)
    else:
        return render_template('hw_login.html', login=0)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)