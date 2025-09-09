#para rodar esse teste => python -m pytest backend/test/user_bag_test.py -v

import pytest
from ..app import app, db
from ..table.user_bag import UserBag
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
def test_add_user_bag(client):
    user = AccountUser(login="atualizar", password="1234", role="user", name ="test")
    db.session.add(user)
    db.session.commit()
    user_id = user.user_id  # pegar ID

    response = client.post( "/user_bag", json={"operation": "input", "user_id": user_id,"item_id":1,"pokemon_id": 0})
    assert response.status_code == 200


# ---------------- Teste GET ----------------
def test_get_all_user_bag(client):
    with app.app_context():
        bag = UserBag(item_id=1, user_id=1, pokemon_id= 1,operation = "input")
        db.session.add(bag)
        db.session.commit()

    response = client.get("/user_bag")  # barra no final
    assert response.status_code == 200

# ---------------- Teste PUT ----------------
def test_update_user_bag(client):
    with app.app_context():
        bag = UserBag(item_id=1, user_id=1, pokemon_id="",operation = "input")
        db.session.add(bag)
        db.session.commit()
        bag_id = bag.bag_id  # pegar ID

    # Usar somente o ID na requisição
    response = client.put("/user_bag",json={"bag_id":bag_id ,"operation": "input", "user_id": 1,"item_id":1,"pokemon_id":1})
    assert response.status_code == 200

# ---------------- Teste DELETE ----------------
def test_delete_user_bag(client):
    # Criar usuário no contexto do app
    with app.app_context():
        bag = UserBag(item_id=1, user_id=1, pokemon_id="",operation = "input")
        db.session.add(bag)
        db.session.commit()
        bag_id = bag.bag_id  # pegar ID

    # Usar somente o ID na requisição
    response = client.delete("/user_bag", json={"bag_id": bag_id})
    assert response.status_code == 200