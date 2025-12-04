from flask import Flask, render_template

@bp.route('/apresentacao_conteudo')
def apresentacao_conteudo():
    return render_template('ApresentacaoConteudo.html')

