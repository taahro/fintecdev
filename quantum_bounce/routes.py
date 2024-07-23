from flask import Blueprint, render_template, request, redirect, url_for, flash
from .quantum_bounce_module import QuantumBounce

quantum_bounce_bp = Blueprint('quantum_bounce', __name__)

@quantum_bounce_bp.route('/', methods=['GET', 'POST'])
def calculate_bounce():
    if request.method == 'POST':
        try:
            critical_density = float(request.form['critical_density'])
            energy_density = float(request.form['energy_density'])
            qb = QuantumBounce(critical_density=critical_density, energy_density=energy_density)
            result = qb.calculate()
            return render_template('results.html', task='Quantum Bounce', result=result)
        except ValueError:
            flash('Invalid input! Please enter numeric values.')
            return redirect(url_for('quantum_bounce.calculate_bounce'))
    return render_template('quantum_bounce.html')
