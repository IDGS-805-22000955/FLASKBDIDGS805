from wtforms import Form
from wtforms import IntegerField, StringField, PasswordField
from wtforms import EmailField
from wtforms import validators
from flask_wtf import FlaskForm

class UserForm2(FlaskForm):
    id=IntegerField('id')
    nombre=StringField("Nombre",[
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=4, max=10, message="Ingrese un nombre valido")
    ])
    apaterno=StringField("Apaterno",[
        validators.DataRequired(message="El campo es requerido")
    ])
    correo=EmailField("Correo", [
        validators.Email(message="Ingresa un correo valido")
    ])

