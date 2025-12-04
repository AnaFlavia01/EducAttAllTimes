from flask import render_template, request, redirect,Blueprint
import psycopg2

def ligar_banco():
    banco = psycopg2.connect(
        host="localhost",
        dbname="EducAttAllTimes",
        user="postgres",
        password="senai",
    )
    return banco

bp = Blueprint('alunos',__name__)
#
@bp.get("/alunos")
def alunos():
    banco = ligar_banco()
    cursor = banco.cursor()
    cursor.execute('''SELECT * FROM aluno''')
    alunos = cursor.fetchall()
    cursor.execute('SELECT id_aluno, nome FROM aluno')
    alunos = cursor.fetchall()
    cursor.close()
    return render_template("exibir_aluno.html",alunos=alunos)


@bp.post("/alunos/excluir/<int:id_aluno>")
def excluir(id_aluno):
    banco = ligar_banco()
    cursor = banco.cursor()
    cursor.execute(
        "DELETE FROM aluno WHERE id_aluno = %s",
        (id_aluno,)
    )
    banco.commit()
    cursor.close()
    banco.close()

    return redirect("/alunos")