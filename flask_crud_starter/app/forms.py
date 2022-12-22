"""Form object declaration."""
from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField
from wtforms.validators import DataRequired, Length

class EnterNewPlot(FlaskForm):
    """New Plot form."""
    name = StringField(
        'name',
        [DataRequired()]
    )
    submit = SubmitField('Submit')
