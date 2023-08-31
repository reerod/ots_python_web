from flask import Flask

app = Flask("meu app")

@app.route('/') # criando rota para o app
def hello():
    return "Hello World"

@app.route('/novo')
def novo():
    return "<h1> Nova Página </h1>"
