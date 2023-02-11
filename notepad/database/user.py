from sqlalchemy import Column, Integer, String
from notepad.database.db_model import base
from flask_login import UserMixin


class Users(UserMixin, base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)

    def __init__(self, username, password):
        self.username = username
        self.password = password
