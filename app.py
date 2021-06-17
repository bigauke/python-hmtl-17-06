from flask import Flask
#cria um objeto
app = Flask(__name__)

#registra uma rota
@app.route('/')

#chama a função index
def index():
    return "HELLO WORLD!!"


