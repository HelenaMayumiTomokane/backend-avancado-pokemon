from ..database import db
from datetime import date


class OwnerPokemon(db.Model):
    """
    A tabela Account User é uma tabela destinada a guardas os dados básicos do usuário
    """
    __tablename__ = 'owner_pokemon'

    date = db.Column(db.Date, default=date.today, nullable=True, 
                    info={"description": "registro da data de criação do usuário"})

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True, 
                    info={"description": "chave primária, dos usuários cadastrados na base"})
    
    pokemon_name = db.Column(db.String, nullable=False, 
                    info={"description": "nome do pokemon"})
    
    pokemon_id = db.Column(db.String, nullable=False, 
                    info={"description": "id do pokemon"})
    
    pokemon_id_external_api = db.Column(db.String, nullable=False, 
                    info={"description": "id do pokemon da api externa"})
    
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)