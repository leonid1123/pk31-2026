from flask import Flask
from flask import render_template
from flask import request
import pymysql.cursors
import os

app = Flask(__name__)
PROC_FOLDER = os.path.join('static', 'img')

conn = pymysql.connect(host='127.0.0.1',
                       user='pk31',
                       password='1234',
                       database='pk31_processors')
cur = conn.cursor()


def get_manufacturers():
    man_list = []
    cur.execute("SELECT DISTINCT manufacturer FROM processors")
    ans = cur.fetchall()
    for item in ans:
        man_list.append(item[0])
    return man_list


@app.route("/", methods=['GET', 'POST'])
def main_page():
    ans = None
    if request.method == 'POST': #нужно поискать в словаре
        if 'sort_up' in request.form:
            print('по возрастанию')
            cur.execute('SELECT model, manufacturer, price FROM processors ORDER BY price DESC')
            ans = cur.fetchall()
        if 'sort_down' in request.form:
            print('по убыванию')
            cur.execute('SELECT model, manufacturer, price FROM processors ORDER BY price ASC')
            ans = cur.fetchall()
        if 'filter' in request.form:
            man_selected = request.form.get('manufacturers')
            sql_values = (man_selected,)
            cur.execute('''SELECT model, manufacturer, price 
                FROM processors WHERE manufacturer = %s ''',
                        sql_values)
            ans = cur.fetchall()
        if 'reset' in request.form:
            cur.execute('SELECT model, manufacturer, price FROM processors;')
            ans = cur.fetchall()

    else:
        cur.execute('SELECT model, manufacturer, price FROM processors')
        ans = cur.fetchall()
    return render_template('index.html',
                           ans=ans,
                           man=get_manufacturers())


@app.route('/shop', methods=['POST', 'GET'])
def shop_page():
    return render_template('shop.html')


if __name__ == "__main__":
    app.run(debug=True)


