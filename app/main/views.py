from flask import render_template,redirect,url_for,abort
from . import main
from flask_login import login_required, current_user
from .. models import User
from app import db

@main.route("/")
def index():
    title = 'Hello'
    
    return render_template("index.html", title = title)

