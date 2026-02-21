import re

from flask import Flask, render_template, request, redirect, url_for
from flask_wtf.csrf import CSRFProtect

import forms

from config import DevelopmentConfig
from models import db, Alumnos

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db.init_app(app)
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
    create_form = forms.UserForm(request.form)
    if request.method == 'POST':
        alum = Alumnos(nombre=create_form.nombre.data,
                       apaterno=create_form.apaterno.data,
                       email=create_form.email.data)
        db.session.add(alum)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template("Alumnos.html", form=create_form)


@app.route("/detalles", methods=["GET", "POST"])
def detalles():
    if request.method == 'GET':
        id = request.args.get('id')
        # select * from alumnos where id = id
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        nombre = alum1.nombre
        apaterno = alum1.apaterno
        correo = alum1.correo
        return render_template("detalles.html", nombre=nombre, apaterno=apaterno, email=correo)
    return render_template("detalles.html")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run()