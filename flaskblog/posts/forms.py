from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length


class PostForm(FlaskForm):
    title=StringField('Title of the content', validators=[DataRequired(), Length(max=60)])
    content=TextAreaField("Content", validators=[DataRequired()])
    submit=SubmitField("Post")
