from flask import session, redirect, url_for
from .models import User

def isauth()->bool:
    if "user" in session and user_exist():
        return True
    else:
        return False
    
def user_exist():
    user = User()
    curr = user.cursor.execute(f"select username, password from user where username='{session['user']['username']}'")
    curr = curr.fetchone()
    user.close()
    username = session["user"]["username"]
    password = session["user"]["password"]
    if (username, password) == curr:
        return True
    else:
        return False