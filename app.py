import os
from auto_mail import *
from flask import Flask, render_template, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, TextAreaField
from wtforms.validators import InputRequired, Email, Length


app = Flask(__name__)

app.config["SECRET_KEY"] ="add your secret key"
