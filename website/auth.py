from flask import Blueprint , render_template ,request ,session ,redirect ,url_for ,flash
from . import db
from .models import Users
auth = Blueprint("auth",__name__)


@auth.route("/login",methods=["POST","GET"])
def login():


    if request.method=="POST":
        
        email=request.form["email"]
        password=request.form["password"]

        user=Users.query.filter_by(email=email).first()
        if user :
            if user.password == password:
                session["email"]=email
                session["password"]=password

                flash("Loged in successfully!","success")
                return redirect(url_for("view.home"))
            else:
                flash("Wrong password","danger")
        else:
            flash("Email does not exist!","danger")
    else:
        if "email" in session:
            flash("Already loged in !","success")
            return redirect(url_for("view.home"))

    return render_template("login.html")

@auth.route("/logout")
def logout():
    session.pop("email",None)
    session.pop("password",None)
    flash("Loged out successfully!","success")
    return redirect(url_for("auth.login"))

@auth.route("/sign_up",methods=["POST","GET"])
def sign_up():
    
    if request.method=="POST":
        
        firstname=request.form["firstname"]
        lastname=request.form["lastname"]
        email=request.form["email"]
        password1=request.form["password1"]
        password2=request.form["password2"]

        user = Users.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='danger')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='danger')
        elif len(firstname) < 2:
            flash('First name must be greater than 1 character.', category='danger')
        elif len(lastname) < 2:
            flash('Last name must be greater than 1 character.', category='danger')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='danger')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='danger')
        else:
            new_user = Users(email=email, firstname=firstname,lastname=lastname, password=password1)
            db.session.add(new_user)
            db.session.commit()
            session["email"]=email
            flash('Account created!', category='success')
            return redirect(url_for('view.home'))
    
    return render_template("sign_up.html")

