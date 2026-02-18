from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
import  forms

from models import db, Alumnos
app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db.init_app(app)
csrf = CSRFProtect(app)

@app.route("/", methods=["GET", "POST"])
@app.route("/index")
def index():
	create_form = forms.UserForm2(request.form)
	alumnos = Alumnos.query.all()
	return render_template("index.html", alumnos=alumnos)

@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html"),404

@app.route("/Alumnos", methods=["GET", "POST"])
def alumnos():
	create_form = forms.UserForm2(request.form)
	if request.method == 'POST' and create_form.validate():
			alum = Alumnos(nombre=create_form.nombre.data,
						   apaterno=create_form.apaterno.data,
						   correo=create_form.correo.data)
			db.session.add(alum)
			db.session.commit()
			flash('¡Alumno registrado con éxito!', 'success')
			return redirect(url_for('alumnos'))

	alumnos = Alumnos.query.all()
	return render_template("Alumnos.html", form=create_form, alumnos=alumnos)

@app.route('/modificar/<int:id>', methods=['GET', 'POST'])
def modificar_alumno(id):
    alum = Alumnos.query.get_or_404(id)
    edit_form = forms.UserForm2(request.form, obj=alum)
    if request.method == 'POST' and edit_form.validate():
        edit_form.populate_obj(alum)
        db.session.commit()
        flash('¡Alumno actualizado con éxito!', 'success')
        return redirect(url_for('alumnos'))
    return render_template('modificar_alumno.html', form=edit_form, alumno=alum)

@app.route('/eliminar/<int:id>')
def eliminar_alumno(id):
    alum = Alumnos.query.get_or_404(id)
    db.session.delete(alum)
    db.session.commit()
    flash('¡Alumno eliminado con éxito!', 'success')
    return redirect(url_for('alumnos'))

if __name__ == '__main__':
	with app.app_context():
		db.create_all()
	app.run()
