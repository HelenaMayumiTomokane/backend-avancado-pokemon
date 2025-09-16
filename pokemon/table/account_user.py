from ..database import db
from datetime import date


class AccountUser(db.Model):
    """
    A tabela Account User é uma tabela destinada a guardas os dados básicos do usuário
    """
    __tablename__ = 'account_user'

    date = db.Column(db.Date, default=date.today, nullable=True, 
                    info={"description": "registro da data de criação do usuário"})

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True, 
                    info={"description": "chave primária, dos usuários cadastrados na base"})
    
    login = db.Column(db.String, nullable=False, 
                    info={"description": "login do usuário"})
    
    name = db.Column(db.String, nullable=False, 
                    info={"description": "nome do usuário"})
    
    password = db.Column(db.String, nullable=False, 
                    info={"description": "senha do usuário"})
    
    
    role = db.Column(db.String, nullable=False,
                    info={"description": "definição de administrador ou visitante"})
    
    # Relacionamentos do usuário com cascade para deleção automática
    user_bag = db.relationship("UserBag", backref="user", cascade="all, delete-orphan", lazy=True)
    cash_audit = db.relationship("CashAudit", backref="user", cascade="all, delete-orphan", lazy=True)
    owner_pokemons = db.relationship("OwnerPokemon", backref="user", cascade="all, delete-orphan", lazy=True)


    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)