#para rodar esse teste => python -m pytest backend/test/cash_audit_test.py -v

import pytest
from ..app import app, db
from ..table.cash_audit import CashAudit
from ..table.account_user import AccountUser



# ---------------- Fixture para cliente de teste ----------------
@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # banco temporário
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    with app.app_context():
        db.create_all()  # cria tabelas temporárias

        with app.test_client() as client:
            yield client  # o teste roda dentro deste contexto

        db.drop_all()  # remove tabelas após teste

# ---------------- Teste POST ----------------
def test_add_cash_audit(client):
    user = AccountUser(login="atualizar", password="1234", role="user", name ="test")
    db.session.add(user)
    db.session.commit()
    user_id = user.user_id  # pegar ID

    response = client.post( "/cash_audit", json={"operation_type": "input", "user_id": user_id,"value":1})
    assert response.status_code == 200


# ---------------- Teste GET ----------------
def test_get_all_cash_audit(client):
    with app.app_context():
        cash = CashAudit(value=1, user_id=1,operation_type = "input")
        db.session.add(cash)
        db.session.commit()
        user_id = cash.user_id  # pegar ID

    response = client.get(f"/cash_audit/user_id?user_id={user_id}")  # barra no final
    assert response.status_code == 200

# ---------------- Teste PUT ----------------
def test_update_cash_audit(client):
    with app.app_context():
        cash = CashAudit(value=1, user_id=1, operation_type = "input")
        db.session.add(cash)
        db.session.commit()
        cash_id = cash.cash_id  # pegar ID

    # Usar somente o ID na requisição
    response = client.put("/cash_audit",json={"cash_id":cash_id ,"operation_type": "input", "user_id": 1,"value":1})
    assert response.status_code == 200

# ---------------- Teste DELETE ----------------
def test_delete_cash_audit(client):
    # Criar usuário no contexto do app
    with app.app_context():
        cash = CashAudit(value=1, user_id=1, operation_type = "input")
        db.session.add(cash)
        db.session.commit()
        cash_id = cash.cash_id  # pegar ID

    # Usar somente o ID na requisição
    response = client.delete("/cash_audit", json={"cash_id": cash_id})
    assert response.status_code == 200