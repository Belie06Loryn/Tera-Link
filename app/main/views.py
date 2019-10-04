from flask import render_template,redirect,url_for,abort
from . import main
from flask_login import login_required, current_user
from .. models import User,Post
from .. import db,photos
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
    posite = Post.query.all()
    if form.validate_on_submit():
        filename = photos.save(form.image.data)
        path=f'photos/{filename}'
        description = form.description.data
        service = Post(image=filename, description=description)
        service.save_service()
        return redirect(url_for('main.new_service'))
    title = 'New Service'
    return render_template('new_service.html', form = form,title=title, posite = posite)

@main.route('/display/new_service/<int:id>')
def service(id):
    post = Post.query.get(id)

    return render_template('post_chef.html', post =post)    

@main.route('/image_service/')
def profile():
    posite = Post.query.all()

    if posite is None:
        abort(404)
        

    return render_template("post_chef.html", posite = posite)

