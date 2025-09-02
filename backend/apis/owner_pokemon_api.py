from flask_openapi3 import Tag, APIBlueprint
from flask import jsonify
from sqlalchemy import desc

from ..database import db
from ..table.owner_pokemon import OwnerPokemon
from ..table.account_user import AccountUser
from ..schema import (OwnerPokemonSchema_All, OwnerPokemonSchema_No_Auto, OwnerPokemonSchema_PrimaryKey)
from ..error_schema import ValidationErrorResponse

owner_pokemon_api = APIBlueprint('owner_pokemon_api', __name__, url_prefix='/owner_pokemon')
owner_pokemon_tag = Tag(name="Pokemon e seus Donos", description="Operação relacionando o pokemon e seu dono")

@owner_pokemon_api.get('/', tags=[owner_pokemon_tag],responses={"200": OwnerPokemonSchema_All, "422": ValidationErrorResponse},
         summary="Requisição para puxar todos os pokemons adotados")
def get_all_owner_pokemon():
    owner_pokemon = OwnerPokemon.query.order_by(desc(OwnerPokemon.user_id)).all()
    result = [
        {k: v for k, v in user.__dict__.items() if not k.startswith('_')}
        for user in owner_pokemon
    ]
    return jsonify(result)


@owner_pokemon_api.post('/', tags=[owner_pokemon_tag],responses={"200": OwnerPokemonSchema_No_Auto, "422": ValidationErrorResponse},
         summary="Requisição para cadastrar novos pokemons de um usuários")
def add_owner_pokemon(body: OwnerPokemonSchema_No_Auto):
    data = body.model_dump()
    user_id = data.get('user_id')
    user = AccountUser.query.filter_by(user_id=user_id).first()

    if user:    
        new_user_pokemon = OwnerPokemon(**data)
        db.session.add(new_user_pokemon)
        db.session.commit()

        return jsonify({
            "message": f"Pokemon {new_user_pokemon.pokemon_id} foi adotado",
            "pokemon_id": new_user_pokemon.pokemon_id,
        })


@owner_pokemon_api.put('/', tags=[owner_pokemon_tag],responses={"200": OwnerPokemonSchema_All, "422": ValidationErrorResponse},
         summary="Requisição para alterar dados do pokemon de um usuário")
def update_owner_pokemon(body: OwnerPokemonSchema_All):
    data = body.model_dump()
    pokemon_id = int(data.get('pokemon_id'))
    pokemon_obj = db.session.get(OwnerPokemon, pokemon_id)

    if not pokemon_obj:
        return jsonify({"error": "pokemon não encontrado"}), 404

    for key, value in data.items():
        if hasattr(pokemon_obj, key):
            setattr(pokemon_obj, key, value)

    db.session.commit()

    return jsonify({
        "message": f"Daddos do Pokemon {pokemon_id} atualizado com sucesso!",
        "pokemon_id": pokemon_id,
    })


@owner_pokemon_api.delete('/', tags=[owner_pokemon_tag],responses={"200": OwnerPokemonSchema_PrimaryKey, "422": ValidationErrorResponse},
         summary="Requisição para deletar um pokemons de um usuário")
def delete_owner_pokemon(body: OwnerPokemonSchema_PrimaryKey):
    data = body.model_dump()
    pokemon_id = int(data.get('pokemon_id'))
    pokemon_obj = db.session.get(OwnerPokemon, pokemon_id)

    if not pokemon_obj:
        return jsonify({"error": "Pokemon não encontrado"}), 404

    db.session.delete(pokemon_obj)
    db.session.commit()

    return jsonify({
        "message": f"Pokemon {pokemon_id} removido com sucesso!",
        "pokemon_id": pokemon_id,
    })
