from flask import request
from notepad.database import session, Users, Posts


def add_obj(obj):
    session.add(obj)
    session.commit()
    session.close()


def find_user_by_name(username):
    user = session.query(Users).where(Users.username == username).first()
    return user


def info_form():
    username = request.form["username"]
    password = request.form["password"]
    return username, password


def get_posts(user_id):
    all_posts = session.query(Posts).where(Posts.user_id == user_id)
    all_posts = [i.text for i in all_posts]
    return all_posts
