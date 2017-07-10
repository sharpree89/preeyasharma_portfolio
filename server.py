from flask import Flask, redirect, render_template, request, session, flash
from random import randint

app = Flask(__name__)
app.secret_key = "supersecretkey!"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pizzaparty')
def pizza():
    return render_template('pizza.html')

@app.route('/rpg')
def rpg():
    return render_template('rpg.html')

@app.route('/bakeit')
def bakeit():
    return render_template('bakeit.html')

@app.route('/timely')
def timely():
    return render_template('timely.html')

@app.route('/weather')
def weather():
    return render_template('weather.html')

@app.route('/sqggl')
def sqggl():
    return render_template('sqggl.html')

app.run(debug=True)
