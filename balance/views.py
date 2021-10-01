from sqlite3.dbapi2 import Date
from balance.templates.forms import MovimientoFormulario
import re
from . import app
from flask import render_template, request, redirect, url_for, flash
from balance.models import DBManager
from datetime import date

ruta_basedatos = app.config.get("RUTA_BASE_DE_DATOS")
dbManager = DBManager(ruta_basedatos)

@app.route("/")
def inicio():
    consulta = """SELECT * 
        FROM movimientos
        ORDER BY fecha;
    """
    movimientos = dbManager.consultaSQL(consulta)
    return render_template("inicio.html", items=movimientos)

@app.route("/nuevo", methods=["GET", "POST"])
def nuevo():
    formulario = MovimientoFormulario()

    if request.method == "GET":
        return render_template("nuevo_movimiento.html", el_formulario=formulario)
    else:
        if formulario.validate():
            consulta = "INSERT INTO movimientos (fecha, concepto, gasto_ingreso, cantidad) VALUES (:fecha, :concepto, :gasto_ingreso, :cantidad)"
            dbManager.modificaSQL(consulta, formulario.data)
            """
            except Exception as e:
                print("Se ha producido un error de acceso a la base de datos: ", e)
                flash("Se ha producido un error en la base de datos. Consulte con su administrador") #Flash le manda el mensaje a Jinja y hace que este disponible para la plantilla.
                return render_template("nuevo_movimiento.html", el_formulario = formulario)

            return redirect(url_for("inicio"))
            """
        else:
            return render_template("nuevo_movimiento.html", el_formulario = formulario) 
    

@app.route("/borrar/<int:id>", methods=["GET", "POST"]) #Forma de pasar un id entero para que borre el numero que se le manda en ese id.
def borrar(id):
    if request.method == "GET":
        consulta = """
            SELECT id, fecha, concepto, gasto_ingreso, cantidad 
              FROM movimientos
            WHERE  id = ? 
             ORDER BY fecha;
        """
        movimientos = dbManager.consultaSQL(consulta, [id])
        if len(movimientos) == 0:
            flash(f"Movimiento {id} no encontrado")
            return redirect(url_for("inicio"))            

        el_movimiento = movimientos[0]
        el_movimiento["fecha"] = date.fromisoformat(el_movimiento["fecha"]) #Pasamos la cadena de fecha a formato date, debería hacerse en models
        formulario = MovimientoFormulario(data = el_movimiento)
        return render_template("borrar_movimiento.html", el_formulario = formulario, id = el_movimiento['id'])
    else:
        movimientos = dbManager.borrarSQL(id)
        return redirect(url_for("inicio"))