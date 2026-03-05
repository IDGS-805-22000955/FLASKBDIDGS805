from wtforms import Form, TextAreaField
from wtforms import IntegerField, StringField, PasswordField, SelectField
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
    email = EmailField("Correo", [
        validators.Email(message="Ingresa un correo valido")
    ])

class MaestroForm(FlaskForm):
    matricula=IntegerField('matricula')
    nombre=StringField("Nombre",[
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=4, max=50, message="Ingrese un nombre valido")
    ])
    apellidos=StringField("Apellidos",[
        validators.DataRequired(message="El campo es requerido")
    ])
    especialidad=StringField("Especialidad",[
        validators.DataRequired(message="El campo es requerido")
    ])
    email=EmailField("Correo", [
        validators.Email(message="Ingresa un correo valido")
    ])

class CursoForm(FlaskForm):
    nombre = StringField("Nombre del Curso", [validators.DataRequired()])
    descripcion = TextAreaField("Descripción")
    maestro_id = SelectField("Maestro Asignado", coerce=int, validators=[validators.DataRequired()])

class InscripcionForm(FlaskForm):
    alumno_id = SelectField("Seleccionar Alumno", coerce=int, validators=[validators.DataRequired()])