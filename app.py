#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from py.primos import generaPrimos
from flask import Flask, request, render_template
from flask.wrappers import Response
import git

app = Flask(__name__)

@app.route('/update_server', methods=['POST'])
def update_server():
  print(request.json)
  return Response(status=200)

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