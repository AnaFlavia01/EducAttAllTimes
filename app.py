from flask import Flask, render_template
import psycopg2
from Rotas import (pag_login, cadastro_aluno, cadastro_prof, pag_indi_prof,
                   contato, login, login_prof, progresso, alunos, editar_aluno)



def ligar_banco():
    banco = psycopg2.connect(
        host="localhost",
        dbname="EducAttAllTimes",
        user="postgres",
        password="senai",
    )
    return banco

app = Flask(__name__)
app.secret_key='senai'

app.register_blueprint(pag_login.bp)
app.register_blueprint(cadastro_aluno.bp)
app.register_blueprint(cadastro_prof.bp)
app.register_blueprint(pag_indi_prof.bp)
app.register_blueprint(contato.bp)
app.register_blueprint(login.bp)
app.register_blueprint(login_prof.bp)
app.register_blueprint(progresso.bp)
app.register_blueprint(alunos.bp)
app.register_blueprint(editar_aluno.bp)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/apresentacao_conteudo')
def apresentacao_conteudo():
    return render_template('ApresentacaoConteudo.html')

@app.route('/apresentacao_conteudo_prof')
def apresentacao_conteudo_prof():
    return render_template('ApresentacaoConteudoProf.html')

@app.route('/estudo')
def estudo():
    return render_template('ESTUDO.html')

@app.route('/estudando1')
def estudando1():
    return render_template('ESTUDANDO1.html')

@app.route('/estudando2')
def estudando2():
    return render_template('ESTUDANDO2.html')

@app.route('/estudando3')
def estudando3():
    return render_template('ESTUDANDO3.html')

@app.route('/estudando4')
def estudando4():
    return render_template('ESTUDANDO4.html')

@app.route('/exibir_aluno')
def exibir_aluno():
    return render_template('exibir_aluno.html')

@app.route('/editar_aluno')
def editar_aluno():
    return render_template('editar_aluno.html')



if __name__ == '__main__':
    app.run()
