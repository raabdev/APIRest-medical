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