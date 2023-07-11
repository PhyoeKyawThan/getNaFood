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
    if (session["user"]["username"], session["user"]["password"]) in curr:
        user.close()
        return True
    else:
        user.close()
        return False