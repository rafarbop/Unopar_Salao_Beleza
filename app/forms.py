from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,validators

class ClienteForm(FlaskForm):
    name = StringField('Nome do Cliente', [
        validators.Length(min=4,max=80,message='Tamanho Inválido"'),
        validators.DataRequired()
    ])
    email = StringField('Email do Cliente',[
        validators.Email(),
        validators.DataRequired()
    ])
    submit = SubmitField('Cadastrar')


class ServicoForm(FlaskForm):
    servico = StringField('Nome do Serviço', [
        validators.Length(min=4,max=80,message='Tamanho Inválido"'),
        validators.DataRequired()
    ])
    submit = SubmitField('Cadastrar')


class FuncionarioForm(FlaskForm):
    name = StringField('Nome do Funcionario', [
        validators.Length(min=4,max=80,message='Tamanho Inválido"'),
        validators.DataRequired()
    ])
    cpf = StringField('CPF do Funcionario',[
        validators.Length(min=11,max=11,message='Tamanho Inválido"'),
        validators.DataRequired()
    ])
    submit = SubmitField('Cadastrar')

