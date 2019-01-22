from flask import Flask, render_template, request
import requests



app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


# @app.route('/boxoffice')
# def get_rank():

#     return render_template('boxoffice.html',rank_mv=rank_mv)
