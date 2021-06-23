#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#from py import primos
from flask import Flask, request, render_template
from flask.wrappers import Response
from py.prime import makePrime
from py.glaton import galtonboard
import git


app = Flask(__name__)

#Route for the GitHub webhook
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
  return render_template("index.html")

@app.route('/prime', methods=["GET","POST"])
def primos():
  if request.method == 'POST':
    n=request.form["number"]
    return render_template("prime.html", list=makePrime(int(n)), title="First "+n+" prime numbers")
  else:
    return render_template("prime.html", list="", title="First prime numbers")

@app.route('/galton', methods=["GET","POST"])
def glaton():
  if request.method=='POST':
    result=galtonboard(int(request.form["number"]))
    print(result)
    return render_template("galton.html",structure=result[0],URL=result[1])
  else:
    return render_template("galton.html")

if __name__=="__main__":
  app.run(debug=True)