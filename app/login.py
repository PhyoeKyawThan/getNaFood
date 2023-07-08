from flask import session

def isauth()->bool:
    if "user" in session:
        return True
    else:
        return False