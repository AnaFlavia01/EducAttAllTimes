from flask import Flask, render_template, Blueprint
import psycopg2
def ligar_banco():
    banco = psycopg2.connect(
        host="localhost",
        dbname="EducAttAllTimes",
        user="postgres",
        password="senai",
    )
    return banco


bp = Blueprint('pag_login',__name__)


@bp.route('/pag_login')
def pag_login():
    return render_template('paglogin.html')



