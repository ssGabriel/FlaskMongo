from flask import Flask, jsonify,render_template,request
from customer import Customer

app = Flask(__name__)


listaDeCliente = []
print(type(listaDeCliente))

@app.route("/")
def index():
    return ("<a href='/index'>Inicio</a>"
            "<h1></h1>"
            "<a href='/criaCliente'>Cria Cliente</a>"
            "<h1></h1>"
            "<a href='listaCliente'>Lista de Cliente</a>")

@app.route("/index")
def inicio():
    return jsonify({"message":"Hello Json!"})

@app.route("/listaCliente")
def listaCliente():
    return render_template("listaCliente.html", listaCliente=listaDeCliente)

@app.route("/criaCliente")
def criaCliente():
    return render_template("criaCliente.html")

@app.route("/criar", methods = ["Post",])
def criar():
    cliente = Customer(nome = request.form["nome"], email=request.form["email"],telefone=request.form["telefone"])
    listaDeCliente.append(cliente)
    return ("<h1> Valor adicionado <h1>"
            "<a href='/'>Voltar</a>")


if __name__ == '__main__':
    app.run(debug=True)


