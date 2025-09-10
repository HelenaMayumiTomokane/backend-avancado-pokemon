from flask import render_template

def register_support_routes(app):
    # renderização de novas abas
    @app.get('/<page>')  
    def render_page(page):
        try:
            return render_template(f'{page}.html')
        except:
            return "Página não encontrada", 404


