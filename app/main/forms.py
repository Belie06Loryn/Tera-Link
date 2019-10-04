from . import main
from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField,TextAreaField,SelectField
from wtforms.validators import Required
from flask_wtf.file import FileField,FileRequired
from werkzeug.utils import secure_filename
class PostForm(FlaskForm):
    image = FileField('Pictures',validators=[Required()])
    description = StringField('Description',validators=[Required()])
    submit = SubmitField('Add post')