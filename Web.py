from flask import Flask, jsonify,render_template,request , redirect, session,flash
from pymongo import MongoClient as mc
from customer import Customer
from User import User

app = Flask(__name__)

app.secret_key = "Tesla2000"


dbclient = mc('127.0.0.1',27017)
db = dbclient.Flask

@app.route("/login")
def login():
   return render_template("login.html", titulo = "Login")

@app.route("/")
def index():
    print(session)
    if 'usuário_logado' not in session or session['usuário_logado'] == None:
        return  redirect("/login")
    return render_template("index.html",titulo="Inicio")

@app.route("/index")
def inicio():
    if 'usuário_logado' not in session or session['usuário_logado'] == None:
        return  redirect("/login")
    return jsonify({"message":"PROGRAMA BASEADO EM FLASK/MONGO, CADASTRANTO DIVERSOS USUÁRIOS!!"})

@app.route("/listaCliente")
def listaCliente():
    if 'usuário_logado' not in session or session['usuário_logado'] == None:
        return  redirect("/login")
    listaDeCliente = []
    documentoCliente = db.flask.find()
    for dc in documentoCliente:
        listaDeCliente.append(Customer(dc["nome"],dc["email"],dc["telefone"]))

    return render_template("listaCliente.html", listaCliente=listaDeCliente , titulo ="Lista de cliente" )

@app.route("/criaCliente")
def criaCliente():
    if 'usuário_logado' not in session or session['usuário_logado'] == None:
        return  redirect("/login")
    return render_template("criaCliente.html",titulo = "Criacao de cliente")

@app.route("/autenticar", methods = ["Post",])
def autenticar():
    user = User(user_name=request.form["usuario"],password=request.form["senha"])
    print(user.user_name)
    print(user.password)
    dc = db.userapp.find_one(user.getUserMongo())
    print(type(dc))
    if  user.autentificar(user.password,dc):
        session['usuário_logado'] = request.form["usuario"]
        flash(request.form["usuario"]+" logou com sucesso!!!" )
        return redirect('/')
    else:
        flash("Usuário não logado")
        return redirect('/login')

@app.route("/criar", methods = ["Post",])
def criar():
    cliente = Customer(nome = request.form["nome"], email=request.form["email"],telefone=request.form["telefone"])
    db.flask.insert_one(cliente.geraDocumento())

    return ("<h1> Valor adicionado <h1>"
            "<a href='/'>Voltar</a>")

@app.route("/logout")
def logout():
    session["usuário_logado"] = None
    return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True)


