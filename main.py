from flask import Flask, request, render_template, url_for
import sqlite3 as sql


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
    return render_template('pacientes.html', pacientes = pacientes)

@app.route('/agregar_paciente')
def add_paciente():
    return render_template('agregar_paciente.html')

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
        return "joya"
    else:       
        return render_template('asignacion_turnos.html')






#CORREMOS LA APP
if __name__ == '__main__':
    app.run(debug=True, port=3000)