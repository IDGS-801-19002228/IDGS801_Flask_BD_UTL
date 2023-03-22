from flask import Flask, redirect, render_template
from flask import request
from flask import url_for
import forms as forms

#from flask import jsonifys
from config import DevelomentConfig
from flask_wtf.csrf import CSRFProtect
from models import Alumnos, db
from Alumnos.routes import alumnos
from Maestros.routes import maestros

app=Flask(__name__)
app.config.from_object(DevelomentConfig)
csrf= CSRFProtect()

@app.route("/")
def index():
   return render_template('index.html')

app.register_blueprint(alumnos)
app.register_blueprint(maestros)


if __name__ =='__main__':
    csrf.init_app(app) #al iniciar tiene seguridad crsf
    db.init_app(app) #iniciar la conexion a la base de datos 
    with app.app_context(): #verifica si se hizo la conexion y crea las tablas 
        db.create_all()
    app.run(port=3000)

