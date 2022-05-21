#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# from py import primos
from flask import Flask, request, render_template, jsonify
from flask.wrappers import Response
from jinja2 import Undefined
from py.prime import makePrime
from galton import galtonboard
from petrol import getPetrolPrice, getProvinces, getFuels
from stocks import getStockPrice
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


@app.route('/prime/', methods=["GET", "POST"])
def primos():
    if request.method == 'POST':
        n = request.form["number"]
        return render_template("prime.html", list=makePrime(int(n)), title="First "+n+" prime numbers")
    else:
        return render_template("prime.html", list="", title="First prime numbers")


@app.route('/galton/', methods=["GET", "POST"])
def glaton():
    if ((request.method == 'POST') and (request.form["number"] != "") and (int(request.form["number"]) > 1)):
        result = galtonboard(int(request.form["number"]))
        return render_template("galton.html", structure=result[0], URL=result[1])
    else:
        return render_template("galton.html", URL="")


@app.route("/petrol/", methods=["GET"])
def petrol():
    # default pyload values
    pyload = {
        "provinceList": getProvinces(),
        "fuelList": getFuels(),
        "province": "",
        "fuel": "",
        "petrolPrice": "",
        "direccion": "",
    }

    # TODO: check if request.args province and fuel have values
    if len(request.args) == 2:
        # Valid or invalid province
        pyload["province"] = request.args['provincia']
        # Valid or invalid fuel
        pyload["fuel"] = request.args['combustible']
        pyload["petrolPrice"] = getPetrolPrice(pyload["province"], pyload["fuel"])[
            "price"]    # price value if valid, None if not
        pyload["direccion"] = getPetrolPrice(pyload["province"], pyload["fuel"])[
            "direccion"]     # address if valid, None if not

    """ province and fuel lists are always returned
        province and fuel can be empty("") or have the value passed in args(witch can be valid or not)
        petrolPrice and direction can be empty(""), None or have correct values """
    return render_template("petrol.html", pyload=pyload)


@app.route("/stocks/", methods=["GET"])
def stocks():
    price = getStockPrice("TSLA")
    return render_template("stocks.html", price=price)


if __name__ == "__main__":
    app.run(debug=True)
    """  app.run(host='0.0.0.0', port=80) """
