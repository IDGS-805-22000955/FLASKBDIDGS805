from flask import Flask, render_template
from config import DevelopmentConfig
from models import db
from flask_wtf.csrf import CSRFProtect
from flask_migrate import Migrate

from alumnos.routes import alumnos
from maestros.routes import maestros

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

db.init_app(app)
migrate = Migrate(app, db)
csrf = CSRFProtect(app)

app.register_blueprint(alumnos)
app.register_blueprint(maestros)

@app.route('/')
def index():
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()
