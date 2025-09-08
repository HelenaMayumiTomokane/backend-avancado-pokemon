from ..database import db
from datetime import date


class CashAudit(db.Model):
    """
    A tabela Cash Audit é uma tabela destinada a guardas os dados de todas as transações por cada usuário
    """
    __tablename__ = 'cash_audit'

    date = db.Column(db.Date, default=date.today, nullable=True, 
                    info={"description": "registro da data da operação de cash"})

    cash_id = db.Column(db.Integer, primary_key=True, autoincrement=True, 
                    info={"description": "chave primária das transações realizadas"})
    
    operation = db.Column(db.String, nullable=False, 
                    info={"description": "descrição se a operação é um input ou output"})
    
    user_id = db.Column(db.Integer, nullable=False, 
                    info={"description": "id do usuário que capturou o pokemon"})
    
    value = db.Column(db.Float, nullable=False, 
                    info={"description": "valor da operação"})
    
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)