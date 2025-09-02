from flask_openapi3 import Tag, APIBlueprint
from flask import jsonify
from sqlalchemy import desc

from ..database import db
from ..table.account_user import AccountUser
from ..schema import (AccountUserSchema_All, AccountUserSchema_No_Auto, AccountUserSchema_PrimaryKey)
from ..error_schema import ValidationErrorResponse

account_user_api = APIBlueprint('account_user_api', __name__, url_prefix='/account_user')
account_user_tag = Tag(name="Usuários", description="Operações relacionadas aos usuários")

@account_user_api.get('/', tags=[account_user_tag],responses={"200": AccountUserSchema_All, "422": ValidationErrorResponse},
         summary="Requisição para puxar os dados de usuários")
def get_all_account_user():
    account_user = AccountUser.query.order_by(desc(AccountUser.user_id)).all()
    result = [
        {k: v for k, v in user.__dict__.items() if not k.startswith('_')}
        for user in account_user
    ]
    return jsonify(result)


@account_user_api.post('/', tags=[account_user_tag],responses={"200": AccountUserSchema_No_Auto, "422": ValidationErrorResponse},
         summary="Requisição para cadastrar novos usuários")
def add_account_user(body: AccountUserSchema_No_Auto):
    data = body.model_dump()
    user_name = data.get('login')
    user = AccountUser.query.filter_by(login=user_name).first()

    if user:
        return jsonify({"error": "Usuário já cadastrado"}), 400

    new_user = AccountUser(**data)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({
        "message": f"Usuário {new_user.user_id} adicionado com sucesso!",
        "user_id": new_user.user_id,
    })


@account_user_api.put('/', tags=[account_user_tag],responses={"200": AccountUserSchema_All, "422": ValidationErrorResponse},
         summary="Requisição para alterar dados do usuário")
def update_account_user(body: AccountUserSchema_All):
    data = body.model_dump()
    user_id = int(data.get('user_id'))
    user_obj = db.session.get(AccountUser, user_id)

    if not user_obj:
        return jsonify({"error": "Usuário não encontrado"}), 404

    for key, value in data.items():
        if hasattr(user_obj, key):
            setattr(user_obj, key, value)

    db.session.commit()

    return jsonify({
        "message": f"Usuário {user_id} atualizado com sucesso!",
        "user_id": user_id,
    })


@account_user_api.delete('/', tags=[account_user_tag],responses={"200": AccountUserSchema_PrimaryKey, "422": ValidationErrorResponse},
         summary="Requisição para deletar usuário")
def delete_account_user(body: AccountUserSchema_PrimaryKey):
    data = body.model_dump()
    user_id = int(data.get('user_id'))
    user_obj = db.session.get(AccountUser, user_id)

    if not user_obj:
        return jsonify({"error": "Usuário não encontrado"}), 404

    db.session.delete(user_obj)
    db.session.commit()

    return jsonify({
        "message": f"Usuário {user_id} removido com sucesso!",
        "user_id": user_id,
    })
