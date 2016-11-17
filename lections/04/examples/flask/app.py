# -*- coding: utf-8 -*-

from flask import Flask, render_template, send_from_directory, request, abort, session, redirect

app = Flask("Simple app")

template_dir = 'templates'

@app.route('/', methods=['GET'])
def index():
    username = session.get('username', None)
    if username is None:
        return redirect("/login")
    return render_template('index.html', username=username)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form.get('username', None)
        password = request.form.get('password', None)
        print username, password, username == password
        if username is None or password is None or username != password:
            return render_template('login.html', error=u"Некорректные данные для входа")
        session['username'] = username
        session.modified = True
        return redirect("/")
    else:
        abort(501)

if __name__ == "__main__":
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    app.run(port=8001)
