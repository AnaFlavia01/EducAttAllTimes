from flask import Flask, render_template, Blueprint, request, redirect, session
import psycopg2

def ligar_banco():
    banco = psycopg2.connect(
        host="localhost",
        dbname="EducAttAllTimes",
        user="postgres",
        password="senai",
    )
    return banco


bp = Blueprint('login_prof',__name__)


@bp.route('/login_prof')
def login_prof():
    return render_template('LOGIN_professor.html')



@bp.route('/autenticar_prof', methods =["POST"])
def autenticar_prof():
    email = request.form['email']
    senha = request.form['senha']
    banco = ligar_banco()
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM professor WHERE email=%s AND senha=%s", (email, senha))

    usuario = cursor.fetchone()
    if usuario:
        session['Usuario_Logado'] = email
        return redirect('/pag_indi_prof')
    else:
        return redirect('/login_prof')



@bp.route('/deslogar_prof')
def deslogar_prof():
    session.clear()
    return redirect('/login_prof')


