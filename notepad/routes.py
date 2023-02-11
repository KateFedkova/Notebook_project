from flask import render_template

from notepad import app


@app.route("/index")
@app.route("/")
def index():
    return render_template("index.html")

 #
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