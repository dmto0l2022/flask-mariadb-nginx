"""Form object declaration."""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class EnterNewPlotForm(FlaskForm):
    """New Plot form."""
    name = StringField(
        'name',
        [DataRequired()]
    )
    submit = SubmitField('Submit')
