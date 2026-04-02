from flask import (Flask,
                   request,
                   render_template, redirect, url_for)
import pymysql.cursors
from db_handler import DB_handler
app = Flask(__name__)
db = DB_handler()
USER = {}

@app.route("/", methods=['POST', 'GET'])
def main_app():
    USER.clear()
    msg = ''
    mode = 'none'
    color = ''
    if request.method == 'POST':
        login = request.form.get('login')
        nik = request.form.get('nik')
        pass1 = request.form.get('pass1')
        pass2 = request.form.get('pass2')
        if login and nik and pass1 and pass2 and pass1==pass2:
            sql='SELECT * FROM users WHERE nik=%s'
            db.cur.execute(sql,(nik,))
            if db.cur.fetchone() is None:
                sql = 'INSERT INTO users(login, password, nik) VALUES(%s,%s,%s)'
                info = (login,pass1,nik)
                db.cur.execute(sql,info)
                db.conn.commit()
                msg = 'Регистрация прошла успешно!'
                mode = 'block'
                color = 'w3-green'
            else:
                msg = 'Такой ник занят'
                mode = 'block'
                color = 'w3-yellow'
        else:
            msg = 'Нужно заполнить все поля и повторить пароль!'
            mode = 'block'
            color = 'w3-yellow'
    return render_template("reg.html", msg=msg, mode=mode, color=color)

@app.route('/login', methods=['POST','GET'])
def login_handler():
    USER.clear()
    login = request.form.get('login')
    password = request.form.get('password')
    sql = 'SELECT * FROM users WHERE login=%s AND password=%s'
    db.cur.execute(sql,(login,password))
    ans = db.cur.fetchone()
    if ans:
        USER['nik'] = ans[1]
        return redirect(url_for('msg_handler'))
    else:
        return render_template("login.html")


@app.route('/msg', methods=['POST','GET'])
def msg_handler():
    if 'nik' in USER:
        return render_template("index.html",
                           user=USER['nik'])
    else:
        return redirect(url_for('main_app'))


app.run(debug=True)
