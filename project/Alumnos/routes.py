from flask import Blueprint
from flask import request
import forms as forms
from models import Alumnos, db
from flask import Flask, redirect, render_template, url_for

alumnos=Blueprint('alumnos',__name__)

@alumnos.route("/", methods=["GET","POST"])
def index():
    create_form = forms.UserForm(request.form)
    if request.method == 'POST':
        alum = Alumnos(nombre = create_form.nombre.data,
                       apellidos = create_form.apellidos.data,
                       correo = create_form.email.data)
       #Realizar el insert en la bd
        db.session.add(alum)
        db.session.commit()
        return redirect(url_for('alumnos.ABCompleto'))
    return render_template('index.html',form = create_form)

@alumnos.route("/ABCompleto",methods=['GET','POST'])
def ABCompleto():
    create_form=forms.UserForm(request.form)
    #Select * from alumnos
    alumnos=Alumnos.query.all()
    return render_template('ABCompleto.html',form=create_form,alumnos=alumnos)

@alumnos.route("/modificar",methods=['GET','POST'])
def modificar():
    create_form=forms.UserForm(request.form)
    if request.method=='GET':
        id=request.args.get('id')
        #Select * from alumnos where id==id
        alum1=db.session.query(Alumnos).filter(Alumnos.id==id).first()
        create_form.id.data=id
        create_form.nombre.data=alum1.nombre
        create_form.apellidos.data=alum1.apellidos
        create_form.email.data=alum1.correo
        
    if request.method=='POST':
        #Select * from alumnos where id==id
        id = create_form.id.data
        alum2=db.session.query(Alumnos).filter(Alumnos.id==id).first()
        
        alum2.nombre=create_form.nombre.data
        alum2.apellidos=create_form.apellidos.data
        alum2.email=create_form.email.data
        db.session.add(alum2)
        db.session.commit()
        return redirect(url_for('alumnos.ABCompleto'))
    return render_template('modificar.html',form=create_form)


@alumnos.route("/eliminar",methods=['GET','POST'])
def eliminar():
    create_form=forms.UserForm(request.form)
    if request.method=='GET':
        id=request.args.get('id')
        #Select * from alumnos where id==id
        alum1=db.session.query(Alumnos).filter(Alumnos.id==id).first()
        create_form.id.data=id
        create_form.nombre.data=alum1.nombre
        create_form.apellidos.data=alum1.apellidos
        create_form.email.data=alum1.correo
        
    if request.method=='POST':
        id = create_form.id.data
        alum2=db.session.query(Alumnos).filter(Alumnos.id==id).first()
        alum2.nombre=create_form.nombre.data
        alum2.apellidos=create_form.apellidos.data
        alum2.email=create_form.email.data
        db.session.delete(alum2)
        db.session.commit()
        return redirect(url_for('alumnos.ABCompleto'))
    return render_template('eliminar.html',form=create_form)