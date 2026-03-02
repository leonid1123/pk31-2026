from flask import Flask
from flask import render_template
from flask import request
import pymysql.cursors

app = Flask(__name__)

conn = pymysql.connect(host='127.0.0.1',
                       user='pk31',
                       password='1234',
                       database='pk31_processors')
cur = conn.cursor()


@app.route("/", methods=['GET', 'POST'])
def main_page():
    if request.method == 'POST': #нужно поискать в словаре
        btn1 = request.form['sort_up']
        btn2 = request.form['sort_down']
        print(btn1, btn2)
    cur.execute('SELECT model, manufacturer, price FROM processors')
    ans = cur.fetchall()
    return render_template('index.html', ans=ans)


if __name__ == "__main__":
    app.run(debug=True)


