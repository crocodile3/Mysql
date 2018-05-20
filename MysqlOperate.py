# -*- coding:utf-8 -*-
from threading import Thread

import pymysql
import time


class Mysql():
    def __init__(self,host,user,passwd,db,port=3306):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.db = db
        self.port = port
        self.connect()

    def connect(self):
        self.conn = pymysql.connect(host = self.host, user = self.user, passwd = self.passwd, db = self.db, port = self.port)
        self.cursor = self.conn.cursor()

    def execute(self,sql):
        result = self.cursor.execute(sql)
        return result

    def query(self,sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

    def scaler(self,sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        return result[0]

    def one(self,sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        return result

    def __del__(self):
        self.cursor.close()
        self.conn.close()



result = []
class MyThread(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        global result
        conn = Mysql('localhost','root','mysql','goods')
        result.append(conn.scaler("select sql_no_cache count(`id`) from `data_" + str(self.no) +"` where `title` like '%hello%'"))

def task():
    thr1 = MyThread()
    thr2 = MyThread()
    thr3 = MyThread()
    thr4 = MyThread()

    thr1.start()
    thr2.start()
    thr3.start()
    thr4.start()

    thr1.join()
    thr2.join()
    thr3.join()
    thr4.join()

    return True

if __name__ == "__main__":

    print ""
    print "...... multi thread query start ......"
    print time.ctime() + ' / ' + str(time.time())
    task()
    print result
    print time.ctime() + ' / ' + str(time.time())
    print "...... multi thread query end ......"

    print ""
    dbCon = Mysql('localhost', 'root', '123456', 'mydb')
    print "...... single thread query start ......"
    print time.ctime() + ' / ' + str(time.time())
    print dbCon.scaler("select sql_no_cache count(`id`) from `data` where `title` like '%hello%'")
    print time.ctime() + ' / ' + str(time.time())