from flask_openapi3 import Tag, APIBlueprint
from flask import jsonify
from sqlalchemy import desc

from ..database import db
from ..table.user_bag import UserBag
from ..table.account_user import AccountUser
from ..schema import (UserBagSchema_All, UserBagSchema_No_Auto, UserBagSchema_PrimaryKey)
from ..error_schema import ValidationErrorResponse

user_bag_api = APIBlueprint('user_bag_api', __name__, url_prefix='/user_bag')
user_bag_tag = Tag(name="Itens na Bag", description="Itens disponíveis ou consumidos da Bag")

@user_bag_api.get('', tags=[user_bag_tag],responses={"200": UserBagSchema_All, "422": ValidationErrorResponse},
         summary="Requisição para puxar todos os item")
def get_all_user_bag():
    user_bag = UserBag.query.order_by(desc(UserBag.user_id)).all()
    result = [
        {k: v for k, v in user.__dict__.items() if not k.startswith('_')}
        for user in user_bag
    ]
    return jsonify(result)


@user_bag_api.post('', tags=[user_bag_tag],responses={"200": UserBagSchema_No_Auto, "422": ValidationErrorResponse},
         summary="Requisição para cadastrar cadastrar a entrada ou saída de um item")
def add_user_bag(body: UserBagSchema_No_Auto):
    data = body.model_dump()
    user_id = data.get('user_id')
    user = AccountUser.query.filter_by(user_id=user_id).first()

    if user:    
        new_operation = UserBag(**data)
        db.session.add(new_operation)
        db.session.commit()

        return jsonify({
            "message": f"Operação Realizada",
            "bag_id": new_operation.bag_id,
        })


@user_bag_api.put('', tags=[user_bag_tag],responses={"200": UserBagSchema_All, "422": ValidationErrorResponse},
         summary="Requisição para alterar os dados dos items")
def update_user_bag(body: UserBagSchema_All):
    data = body.model_dump()
    bag_id = int(data.get('bag_id'))
    pokemon_obj = db.session.get(UserBag, bag_id)

    if not pokemon_obj:
        return jsonify({"error": "pokemon não encontrado"}), 404

    for key, value in data.items():
        if hasattr(pokemon_obj, key):
            setattr(pokemon_obj, key, value)

    db.session.commit()

    return jsonify({
        "message": f"Operação Realizada",
        "bag_id": bag_id,
    })


@user_bag_api.delete('', tags=[user_bag_tag],responses={"200": UserBagSchema_PrimaryKey, "422": ValidationErrorResponse},
         summary="Requisição para deletar um pokemons de um usuário")
def delete_user_bag(body: UserBagSchema_PrimaryKey):
    data = body.model_dump()
    bag_id = int(data.get('bag_id'))
    pokemon_obj = db.session.get(UserBag, bag_id)

    if not pokemon_obj:
        return jsonify({"error": "Pokemon não encontrado"}), 404

    db.session.delete(pokemon_obj)
    db.session.commit()

    return jsonify({
        "message": f"Operação Realizada",
        "bag_id": bag_id,
    })
