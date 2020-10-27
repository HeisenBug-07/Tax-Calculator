from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, SelectField, StringField
from wtforms.validators import DataRequired


class UserIncomeForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    job = SelectField('Select job', choices=[('1', 'Private'), ('2', 'Government')])
    age = IntegerField('Age', validators=[DataRequired()])
    city = SelectField('Select city', choices=[('1', 'Metropolitan'), ('2', 'Non metropolitan')])
    basic = IntegerField('Basic Salary', validators=[DataRequired()])
    da = IntegerField('DA')
    hra = IntegerField('HRA')
    conveyance = IntegerField('Conveyance')
    lta = IntegerField('LTA')
    others = IntegerField('Other income')
    rent = IntegerField('Rent Paid')
    p_tax = IntegerField('Professional Tax')
    ac = IntegerField('80C')
    ad = IntegerField('80D')
    add = IntegerField('80DD')
    addb = IntegerField('80DDB')
    ae = IntegerField('80E')
    ag = IntegerField('80G')
    agg = IntegerField('80GG')
    agga = IntegerField('80GGA')
    aggc = IntegerField('80GGC')
    atta = IntegerField('80TTA')
    au = IntegerField('80U')
    submit = SubmitField('Calculate IncomeTax')


class Theme(FlaskForm):
    theme = SelectField('Theme', choices=[('1', 'default'), ('2', 'Flare'), ('3', 'Ohhapiness'), ('4', 'Starfall')])
    submit = SubmitField('Theme')
