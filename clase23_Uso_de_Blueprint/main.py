from flask import request, make_response, redirect, render_template, session, url_for, flash
from flask_bootstrap import Bootstrap 
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
import unittest

from app import create_app
from app.forms import LoginForm

app = create_app()

#todos = ['TODO 1', 'TODO 2', 'TODO 3']
todos = ['Comprar Café', 'Solicitud de compra', 'Entregar video al productor']

@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)

@app.route('/trigger_error')
def trigger_error():
    # Algo que cause un error 500 (por ejemplo, dividir por cero)
    ##result = 1 / 0
    ##return 'Esta línea nunca se alcanzará'
    # Lanzar un error HTTP 500
    abort(500)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)

@app.errorhandler(500)
def server_error(error):
    return render_template('500.html', error=error)

@app.route('/')
def index():
    user_ip = request.remote_addr

    response = make_response(redirect('/hello'))
    #response.set_cookie('user_ip', user_ip)
    session['user_ip'] = user_ip

    return response


@app.route('/hello', methods=['GET', 'POST'])
def hello():
    #user_ip = request.cookies.get('user_ip')
    user_ip = session.get('user_ip')
    login_form = LoginForm()
    username = session.get('username')
    # Dicccionario de python llamado context, ahora en lugar de usar
    # como parametros user_ip=user_ip, todos=todos, convirtiendo en variables o key values 
    context = {
        'user_ip': user_ip,
        'todos': todos,
        'login_form': login_form,
        'username' : username
    }

    if login_form.validate_on_submit():
        username = login_form.username.data
        session['username'] = username

        flash('Nombre de usuario registrado con exito!')

        return redirect(url_for('index'))

    return render_template('hello.html', **context)
    #return render_template('hello.html', user_ip=user_ip, todos=todos)
