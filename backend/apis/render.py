from flask import request, render_template, redirect
from flask_openapi3 import Tag

# Definição da tag de documentação
support_tag = Tag(name="suporte", description="Endpoint para geração da documentação dos APIs")

def register_support_routes(app):
   
    # renderização de novas abas
    @app.get('/<page>', tags=[support_tag])  
    def render_page(page):
        try:
            return render_template(f'{page}.html')
        except:
            return "Página não encontrada", 404


