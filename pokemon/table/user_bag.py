from ..database import db
from datetime import date


class UserBag(db.Model):
    """
    A tabela User Bag é uma tabela destinada a guardas os os items comprados e utilizados pelo usuário
    """
    __tablename__ = 'user_bag'

    date = db.Column(db.Date, default=date.today, nullable=True, 
                    info={"description": "registro da data de compra ou utilização do item"})

    bag_id = db.Column(db.Integer, primary_key=True, autoincrement=True, 
                    info={"description": "chave primária das transações realizadas"})
    
    operation_type = db.Column(db.String, nullable=False, 
                    info={"description": "descrição se a operação é um input ou output"})
    
    user_id = db.Column(db.Integer, nullable=False, 
                    info={"description": "id do usuário que capturou o pokemon"})
    
    item_id = db.Column(db.String, nullable=False, 
                    info={"description": "item utilizado"})
    
    pokemon_id = db.Column(db.Integer, nullable=True, 
                    info={"description": "id do pokemon que utilizou o item"})
    
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)