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


bp = Blueprint('cadastro_aluno',__name__)


@bp.route('/cadastro_aluno')
def cadastro_aluno():
    return render_template('CADASTRO_ALUNO.html')



@bp.route("/aluno/cadastrar",methods=["GET","POST"])
def cadastrar_aluno():
    if request.method == "POST":
        nome_aluno = request.form["nome"]
        email_aluno = request.form["email"]
        senha_aluno = request.form["senha"]
        banco = ligar_banco()
        cursor = banco.cursor()
        cursor.execute(
            "INSERT INTO aluno (nome,  email, senha ) VALUES (%s, %s, %s)",
            (nome_aluno, email_aluno,senha_aluno )
        )
        banco.commit()
        banco.close()
        return redirect("/")


