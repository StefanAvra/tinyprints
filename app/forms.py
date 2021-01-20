from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, PasswordField
from wtforms.validators import DataRequired, Length, NumberRange


class TinyForm(FlaskForm):
    tiny_text = TextAreaField('tiny_text', validators=[
                              DataRequired(), Length(max=33*25)])
    title = StringField('title', validators=[DataRequired(), Length(max=32)])
    submit = SubmitField('send it!')


class VoteForm(FlaskForm):
    tiny_text_id = IntegerField('tiny_text_id', validators=[
                                DataRequired(), NumberRange(min=1)])
    submit_upvote = SubmitField('')


class DeleteForm(FlaskForm):
    delete_id = IntegerField('delete_id', validators=[
                             DataRequired(), NumberRange(min=1)])
    delete_pw = PasswordField('delete_pw', validators=[DataRequired()])
    submit_deletion = SubmitField('')
