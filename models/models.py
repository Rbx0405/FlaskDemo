from . import db 
import datetime

#this is a table below
class Users(db.Model):
    _tablename_ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
    agent_name = db.Column(db.String(40), nullable=True)
    agent_phone = db.Column(db.BigInteger, nullable=True)
    date_added = db.Column(db.DateTime, default=datetime.datetime.now(), nullable=True)

    def _init_(self, email, password, agent_name=None, agent_phone=None, date_added=None):
        self.email = email
        self.password = password
        self.agent_name = agent_name
        self.agent_phone = agent_phone
        self.date_added = date_added