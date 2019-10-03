from flask import render_template,redirect,url_for,abort
from . import main
from flask_login import login_required, current_user
from .. models import User,Post
from .. import db
from .forms import PostForm

@main.route("/")
def index():

    return render_template('index.html')


@main.route('/add/new_service', methods=['GET','POST'])
@login_required
def new_service():
    '''
    View new group route function that returns a page with a form to create a new service
    '''
    form = PostForm()
    if form.validate_on_submit():
        image = form.image.data
        description = form.description.data
        service = Post(image=image, description=description)
        service.save_service()
        return redirect(url_for('.index'))
    title = 'New Service'
    return render_template('new_service.html', Service_form = form,title=title)