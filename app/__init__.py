from flask import Flask, render_template, request, flash, redirect, url_for
import os
from app.forms import ClienteForm, FuncionarioForm, ServicoForm
from app.models import db, Cliente, Funcionario, Servico


def create_app():
    app  = Flask(__name__,instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.dirname(app.instance_path)}/databases/app.sqlite"
    )
    app.config.from_pyfile('config.py',silent=True)

    db.init_app(app)

    @app.route('/')
    def index():
        return render_template('base.html')

    @app.route('/clientes', methods=['POST', 'GET'])
    def clientes():
        clientes_lista = Cliente.query.all()
        form = ClienteForm(request.form)
        if request.method == 'POST'  and form.validate():
            cliente = Cliente(name=form.name.data,email=form.email.data)
            db.session.add(cliente)
            db.session.commit()
            flash('Cliente Registrado!')
            return redirect(url_for('clientes'))
        return render_template('clientes.html', clientes_lista=clientes_lista, form = form)
    
    @app.route('/servicos', methods=['POST', 'GET'])
    def servicos():
        servicos_lista = Servico.query.all()
        form = ServicoForm(request.form)
        if request.method == 'POST' and form.validate():
            servico = Servico(servico=form.servico.data)
            db.session.add(servico)
            db.session.commit()
            flash('Serviço Registrado!')
            return redirect(url_for('servicos'))
        return render_template('servicos.html',servicos_lista=servicos_lista,form = form)

    @app.route('/funcionarios', methods=['POST', 'GET'])
    def funcionarios():
        funcionarios_lista = Funcionario.query.all()
        form = FuncionarioForm(request.form)
        if request.method == 'POST'  and form.validate():
            funcionario = Funcionario(name=form.name.data,cpf=form.cpf.data)
            db.session.add(funcionario)
            db.session.commit()
            flash('Funcionário Registrado!')
            return redirect(url_for('funcionarios'))
        return render_template('funcionarios.html', funcionarios_lista=funcionarios_lista, form = form)

    @app.route('/agenda', methods=['POST', 'GET'])
    def agenda():
        return render_template('agenda.html')
    
    return app