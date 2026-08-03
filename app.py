from flask import Flask

app = Flask(__name__)


@app.route("/")
def accueil():
    return "Bonjour ! Mon API DevOps fonctionne."


def additionner(a, b):
    return a - b


@app.route("/calcul")
def calcul():
    resultat = additionner(2, 3)
    return f"2 + 3 = {resultat}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)