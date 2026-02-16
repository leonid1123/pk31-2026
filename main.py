from flask import Flask
from flask import render_template
from flask import request


app=Flask(__name__)
@app.route("/", methods=['POST','GET'])
def hello_world():
    if request.method == 'POST':
        new_food = request.form['food']
        new_price = request.form['price']
        return render_template('index.html', food=new_food ,price=new_price)
    return render_template('index.html')
