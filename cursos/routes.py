from flask import render_template, request, redirect, url_for, flash
from models import db, Curso, Maestros, Alumnos
from forms import CursoForm, InscripcionForm
from . import cursos


@cursos.route('/', methods=['GET', 'POST'])
def index():
    form = CursoForm()
    form.maestro_id.choices = [(m.matricula, f"{m.nombre} {m.apellidos}") for m in Maestros.query.all()]

    if form.validate_on_submit():
        curso = Curso(
            nombre=form.nombre.data,
            descripcion=form.descripcion.data,
            maestro_id=form.maestro_id.data
        )
        db.session.add(curso)
        db.session.commit()
        flash('Curso registrado con éxito!', 'success')
        return redirect(url_for('cursos.index'))

    lista_cursos = Curso.query.all()
    return render_template('cursos/index.html', cursos=lista_cursos, form=form)


@cursos.route('/<int:id>/alumnos', methods=['GET', 'POST'])
def alumnos_curso(id):
    curso = Curso.query.get_or_404(id)
    form = InscripcionForm()
    inscritos_ids = [a.id for a in curso.alumnos]
    query_alumnos = Alumnos.query.filter(~Alumnos.id.in_(inscritos_ids)).all() if inscritos_ids else Alumnos.query.all()

    form.alumno_id.choices = [(a.id, f"{a.nombre} {a.apaterno}") for a in query_alumnos]

    if form.validate_on_submit():
        alumno = Alumnos.query.get(form.alumno_id.data)
        curso.alumnos.append(alumno)
        db.session.commit()
        flash('Alumno inscrito con éxito al curso.', 'success')
        return redirect(url_for('cursos.alumnos_curso', id=curso.id))

    return render_template('cursos/alumnos.html', curso=curso, form=form)


@cursos.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    curso = Curso.query.get_or_404(id)
    form = CursoForm(obj=curso)
    form.maestro_id.choices = [(m.matricula, f"{m.nombre} {m.apellidos}") for m in Maestros.query.all()]

    if form.validate_on_submit():
        curso.nombre = form.nombre.data
        curso.descripcion = form.descripcion.data
        curso.maestro_id = form.maestro_id.data
        db.session.commit()
        flash('Curso actualizado con éxito!', 'success')
        return redirect(url_for('cursos.index'))

    return render_template('cursos/edit.html', form=form, curso=curso)


@cursos.route('/eliminar/<int:id>')
def eliminar(id):
    curso = Curso.query.get_or_404(id)
    db.session.delete(curso)
    db.session.commit()
    flash('Curso eliminado con éxito!', 'success')
    return redirect(url_for('cursos.index'))


@cursos.route('/<int:curso_id>/desasignar/<int:alumno_id>')
def desasignar_alumno(curso_id, alumno_id):
    curso = Curso.query.get_or_404(curso_id)
    alumno = Alumnos.query.get_or_404(alumno_id)
    if alumno in curso.alumnos:
        curso.alumnos.remove(alumno)
        db.session.commit()
        flash('Alumno desasignado del curso correctamente.', 'success')

    return redirect(url_for('cursos.alumnos_curso', id=curso.id))