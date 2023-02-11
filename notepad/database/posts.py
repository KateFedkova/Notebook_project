from sqlalchemy import Column, Integer, String, ForeignKey
from notepad.database.db_model import base


class Posts(base):

    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    text = Column(String)

    def __init__(self, user_id, text):
        self.user_id = user_id
        self.text = text
