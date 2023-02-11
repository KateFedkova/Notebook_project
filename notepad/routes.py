from flask import render_template, request, flash, redirect, url_for
from flask_login import login_required, logout_user, login_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from notepad import app, login_manager
from notepad.database import session, Posts, Users


@app.route("/index")
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = session.query(Users).where(Users.username == username).first()
        if user:
            flash("This user already exists")
            #return redirect(url_for("login"))

        new_user = Users(username=username, password=generate_password_hash(password))
        session.add(new_user)
        session.commit()
        session.close()
        return redirect("login")
    return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        remember = True if request.form.get("remember") else False

        user = session.query(Users).where(Users.username == username).first()

        if not user or not check_password_hash(user.password, password):
            flash("Check if you enter data correctly or sign up")
            return redirect(url_for("login"))
        login_user(user, remember=remember)
        return redirect(url_for("index"))

    return render_template("login.html")


@app.route("/add_note", methods=["GET", "POST"])
@login_required
def add_note():
    if request.method == "POST":
        note = request.form["note"]
        user_id = current_user.id

        new_note = Posts(user_id=user_id, text=note)
        session.add(new_note)
        session.commit()
        session.close()

    return render_template("add_note.html")


@app.route("/all_notes")
def all_notes():
    id = current_user.id
    all_posts = session.query(Posts).where(Posts.user_id == id)
    all_posts = [i.text for i in all_posts]

    return render_template("all_notes.html", all_posts=all_posts)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))


@login_manager.user_loader
def load_user(id):
    return session.query(Users).get(int(id))
