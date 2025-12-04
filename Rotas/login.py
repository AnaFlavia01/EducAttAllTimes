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


bp = Blueprint('login',__name__)


@bp.route('/login')
def login():
    return render_template('LOGIN.html')



@bp.route('/autenticar', methods =["POST"])
def autenticar():
    email = request.form['email']
    senha = request.form['senha']
    banco = ligar_banco()
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM aluno WHERE email=%s AND senha=%s", (email, senha))
    usuario = cursor.fetchone()
    if usuario:
        session['Usuario_Logado'] = email
        return redirect('/apresentacao_conteudo')
    else:
        return redirect('/login')



@bp.route('/deslogar')
def deslogar():
    session.clear()
    return redirect('/login')


