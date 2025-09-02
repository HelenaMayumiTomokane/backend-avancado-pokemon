from flask import request, redirect, render_template
from flask_cors import CORS
from flask_openapi3 import OpenAPI, Info, Tag
from .config import DevelopmentConfig
from .database import db
from .error_schema import register_validation_error_handler

# Importa os módulos de rotas
from .apis.account_user_api import account_user_api

info = Info(
    title="Minha API de Amigurumi",
    version="1.0.0",
    description="API para gerenciar informações dos Amigurumis"
)

app = OpenAPI(__name__, info=info)
CORS(app)

# Configurações do banco
app.config.from_object(DevelopmentConfig)
db.init_app(app)

with app.app_context():
    db.create_all()

register_validation_error_handler(app)

# Registro das APIs
app.register_api(account_user_api)



if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000, use_reloader=True)