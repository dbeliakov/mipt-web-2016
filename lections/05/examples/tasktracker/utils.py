import json
from flask import redirect, session
from functools import wraps

with open('users.json') as users_file:
    g_users = json.load(users_file)

class User(object):
    def __init__(self, login):
        if login is not None and login in g_users:
            self.login = login
            self.anonymous = False
            self.password = g_users[login]["password"]
        else:
            self.anonymous = True

    def is_anonymous(self):
        return self.anonymous

    def is_authorized(self):
        return not self.anonymous


def authorize(login, password):
    user = User(login)
    if not user.is_authorized():
        return user
    if user.password == password:
        return user
    return User(None)

def get_user(login):
    return User(login)

def authorized(fn):
    @wraps(fn)
    def wrapped(*args, **kwargs):
        user = get_user(session.get("user_login", None))
        if user.is_authorized():
            return fn(*args, **kwargs)
        else:
            return redirect('/login')
    return wrapped

def not_authorized(fn):
    @wraps(fn)
    def wrapped():
        user = get_user(session.get("user_login", ""))
        if not user.is_authorized():
            return fn()
        else:
            return redirect('/')
    return wrapped
