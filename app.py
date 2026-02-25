from flask import Flask, render_template, request, redirect, url_for
from flask_wtf.csrf import CSRFProtect
from flask_migrate import Migrate
import forms

from config import DevelopmentConfig
from models import db, Alumnos

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db.init_app(app)
migrate = Migrate(app, db)
csrf = CSRFProtect(app)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.route("/")
@app.route("/index")
def index():
    alumnos_lista = Alumnos.query.all()
    return render_template("index.html", alumnos=alumnos_lista)


@app.route("/Alumnos", methods=["GET", "POST"])
def alumnos():
    create_form = forms.UserForm2(request.form)

    if request.method == 'POST':
        alum = Alumnos(
            nombre=create_form.nombre.data,
            apellidos=create_form.apellidos.data,
            correo=create_form.correo.data
        )
        db.session.add(alum)
        db.session.commit()
        return redirect(url_for('index'))

    alumnos_lista = Alumnos.query.all()
    return render_template("Alumnos.html", form=create_form, alumnos=alumnos_lista)


@app.route("/detalles", methods=["GET", "POST"])
def detalles():
    if request.method == 'GET':
        id = request.args.get('id')
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()

        if alum1:
            return render_template("detalles.html", nombre=alum1.nombre, apellidos=alum1.apellidos, email=alum1.correo)

    return render_template("detalles.html")


@app.route("/modificar", methods=["GET", "POST"])
def modificar():
    create_form = forms.UserForm2(request.form)

    if request.method == 'GET':
        id = request.args.get('id')
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()

        if alum1:
            create_form.nombre.data = alum1.nombre
            create_form.apellidos.data = alum1.apellidos
            create_form.correo.data = alum1.correo

        return render_template("modificar.html", form=create_form)

    if request.method == 'POST':
        id = request.args.get('id')
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()

        if alum1:
            alum1.nombre = create_form.nombre.data
            alum1.apellidos = create_form.apellidos.data
            alum1.correo = create_form.correo.data

            db.session.add(alum1)
            db.session.commit()

        return redirect(url_for('index'))

@app.route("/eliminar", methods=["GET"])
def eliminar():
    id = request.args.get('id')
    alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
    if alum1:
        db.session.delete(alum1)
        db.session.commit()
    return redirect(url_for('index'))



if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run()