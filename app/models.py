from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self) -> str:
        return f'<Cliente {self.name}>'


class Servico(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    servico = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self) -> str:
        return f'<Servico {self.servico}>'


class Funcionario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)

    def __repr__(self) -> str:
        return f'<Funcionario {self.name}>'