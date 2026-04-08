from flask import Flask, render_template, session, redirect
from sqlalchemy import URL, text
from alchemyClasses import db

def create_blueprint():
    pass


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = URL.create(
        drivername="mysql+pymysql",
        username="ing_soft_user",
        password="P4ssw0rd@",
        host="localhost",
        port=3306,
        database="practica4"
    )
    app.config.from_mapping(SECRET_KEY="dev")
    db.init_app(app)
    
    @app.route('/login', methods=["GET"])
    def login_view():
        return render_template('index.html')

    @app.route('/user', methods=["GET"])
    def user_page():
        if 'user' not in session:
            return redirect('/')

        return render_template(
            'user.html',
            user_name=session['user'],
            rol=session.get('rol', 'usuario')
    )

    from controllers.cookies_controller import cookies_bp
    from controllers.sql_controller import sql_bp

    app.register_blueprint(cookies_bp)
    app.register_blueprint(sql_bp)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host="127.0.0.1", port=5000)
