from flask import Flask, render_template, Blueprint


bp = Blueprint('progresso',__name__)


@bp.route('/progresso')
def progresso():
    return render_template('PROGRESSO.html')


