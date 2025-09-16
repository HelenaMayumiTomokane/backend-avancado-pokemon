from ..database import db
from datetime import date


class OwnerPokemon(db.Model):
    """
    A tabela Owner Pokemon é uma tabela destinada a guardas os dados de cada pokemon capturado por cada usuário
    """
    __tablename__ = 'owner_pokemon'

    date = db.Column(db.Date, default=date.today, nullable=True, 
                    info={"description": "registro da data de captura do pokemon"})

    pokemon_id = db.Column(db.Integer, primary_key=True, autoincrement=True, 
                    info={"description": "chave primária dos pokemons capturados"})
    
    pokemon_species = db.Column(db.String, nullable=False, 
                    info={"description": "espécie do pokemon"})
    
    pokemon_name = db.Column(db.String, nullable=False, 
                    info={"description": "nome do pokemon"})
    
    user_id = db.Column(db.Integer, db.ForeignKey('account_user.user_id'), nullable=False, 
                    info={"description": "id do usuário que capturou o pokemon"})
    
    pokemon_id_external_api = db.Column(db.Integer, nullable=False, 
                    info={"description": "id do pokemon da api externa"})
    
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)