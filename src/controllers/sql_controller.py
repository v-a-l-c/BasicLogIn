from flask import Blueprint, request, jsonify
from sqlalchemy import text
from alchemyClasses import db

sql_bp = Blueprint('sql', __name__)

@sql_bp.route('/sql/', methods=["POST", "GET"])
def sql_queries():

    if request.method == "GET":
        return jsonify({"data": []})

    if request.is_json:
        data = request.get_json()
        choice = int(data.get("choice", 0))
    else:
        choice = int(request.form.get("choice", 0))

    if choice == 1:
        query = text("""
            SELECT u.name
            FROM `user` u
            JOIN project_members pm ON u.id_user = pm.id_user
            GROUP BY u.id_user, u.name
            HAVING COUNT(pm.id_project) >= 2
        """)
        result = db.session.execute(query).mappings().all()
        return jsonify({"names": [row["name"] for row in result]})


    elif choice == 2:
        query = text("""
            SELECT DISTINCT u.name
            FROM `user` u
            JOIN project_members pm ON u.id_user = pm.id_user
            JOIN project p ON pm.id_project = p.id_project
            WHERE p.name = 'Tool'
        """)
        result = db.session.execute(query).mappings().all()
        return jsonify({"names": [row["name"] for row in result]})


    elif choice == 3:
        query = text("""
            SELECT p.name, COUNT(pm.id_user) as total
            FROM project p
            LEFT JOIN project_members pm ON p.id_project = pm.id_project
            GROUP BY p.id_project, p.name
        """)
        result = db.session.execute(query).mappings().all()
        return jsonify({"data": [dict(row) for row in result]})

    return jsonify({"error": "Invalid choice"}), 400