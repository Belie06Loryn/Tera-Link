from . import db
from datetime import datetime

class Post(db.Model):
    '''
    This class will contain database schema for posts
    '''
    __tablename__ = 'posts'
    id = db.Column(db.Integer,primary_key=True)
    image = db.Column(db.String())
    description = db.Column(db.String())

    