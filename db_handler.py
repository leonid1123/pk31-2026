import pymysql.cursors


class DB_handler:
    def __init__(self):
        self.conn = pymysql.connect(
            host='192.168.1.61',
            user='pk31',
            password='1234',
            database='pk31_msg'
        )
        self.cur = self.conn.cursor()
