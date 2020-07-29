from flask import Flask, request, render_template, url_for
import pandas as pd


#CREAMOS UNA INSTANCIA
app = Flask(__name__)

#CREAMOS EL DECORADOR
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/turnos/')
def turnos():
    return render_template('turnos.html')

@app.route('/turnos/asignacion_turnos/', methods = ["GET", "POST"])
def asignacion_turnos():
    if request.method == "POST":
        resultados = request.form
        print(resultados)
        return resultados
    else:
        horarios = pd.read_excel('turnos.xlsx')
        print(horarios)
        return render_template('asignacion_turnos.html')






#CORREMOS LA APP
if __name__ == '__main__':
    app.run(debug=True, port=3000)