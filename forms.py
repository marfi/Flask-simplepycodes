from app import *


class MessageForm(FlaskForm):
    name = StringField("name", validators=[InputRequired(), Length(max=25)])
    email = StringField("email", validators=[InputRequired(), Email(message="Enter your email")])
    message =  TextAreaField()
    submit = SubmitField("Send")
