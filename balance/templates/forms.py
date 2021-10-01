from flask_wtf import FlaskForm                 #Libreria en flask-wtf.readthedocs.io y wtforms.readthedocs.io
from wtforms import DateField, StringField
from wtforms.fields.core import FloatField, RadioField
from wtforms.fields.simple import SubmitField
from wtforms.validators import DataRequired, Length, NumberRange, ValidationError
from balance.validators import Validators


class MovimientoFormulario(FlaskForm):
    fecha = DateField("Fecha", validators=[DataRequired(message="Debe informar la fecha")])
    concepto = StringField("Concepto", validators=[DataRequired(message="Debe informar el concepto"), Length(min=2)])
    cantidad = FloatField("Cantidad", validators=[DataRequired(message="Debe informar el monto del movimiento"), NumberRange(message="debe informar un importe positivo", min=0.01)])
    ingreso_gasto = RadioField(validators=[DataRequired(message="Debe de informar el tipo de movimiento")], choices=[('G', 'Gasto'), ('I', 'Ingreso')])
    submit = SubmitField('Aceptar')

"""
    def validate_fecha(self, campo): #No se sería así
        Validators.validate_fecha(campo)
"""