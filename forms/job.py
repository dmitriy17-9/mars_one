from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, BooleanField, IntegerField, DateTimeField
from wtforms.validators import DataRequired


class JobsForm(FlaskForm):
    team_leader = IntegerField("Team Leader id", validators=[DataRequired()])
    job = TextAreaField("Job title", validators=[DataRequired()])
    work_size = IntegerField("Work Size")
    collaborators = StringField("Collaborators")
    start_date = DateTimeField("Start date")
    end_date = DateTimeField("End date")
    is_finished = BooleanField("Is job finished?")

    submit = SubmitField("Submit")
