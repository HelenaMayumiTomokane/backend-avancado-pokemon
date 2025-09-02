from flask import request, redirect
from flask_openapi3 import Tag

openapi_tag = Tag(name="openapi", description="Rotas para documentação OpenAPI")

def register_openapi_routes(app):
    @app.get('/openapi', tags=[openapi_tag])
    def openapi():
        doc_type = request.args.get('doc', 'swagger') 

        if doc_type == 'redoc':
            return redirect("/redoc")
        
        elif doc_type == 'rapidoc':
            return redirect("/rapidoc")
        
        elif doc_type == 'swagger':
            return redirect("/swagger")
        
        elif doc_type == 'scalar':
            return redirect("/scalar")
        
        elif doc_type == 'rapipdf':
            return redirect("/rapipdf")
        
        elif doc_type == 'elements':
            return redirect("/elements")
