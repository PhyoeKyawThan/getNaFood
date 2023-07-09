from flask import session, redirect, url_for

def isauth()->bool:
    if "user" in session:
        return True
    else:
        return False