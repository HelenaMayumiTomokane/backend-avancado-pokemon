from flask_openapi3 import Tag, APIBlueprint
from flask import jsonify,request
from pydantic import BaseModel, Field

from ..database import db
from ..table.cash_audit import CashAudit
from ..table.account_user import AccountUser
from ..schema import (CashAuditSchema_All, CashAuditSchema_No_Auto, CashAuditSchema_PrimaryKey)
from ..error_schema import ValidationErrorResponse

cash_audit_api = APIBlueprint('cash_audit_api', __name__, url_prefix='/cash_audit')
cash_audit_tag = Tag(name="Histórico de Cash", description="Entradas e saídas de dinheiro Pokemon")

# Definição do schema de query parameter
class UserIdQuery(BaseModel):
    user_id: int = Field(..., description="ID do usuário")

@cash_audit_api.get('/user_id', tags=[cash_audit_tag],responses={"200": CashAuditSchema_All, "422": ValidationErrorResponse},
         summary="Requisição para puxar todos os item")
def get_all_cash_audit(query: UserIdQuery):
    user_id = query.user_id
    cash_audit = CashAudit.query.filter_by(user_id=user_id).all()
    result = [
        {k: v for k, v in user.__dict__.items() if not k.startswith('_')}
        for user in cash_audit
    ]
    return jsonify(result)


@cash_audit_api.post('', tags=[cash_audit_tag],responses={"200": CashAuditSchema_No_Auto, "422": ValidationErrorResponse},
         summary="Requisição para cadastrar cadastrar a entrada ou saída de um item")
def add_cash_audit(body: CashAuditSchema_No_Auto):
    data = body.model_dump()
    user_id = data.get('user_id')
    user = AccountUser.query.filter_by(user_id=user_id).first()

    if user:    
        new_operation = CashAudit(**data)
        db.session.add(new_operation)
        db.session.commit()

        return jsonify({
            "message": f"Operação Realizada",
            "cash_id": new_operation.cash_id,
        })


@cash_audit_api.put('', tags=[cash_audit_tag],responses={"200": CashAuditSchema_All, "422": ValidationErrorResponse},
         summary="Requisição para alterar os dados dos items")
def update_cash_audit(body: CashAuditSchema_All):
    data = body.model_dump()
    cash_id = int(data.get('cash_id'))
    pokemon_obj = db.session.get(CashAudit, cash_id)

    if not pokemon_obj:
        return jsonify({"error": "pokemon não encontrado"}), 404

    for key, value in data.items():
        if hasattr(pokemon_obj, key) and value is not None:
            setattr(pokemon_obj, key, value)

    db.session.commit()

    return jsonify({
        "message": f"Operação Realizada",
        "cash_id": cash_id,
    })


@cash_audit_api.delete('', tags=[cash_audit_tag],responses={"200": CashAuditSchema_PrimaryKey, "422": ValidationErrorResponse},
         summary="Requisição para deletar um pokemons de um usuário")
def delete_cash_audit(body: CashAuditSchema_PrimaryKey):
    data = body.model_dump()
    cash_id = int(data.get('cash_id'))
    pokemon_obj = db.session.get(CashAudit, cash_id)

    if not pokemon_obj:
        return jsonify({"error": "Pokemon não encontrado"}), 404

    db.session.delete(pokemon_obj)
    db.session.commit()

    return jsonify({
        "message": f"Operação Realizada",
        "cash_id": cash_id,
    })
