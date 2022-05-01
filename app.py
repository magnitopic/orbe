#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#from py import primos
from flask import Flask, request, render_template, jsonify
from flask.wrappers import Response
from py.prime import makePrime
from galton import galtonboard as galton
from petrol import getPetrolPrice
import git  # GitPython library
import os


app = Flask(__name__)

# Route for the GitHub webhook


@app.route('/git_update', methods=['POST'])
def git_update():
    repo = git.Repo('./orbe')
    origin = repo.remotes.origin
    repo.create_head('main',
                     origin.refs.main).set_tracking_branch(origin.refs.main).checkout()
    origin.pull()
    return '', 200


@app.route('/')
def index():
    print(os.getcwd())
    return render_template("index.html")


@app.route('/api1')
def api1():
    # JSON can be returned directlly like so:
    return jsonify({"clave": "valor"})


@app.route('/api2')
def api2():
    # Or you can open a JSON file and serve it's contents
    file = open("./api/test.json", "rt", encoding="utf-8")
    archivoJson = file.readlines()
    file.close()
    print(archivoJson)
    return jsonify(archivoJson)


@app.route('/prime', methods=["GET", "POST"])
def primos():
    if request.method == 'POST':
        n = request.form["number"]
        return render_template("prime.html", list=makePrime(int(n)), title="First "+n+" prime numbers")
    else:
        return render_template("prime.html", list="", title="First prime numbers")


@app.route('/galton', methods=["GET", "POST"])
def glaton():
    if ((request.method == 'POST') and (request.form["number"] != "") and (int(request.form["number"]) > 1)):
        result = galton(int(request.form["number"]))
        print(result[1])
        return render_template("galton.html", structure=result[0], URL=result[1])
    else:
        return render_template("galton.html", URL="")


@app.route("/petrol", methods=["GET"])
def petrol():
    return render_template("petrol.html", petrolPrice="", provincia="")


@app.route("/petrol/<provincia>/<producto>", methods=["GET"])
def petrolPrice(provincia, producto):
    return render_template("petrol.html", petrolPrice=getPetrolPrice(provincia, producto), provincia=provincia)


if __name__ == "__main__":
    app.run(debug=True)
