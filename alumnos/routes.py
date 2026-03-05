from flask import render_template, request, redirect, url_for, flash
from forms import UserForm2
from models import db, Alumnos
from . import alumnos


@alumnos.route('/', methods=['GET', 'POST'])
def listar():
    form = UserForm2()
    if form.validate_on_submit():
        alumno = Alumnos(
            nombre=form.nombre.data,
            apaterno=form.apaterno.data,
            email=form.email.data
        )
        db.session.add(alumno)
        db.session.commit()
        flash('Alumno registrado con éxito!', 'success')
        return redirect(url_for('alumnos.listar'))

    alumnos = Alumnos.query.all()
    return render_template('alumnos/index.html', alumnos=alumnos, form=form)


@alumnos.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    alumno = Alumnos.query.get_or_404(id)
    form = UserForm2(obj=alumno)
    if form.validate_on_submit():
        form.populate_obj(alumno)
        db.session.commit()
        flash('Alumno actualizado con éxito!', 'success')
        return redirect(url_for('alumnos.listar'))
    return render_template('alumnos/editar.html', form=form, alumno=alumno)


@alumnos.route('/eliminar/<int:id>')
def eliminar(id):
    alumno = Alumnos.query.get_or_404(id)
    db.session.delete(alumno)
    db.session.commit()
    flash('Alumno eliminado con éxito!', 'success')
    return redirect(url_for('alumnos.listar'))