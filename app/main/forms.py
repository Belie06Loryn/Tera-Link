from . import main
from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField,TextAreaField,SelectField
from wtforms.validators import Required
from ..models import Posts

class PostUploadForm(FlaskForm):
    image = SelectField('Pictures',validators=[Required()])
    posts = TextAreaField('Posts',validators=[Required()])
    submit = SubmitField('Add post')
