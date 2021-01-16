from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class TinyForm(FlaskForm):
    tiny_text = TextAreaField('tiny_text', validators=[DataRequired()])
    title = StringField('title', validators=[DataRequired()])
    submit = SubmitField('send it!')