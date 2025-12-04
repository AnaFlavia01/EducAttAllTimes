from flask import Flask, render_template, Blueprint


bp = Blueprint('pag_indi_prof',__name__)


@bp.route('/pag_indi_prof')
def pag_indi_prof():
    return render_template('paginaDoProfessor.html')