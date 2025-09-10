# Dockerfile do backend
FROM python:3.11-slim

WORKDIR /app

# Copia o requirements.txt
COPY requirements.txt .

# Instala dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o pacote pokemon
COPY pokemon/ pokemon/

# Expor porta do Flask
EXPOSE 5000

# Rodar como módulo
ENV FLASK_APP=app.py
ENV FLASK_ENV=development
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]

