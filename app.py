from flask import Flask, request, render_template
from flask.wrappers import Response
import git

app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")
