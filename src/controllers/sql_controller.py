from flask import Blueprint, request, jsonify, session
from sqlalchemy import text
from alchemyClasses import db

sql_bp = Blueprint('sql', __name__)

@sql_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    username = data.get('email')
    password = data.get('password')

    query = text("SELECT * FROM Usuario WHERE nombre_usuario = :user AND contrasena = :pass")

    result = db.session.execute(query, {
        "user": username,
        "pass": password
    }).fetchone()

    if result:
        session['user'] = username
        return jsonify({"success": True})
    else:
        return jsonify({"success": False, "message": "Credenciales incorrectas"}), 401