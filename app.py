from flask import Flask, render_template, request, redirect, url_for,session,make_response

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

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/login-hw', methods=['GET'])
def login_form_hw():
    return render_template('hw_login.html')


@app.route('/my-profile')
def login_success():
    if 'email' and 'password' in session:
        if request.cookies.get('counter') == '1':
            return render_template('success_login.html',login=1,email=session['email'],password=session['password'])
        resp = make_response(render_template('success_login.html',login=0,email=session['email'],password=session['password']))
        resp.set_cookie('counter', '1')
        return resp
    return redirect(url_for('login_error'))

@app.route('/login-error', methods=['GET'])
def login_error():
    return render_template('hw_login.html', login=3)

@app.route('/login-hw', methods=['POST'])
def login_user_hw():
    email = request.form['email']
    password = request.form['password']
    if email == "test@flask.app" and password == "password123":
        session['email'] = request.form['email']
        session['password'] = request.form['password']
        return redirect(url_for('login_success'))
    elif email == "test@flask.app" and password != "password123":
        return render_template('hw_login.html', login=1)
    else:
        return render_template('hw_login.html', login=0)
    

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login_user_hw'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)