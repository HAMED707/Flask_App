from flask import Blueprint,render_template, session ,request ,redirect ,url_for
from .models import Users 
from . import db

view=Blueprint("view",__name__)

@view.route("/home")
def home():
    email=session.get("email")
    password=session.get("password")

    users=Users.query.all()
    return render_template("home.html",password=password,email=email,users=users)

@view.route("/delete",methods=["POST"])
def delete_user():
    
        id=request.form.get("id")

        if id:
            user=Users.query.filter_by(id=id).first()
            if user:
                db.session.delete(user)
                db.session.commit()

        return redirect(url_for("view.home"))


