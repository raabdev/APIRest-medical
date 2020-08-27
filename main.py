from flask import Flask, request, render_template, url_for, redirect
import sqlite3 as sql
import datetime


#CREAMOS UNA INSTANCIA
app = Flask(__name__)

#RUTAS
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pacientes')
def pacientes():
    con = sql.connect('database.db')
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from pacientes")
    pacientes = cur.fetchall()
    con.close()
    return render_template('pacientes.html', pacientes = pacientes)

@app.route('/agregar_paciente')
def add_paciente():
    return render_template('agregar_paciente.html')

@app.route('/modificar/<string:id>')
def get_paciente(id):
    con = sql.connect('database.db')
    cur = con.cursor()
    cur.execute(f"select * from pacientes where id = {id}")
    data = cur.fetchall()
    return render_template('editar_paciente.html', paciente = data[0])

@app.route('/update/<string:id>', methods = ["POST"])
def update_paciente(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        dni = request.form['dni']
        social = request.form['social']
        plan = request.form['plan']
        direccion = request.form['direccion']
        localidad = request.form['localidad'] 
        con = sql.connect('database.db')
        cur = con.cursor()
        sql_ejecutar = """update pacientes set nombre = ?,
                                                dni = ?,
                                                social = ?,
                                                plan = ?,
                                                direccion = ?,
                                                localidad = ?
                                                where id = ?"""
        data = (nombre,dni,social,plan,direccion,localidad,id)
        cur.execute(sql_ejecutar, data)
        con.commit()
        return redirect(url_for('pacientes'))


@app.route('/borrar/<string:id>')
def borrar(id):
    con = sql.connect('database.db')
    cur = con.cursor()
    cur.execute(f"delete from pacientes where id = {id}")
    con.commit()
    con.close()
    return redirect(url_for('pacientes'))

@app.route('/add_record', methods = ["POST", "GET"])
def addrec():
    if request.method == 'POST':
        nombre = request.form['nombre']
        dni = request.form['dni']
        social = request.form['social']
        plan = request.form['plan']
        direccion = request.form['direccion']
        localidad = request.form['localidad']

        con = sql.connect('database.db')
        cur = con.cursor()

        cur.execute("INSERT INTO pacientes (nombre,dni,social,plan,direccion,localidad) VALUES (?,?,?,?,?,?)",(nombre,dni,social,plan,direccion,localidad))
        con.commit()
        con.close()
        return render_template('resultado.html')

@app.route('/turnos/')
def turnos():
    return render_template('turnos.html')

@app.route('/turnos/asignacion_turnos/', methods = ["GET", "POST"])
def asignacion_turnos():
    if request.method == "POST":
        
        #practica elegida
        practica = request.form['servicio1']

        #buscamos los pacientes
        con = sql.connect('database.db')
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute("select * from pacientes")
        pacientes = cur.fetchall()
        con.close()

        return render_template('filtrar_paciente.html', pacientes = pacientes, practica = practica)
    else:

        return render_template('asignacion_turnos.html')

@app.route('/confirm_turno', methods = ["POST", "GET"])
def confirm_turno():
    return render_template('filtrar_paciente.html')

@app.route('/turnos/asignacion_turnos/filtrar_paciente')
def filtrar():
    return 'filtrado'


#CORREMOS LA APP
if __name__ == '__main__':
    app.run(debug=True, port=3000)