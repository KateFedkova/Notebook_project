from flask import render_template, request, flash, redirect, url_for
from flask_login import login_required
from werkzeug.security import generate_password_hash
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
    # if request.method == "POST":
    #     username = request.form["username"]
    #     password = request.form["password"]
    #     user = session.query(Users).where(Users.username == username).first()
    #     if user:
    #         flash("This user already exists")
    #         return redirect(url_for("login"))
    #
    #     new_user = Users(username=username, password=generate_password_hash(password))
    #     session.add(new_user)
    #     session.commit()
    #     session.close()
    #     return redirect("login")
    return render_template("login.html")


@app.route("/add_post")
@login_required
def add_post():
    return render_template("add_post.html")




 # <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
 #            <div class="navbar-nav">
 #                <a class="nav-item nav-link" href="{{ url_for('group_get') }}">Show groups</a>
 #              </div>
 #            {% if current_user.is_authenticated %}
 #                 <div class="navbar-nav">
 #                    <a class="nav-item nav-link" href="{{ url_for('logout') }}">Log out</a>
 #                </div>
 #                {% if current_user.username == "Admin" %}
 #                    <div class="navbar-nav">
 #                        <a class="nav-item nav-link" href="{{ url_for('admin') }}">Profile</a>
 #                    </div>
 #                {% else %}
 #                    <div class="navbar-nav">
 #                        <a class="nav-item nav-link" href="{{ url_for('profile') }}">Profile</a>
 #                    </div>
 #                {% endif %}
 #            {% else %}
 #                <div class="navbar-nav">
 #                    <a class="nav-item nav-link" href="{{ url_for('login') }}">Log in</a>
 #                </div>
 #            {% endif %}