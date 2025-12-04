from flask import Flask, render_template, Blueprint, request, redirect
import psycopg2
def ligar_banco():
    banco = psycopg2.connect(
        host="localhost",
        dbname="EducAttAllTimes",
        user="postgres",
        password="senai",
    )
    return banco


bp = Blueprint('contato',__name__)


@bp.route('/contato')
def contato():
    return render_template('CONTATO.html')


@bp.route("/fazer_contato", methods=["GET", "POST"])
def contatando():
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        assunto = request.form["assunto"]
        banco = ligar_banco()
        cursor = banco.cursor()
        cursor.execute(
            "INSERT INTO contato (nome, email, assunto) VALUES (%s, %s, %s)",
            (nome, email, assunto)
        )
        banco.commit()
        banco.close()
        return redirect("/")
    return render_template('index.html')


