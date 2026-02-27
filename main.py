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
    cur.execute('SELECT model, manufacturer, price FROM processors')
    ans = cur.fetchall()
    print(ans)
    return render_template('index.html', ans=ans)


if __name__ == "__main__":
    app.run(debug=True)


