#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#from py import primos
from flask import Flask, request, render_template
from flask.wrappers import Response
from py.primos import generaPrimos
import git


app = Flask(__name__)

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

@app.route('/primos')
def primos():
  n=200
  return render_template("primos.html", lista=generaPrimos(n))

if __name__=="__main__":
  app.run(debug=True)