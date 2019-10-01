from . import main
from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField,TextAreaField,SelectField
from wtforms.validators import DataRequired
from ..models import Posts

class PostForm(FlaskForm):
    image = SelectField('Pictures',validators=[Required()])
    description = TextAreaField('Posts',validators=[Required()])
    submit = SubmitField('Add post')
