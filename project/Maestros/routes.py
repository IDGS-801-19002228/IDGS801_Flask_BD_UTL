from flask import Blueprint
from flask import request
import forms as forms
from models import Alumnos, db, Maestros
from flask import Flask, redirect, render_template, url_for
from db import get_connection

maestros=Blueprint('maestros',__name__)

@maestros.route("/insertarM", methods=["GET","POST"])
def insertarM():
    create_form2 = forms.MaestroForm(request.form)
    if request.method == 'POST':
        nombre = create_form2.nombre.data
        apellidos = create_form2.apellidos.data
        correo = create_form2.email.data
        tel = create_form2.tel.data
        try:
           connection=get_connection()
           with connection.cursor() as cursor:
                cursor.execute('call insertar_maestro(%s,%s,%s,%s)', (nombre, apellidos, correo, tel))
                
           connection.commit()
           connection.close()
        except Exception as ex:
            print('ERROR {}'.format(ex))
            
        #print(nombre, apellidos, correo, tel)
        return redirect(url_for('maestros.maestros2'))
    return render_template('Maestros.html',form = create_form2)

@maestros.route("/maestros2",methods=["GET","POST"])
def maestros2():
    create_form=forms.MaestroForm(request.form)
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute('call consultar_maestro()')
            resultset = cursor.fetchall()
        cursor.close()
    except Exception as ex:
        print('Error')
    finally:
        connection.close()
    #print (resultset)
    return render_template("maestros.html", form=create_form, result=resultset)


@maestros.route("/modificarM",methods=['GET','POST'])
def modificarM():
    create_form2=forms.MaestroForm(request.form)
    if request.method=='GET':
        id = request.args.get('id')    
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('call consultar_maestro(%s)',(id))
                resultset = cursor.fetchall()
            cursor.close()
            for row in resultset:
                    create_form2.id.data = id
                    create_form2.nombre.data = row[2]
                    create_form2.apellidos.data = row[3]
                    create_form2.email.data = row[4]
                    create_form2.tel.data = row[5]
        except Exception as ex:
            print('Error')
        finally:
            connection.close()
        
        if request.method == 'POST':
            nombre = create_form2.nombre.data
            apellidos = create_form2.apellidos.data
            correo = create_form2.email.data
            tel = create_form2.tel.data
        try:
           connection=get_connection()
           with connection.cursor() as cursor:
                cursor.execute('call modificar_maestro(%s,%s,%s,%s)', (nombre, apellidos, correo, tel))
                
           connection.commit()
           connection.close()
        except Exception as ex:
            print('ERROR {}'.format(ex))
        
        return redirect(url_for('maestros.maestros2'))
    return render_template('modificarM.html',form=create_form2)


@maestros.route("/eliminarM",methods=['GET','POST'])
def eliminarM():
    create_form2=forms.MaestroForm(request.form)
    if request.method=='GET':
        id=request.args.get('id')
        
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('call consultar_maestro(%s)', (id))
                resultset = cursor.fetchall()
            create_form2.id.data = id
            create_form2.nombre.data = resultset[2]
            create_form2.apellidos.data = resultset[3]
            create_form2.email.data = resultset[4]
            create_form2.tel.data = resultset[5]
            cursor.close()
        except Exception as ex:
           print(ex)
        finally:
           connection.close()
    if request.method=='POST':   
        id= create_form2.id.data
        try:
            connection= get_connection()
            with connection.cursor() as curso:
                curso.execute('call eliminar_maestro(%s)',(id))
            connection.commit()
            connection.close()
        except Exception as e:
            print(e)
            pass
        return redirect(url_for('maestros.maestros2'))
    return render_template('eliminarM.html',form=create_form2)


