# python.exe -m venv .venv
# cd .venv/Scripts
# activate.bat
# py -m ensurepip --upgrade
# pip install -r requirements.txt

from flask import Flask

from flask import render_template
from flask import request
from flask import jsonify, make_response

import mysql.connector

import datetime
import pytz

from flask_cors import CORS, cross_origin

con = mysql.connector.connect(
    host="82.197.82.90",
    database="u861594054_app9",
    user="u861594054_Misael2009",
    password="NZqhQyiNZ3Tg8JJ"
)

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    if not con.is_connected():
        con.reconnect()

    con.close()

    return render_template("index.html")

@app.route("/app")
def app2():
    if not con.is_connected():
        con.reconnect()

    con.close()

    return "<h5>Hola, soy la view app</h5>"

@app.route("/asistencias")
def asistencias():
    if not con.is_connected():
        con.reconnect()

    cursor = con.cursor(dictionary=True)
    sql    = "SELECT  `idAsistencia`, `empleado`, `reporte`, `reporte` FROM `vistatotal` LIMIT 10 OFFSET 0"

    cursor.execute(sql)
    registros = cursor.fetchall()

    return render_template("asistencias.html", asistencias=registros)
@app.route("/empleados")
def empleados():
    if not con.is_connected():
        con.reconnect()

    cursor = con.cursor(dictionary=True)
    sql    = "SELECT `idEmpleado`, `nombreEmpleado`, `numero`, `fechaIngreso` FROM empleados LIMIT 10 OFFSET 0"

    cursor.execute(sql)
    registros = cursor.fetchall()

    # Si manejas fechas y horas
    for registro in registros:
        fecha_hora = registro["fechaIngreso"]

        registro["Fecha_Hora"] = fecha_hora.strftime("%Y-%m-%d %H:%M:%S")


    return render_template("empleados.html", empleados=registros)

@app.route("/reportes")
def reportes():
    if not con.is_connected():
        con.reconnect()

    cursor = con.cursor(dictionary=True)
    sql    = "SELECT `idReporte`, `fecha`, `comentarios` FROM `reportes` LIMIT 10 OFFSET 0"

    cursor.execute(sql)
    registros = cursor.fetchall()

    # Si manejas fechas y horas
    for registro in registros:
        fecha_hora = registro["fecha"]

        registro["Fecha"]      = fecha_hora.strftime("%d/%m/%Y")

    return render_template("reportes.html", reportes=registros)
