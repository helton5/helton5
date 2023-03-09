# tem um novo import aqui: request
from flask import Flask, jsonify, request
from flask_cors import CORS
from pessoa import *

app = Flask(__name__)
with app.app_context():
    CORS(app)

    @app.route("/")
    def ola():
        return "operação post"

    # rota de listar pessoas
    @app.route("/incluir_pessoa", methods=['POST'])
    def incluir():
        # receber as informações da nova pessoa
        dados = request.get_json() #(force=True) dispensa Content-Type na requisição
        try: # tentar executar a operação
            nova = Pessoa(**dados) # criar a nova pessoa

            # faz a persistência da nova pessoa... :-/ em breve :-p

            return jsonify({"resultado":"ok"})
        except Exception as e: # em caso de erro...
            # informar mensagem de erro
            return jsonify({"resultado":"erro"})
    
    app.run(debug=True)

    # para depurar a aplicação web no VSCode, é preciso remover debug=True
    # https://stackoverflow.com/questions/17309889/how-to-debug-a-flask-app

'''
* resultado da invocação ao servidor:

$ curl localhost:5000/incluir_pessoa -X POST -d '{"nome":"John Stick", "email":"jostick@gmail.com","telefone":"47 9 9222 1234"}' -H "Content-Type:application/json"
{
  "resultado": "ok"
}

* se esquecer de dizer que é POST, funciona também, 
porque ele já assume que é POST, 
pois você está enviando dados

$ curl localhost:5000/incluir_pessoa -d '{"nome":"John Stick", "email":"jostick@gmail.com","telefone":"47 9 9222 1234"}' -H "Content-Type:application/json"
{
  "resultado": "ok"
}

* agora, se esquecer o contenttype, aí dá ruim...

$ curl localhost:5000/incluir_pessoa -d '{"nome":"John Stick", "email":"jostick@gmail.com","telefone":"47 9 9222 1234"}'
<!doctype html>
<html lang=en>
<title>400 Bad Request</title>
<h1>Bad Request</h1>
<p>Did not attempt to load JSON data because the request Content-Type was not &#39;application/json&#39;.</p>

* se enviar nome de campo errado (telefoneABC em vez de telefone), olha lá o erro...

$ curl localhost:5000/incluir_pessoa -X POST -d '{"nome":"John Stick", "email":"jostick@gmail.com","telefoneABC":"47 9 9222 1234"}' -H "Content-Type:application/json"
{
  "resultado": "erro"
}

'''
