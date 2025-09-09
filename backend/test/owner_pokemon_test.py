#para rodar esse teste => python -m pytest backend/test/owner_pokemon_test.py -v

import pytest
from ..app import app, db
from ..table.owner_pokemon import OwnerPokemon
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
def test_add_owner_pokemon(client):
    user = AccountUser(login="atualizar", password="1234", role="user", name ="test")
    db.session.add(user)
    db.session.commit()
    user_id = user.user_id  # pegar ID

    response = client.post( "/owner_pokemon/", json={"pokemon_id_external_api": 1, "user_id": user_id,"pokemon_name":"test" })
    assert response.status_code == 200


# ---------------- Teste GET ----------------
def test_get_all_owner_pokemon(client):
    with app.app_context():
        pokemon = OwnerPokemon(pokemon_id_external_api=1, user_id=1, pokemon_name="teste")
        db.session.add(pokemon)
        db.session.commit()

    response = client.get("/owner_pokemon")  # barra no final
    assert response.status_code == 200


# ---------------- Teste PUT ----------------
def test_update_owner_pokemon(client):
    with app.app_context():
        pokemon = OwnerPokemon(pokemon_id_external_api=1, user_id=1, pokemon_name="test")
        db.session.add(pokemon)
        db.session.commit()
        pokemon_id = pokemon.pokemon_id  # pegar ID

    # Usar somente o ID na requisição
    response = client.put("/owner_pokemon/",json={"pokemon_id": pokemon_id,"pokemon_id_external_api": 1, "user_id": 1,"pokemon_name":"test" })
    assert response.status_code == 200

# ---------------- Teste DELETE ----------------
def test_delete_owner_pokemon(client):
    # Criar usuário no contexto do app
    with app.app_context():
        pokemon = OwnerPokemon(pokemon_id_external_api=1, user_id=1, pokemon_name="test")
        db.session.add(pokemon)
        db.session.commit()
        pokemon_id = pokemon.pokemon_id  # pegar ID

    # Usar somente o ID na requisição
    response = client.delete(
        "/owner_pokemon/",
        json={"pokemon_id": pokemon_id}
    )
    assert response.status_code == 200