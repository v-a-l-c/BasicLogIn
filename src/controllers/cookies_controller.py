from flask import Blueprint, session

cookies_bp = Blueprint('cookies', __name__)

@cookies_bp.route('/cookies/', methods=["GET"])
def hello_from_cookies():
    return 'Hello from Cookies!'


@cookies_bp.route('/cookies/greet', methods=["GET"])
def greets_from_cookies():
    if session.get("visited"):
        session["visited"] = False
        return 'Goodbye, come back soon!'
    else:
        session["visited"] = True
        return 'Hi, welcome!'