from flask import Flask ,render_template
from flask_sqlalchemy import SQLAlchemy


db=SQLAlchemy()

def creat_app():

    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    app.secret_key="HAMED777"

    from .auth import auth
    from .view import view

    app.register_blueprint(auth,url_prefix="/")
    app.register_blueprint(view,url_prefix="/")


    from .models import Users
    @app.route("/")
    def test():
        users=Users.query.all()
        return render_template("test.html",users=users)
    
    


    return app
    