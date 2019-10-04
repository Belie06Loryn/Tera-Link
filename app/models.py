from . import db, login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#User class
class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))
    post = db.relationship('Post', backref = 'users', lazy = 'dynamic')

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)

    def __repr__(self):
        return f'User {self.username}'

class Post(db.Model):
    '''
    This class will contain database schema for posts
    '''
    __tablename__ = 'posts'
    id = db.Column(db.Integer,primary_key=True)
    image = db.Column(db.String())
    description = db.Column(db.String())
    user = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    def save_service(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_posts(cls):
        posts = Post.query.all()
        return posts
