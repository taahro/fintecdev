from flask import Blueprint, render_template, request
from .mrca_module import MRCA

mrca_bp = Blueprint('mrca', __name__)

@mrca_bp.route('/', methods=['GET', 'POST'])
def analyze_mrca():
    if request.method == 'POST':
        mrca = MRCA()
        result = mrca.analyze()
        return render_template('results.html', task='MRCA', result=result)
    return render_template('mrca.html')
