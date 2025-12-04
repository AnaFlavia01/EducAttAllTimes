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


bp = Blueprint('cadastro_prof',__name__)


@bp.route('/cadastro_prof')
def cadastro_prof():
    return render_template('CADASTRO_PROF.html')


@bp.route("/prof/cadastrar",methods=["GET","POST"])
def cadastrar_prof():
    if request.method == "POST":
        nome_professor = request.form["nome"]
        email_professor = request.form["email"]
        senha_professor = request.form["senha"]
        cndb_professor_valor = request.form["cndb"]
        banco = ligar_banco()
        cursor = banco.cursor()
        cursor.execute(
            "INSERT INTO professor (nome,  email, senha, cndb_professor ) VALUES (%s, %s, %s,%s )",
            (nome_professor, email_professor,senha_professor, cndb_professor_valor )
        )
        banco.commit()
        banco.close()
        return redirect('/pag_indi_prof')
    return render_template("paginaDoProfessor.html")
