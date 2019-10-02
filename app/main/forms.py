from . import main
from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField,TextAreaField,SelectField
from wtforms.validators import Required
from ..models import Post

class PostForm(FlaskForm):
    image = SelectField('Pictures',validators=[Required()])
    description = TextAreaField('Posts',validators=[Required()])
    submit = SubmitField('Add post')
