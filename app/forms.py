from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length

class TinyForm(FlaskForm):
    tiny_text = TextAreaField('tiny_text', validators=[DataRequired(), Length(max=33*25)])
    title = StringField('title', validators=[DataRequired(), Length(max=32)])
    submit = SubmitField('send it!')