from flask import render_template,redirect,url_for, abort
from . import main
from ..models import Post,User
from flask_login import login_required, current_user
from .forms import PostForm
from .. import db

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/add/service', methods=['GET','POST'])

def new_service():
    '''
    View new group route function that returns a page with a form to create a new service
    '''
    form = PostForm()

    if form.validate_on_submit():
        image = form.image.data
        new_service = Post(image=image)
        new_service.save_service()

        description = form.description.data
        new_service = Post(description=description)
        new_service.save_service()

        return redirect(url_for('.new_sevice'))

    
    title = 'New Service'
    return render_template('index.html', Service_form = form,title=title)




