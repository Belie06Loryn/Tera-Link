from . import main
from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField,TextAreaField,SelectField
from wtforms.validators import Required
class PostForm(FlaskForm):
    image = SelectField('Pictures',validators=[Required()])
    description = TextAreaField('Description',validators=[Required()])
    submit = SubmitField('Add post')