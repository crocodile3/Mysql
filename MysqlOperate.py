# -*- coding:utf-8 -*-
import pymysql

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

