from flask import render_template, request, redirect, Blueprint
import psycopg2

def ligar_banco():
    return psycopg2.connect(
        host="localhost",
        dbname="EducAttAllTimes",
        user="postgres",
        password="senai",
    )

bp = Blueprint('editar_aluno', __name__)

@bp.route("/alunos/editar/<int:id_aluno>", methods=["GET", "POST"])
def editar_curso(id_aluno):

    if request.method == "GET":
        banco = ligar_banco()
        cursor = banco.cursor()

        cursor.execute(
            "SELECT id_aluno, nome, email, senha FROM aluno WHERE id_aluno = %s",
            (id_aluno,)
        )
        aluno = cursor.fetchone()

        cursor.close()
        banco.close()


        aluno_dict = {
            "id": aluno[0],
            "nome": aluno[1],
            "email": aluno[2],
            "senha": aluno[3]
        }

        return render_template("editar_aluno.html", aluno=aluno_dict)


    elif request.method == "POST":
        nome_aluno = request.form["nome"]
        email_aluno = request.form["email"]
        senha_aluno = request.form["senha"]

        banco = ligar_banco()
        cursor = banco.cursor()

        cursor.execute(
            """
            UPDATE aluno
            SET nome = %s, email = %s, senha = %s
            WHERE id_aluno = %s
            """,
            (nome_aluno, email_aluno, senha_aluno, id_aluno)
        )

        banco.commit()
        cursor.close()
        banco.close()

        return redirect("/alunos")
