#para rodar esse teste => python -m pytest backend/test/account_user_test.py -v

import pytest
from ..app import app, db
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
def test_add_user(client):
    response = client.post( "/account_user/", json={"login": "novo_user", "password": "abcd", "role": "user", "name":"test" })
    assert response.status_code == 200
    data = response.get_json()
    assert "message" in data
    assert data["user_id"] > 0


# ---------------- Teste GET ----------------
def test_get_all_user(client):
    with app.app_context():
        user = AccountUser(login="teste", password="1234", role="user", name ="test")
        db.session.add(user)
        db.session.commit()

    response = client.get("/account_user/")  # barra no final
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 1
    assert data[0]['login'] == "teste"


# ---------------- Teste PUT ----------------
def test_update_user(client):
    with app.app_context():
        user = AccountUser(login="atualizar", password="1234", role="user", name ="test")
        db.session.add(user)
        db.session.commit()
        user_id = user.user_id  # pegar ID

    # Usar somente o ID na requisição
    response = client.put("/account_user/", json={"user_id": user_id, "login": "atualizado", "password": "4321", "role": "admin", "name": "test"})
    assert response.status_code == 200
    data = response.get_json()
    assert data["message"] == f"Usuário {user_id} atualizado com sucesso!"



# ---------------- Teste DELETE ----------------
def test_delete_user(client):
    # Criar usuário no contexto do app
    with app.app_context():
        user = AccountUser(login="atualizar", password="1234", role="user", name="test")
        db.session.add(user)
        db.session.commit()
        user_id = user.user_id  # pegar ID

    # Usar somente o ID na requisição
    response = client.delete("/account_user/",json={"user_id": user_id})
    assert response.status_code == 200
    data = response.get_json()
    # Corrigido para a mensagem real da API
    assert data["message"] == f"Usuário {user_id} removido com sucesso!"
