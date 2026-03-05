from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import db, Maestros
from forms import MaestroForm

maestros = Blueprint('maestros', __name__)

@maestros.route('/maestros', methods=['GET', 'POST'])
def listar():
    form = MaestroForm()
    if form.validate_on_submit():
        existing_maestro = Maestros.query.get(form.matricula.data)
        if existing_maestro:
            flash('La matrícula ya existe. Por favor, ingrese una matrícula diferente.', 'error')
        else:
            maestro = Maestros(
                matricula=form.matricula.data,
                nombre=form.nombre.data,
                apellidos=form.apellidos.data,
                especialidad=form.especialidad.data,
                email=form.email.data
            )
            db.session.add(maestro)
            db.session.commit()
            flash('Maestro registrado con éxito!', 'success')
        return redirect(url_for('maestros.listar'))
    
    maestros = Maestros.query.all()
    return render_template('maestros/listadoMest.html', maestros=maestros, form=form)

@maestros.route('/maestros/editar/<int:matricula>', methods=['GET', 'POST'])
def editar(matricula):
    maestro = Maestros.query.get_or_404(matricula)
    form = MaestroForm(obj=maestro)
    if form.validate_on_submit():
        form.populate_obj(maestro)
        db.session.commit()
        flash('Maestro actualizado con éxito!', 'success')
        return redirect(url_for('maestros.listar'))
    return render_template('maestros/editarM.html', form=form, maestro=maestro)

@maestros.route('/maestros/eliminar/<int:matricula>')
def eliminar(matricula):
    maestro = Maestros.query.get_or_404(matricula)
    db.session.delete(maestro)
    db.session.commit()
    flash('Maestro eliminado con éxito!', 'success')
    return redirect(url_for('maestros.listar'))
