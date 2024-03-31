from flask import Flask, url_for, request, render_template, redirect, flash
from flask_wtf import FlaskForm
from sqll import *
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired
init_database()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'predpof_code_crusaders'


@app.route('/', methods=['GET'])
def first():
    return render_template('sigma.html', style=url_for('static', filename='css/css_for_reg.css'))


@app.route('/all_days', methods=['GET'])
def reg():
    date = request.form['zxc']
    context = get_day(date)
    return render_template('all_days.html', style=url_for('static', filename='css/css_for_reg.css'), context=context)


if __name__ == '__main__':
    app.run(port=8888, host='127.0.0.1')
