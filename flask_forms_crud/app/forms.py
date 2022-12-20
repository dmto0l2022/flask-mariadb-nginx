from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, FloatField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from datetime import date

class NoteForm(FlaskForm):
    note = TextAreaField('Note', 
                         validators = [DataRequired(),         
                         Length(min=1, max=800)])
    boolean = BooleanField('Boolean Field',
                           default="checked")
    float = FloatField('Float', 
                       validators = [DataRequired()])
    date = DateField('Date',
                      default=date.today, 
                      validators = [DataRequired()])
    submit = SubmitField('Submit')
