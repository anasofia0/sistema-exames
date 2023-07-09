from flask import Flask, render_template, jsonify
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_swagger import swagger

import os


db: SQLAlchemy = SQLAlchemy()
bootstrap = Bootstrap()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)

    basedir = os.path.abspath(os.path.dirname(__file__))
    db_path = os.path.join(basedir, '..', 'saas.db')
    login_manager.init_app(app)
    app.config["SECRET_KEY"] = "secret"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"

    # init
    db.init_app(app)
    with app.app_context():
        from .models.user import User
        from .models.exame import Exame
        db.create_all()
    bootstrap.init_app(app)

    @app.context_processor
    def inject_bootstrap():
        return {'bootstrap': bootstrap}

    from .auth.auth import auth_bp
    app.register_blueprint(auth_bp)
    
    from .controllers import blueprints
    for bp in blueprints():
        app.register_blueprint(bp)

    return app


app = create_app()

@app.route("/")
def index():
    return render_template("index.html")

@login_manager.user_loader
def load_user(user_id):
    from .models.user import User
    return User.query.get(user_id)



