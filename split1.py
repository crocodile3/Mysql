# -*- coding:utf-8 -*
import re

import pymysql
import json
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def split(field_name):
    try:
        con = pymysql.connect(host="127.0.0.1", user="root", passwd="admin@1218pingan.cn", db="qichacha", port=3306,
                              charset='utf8')
        cur = con.cursor()
        sql = "select {} from t2_qichacha limit 10;".format(field_name)
        cur.execute(sql)
        data_tuple = cur.fetchall()
        # data_str = str(data_tuple).encode("utf8").decode("unicode_escape")
        # print(data_str)
        # print data.decode('utf8')
        # 6.关闭cursor
        cur.close()
        # 7.关闭connection
        con.close()
        # print data_str
        for row in list(data_tuple):
            if field_name == "g_mail":
                old = row[0]
                list1 = old.split(" ")
                print list1
                g_mail = list1[1]
                g_web = list1[-1]
                print g_mail
                print g_web

            if field_name == "gs_sockinfo":
                lines = row[0]
                if lines is not None:
                    pt = re.compile(r"#(.*?)东")
                    group = pt.findall(lines)
                    for line in group:
                        line = line.strip()
                        # print line
                        item = line.split("|")
                        queries = item[0]
                        list1 = queries.split(" ")
                        query = list1[0]
                        StockName = list1[2]
                        CompLinkNum = list1[4]
                        # print query
                        # print StockName
                        # print  CompLinkNum
                        CapiRate = item[1].strip()
                        Unit = item[3].strip()
                        # StockType = item[-1].replace(" ","").replace("-","")
                        item6 = item[-1].replace(" ", "")
                        # print item6
                        m = re.search(r"\d{4}-\d{2}-\d{2}", item6)
                        if m is not None:
                            ShoudDate = item6[0:10]
                            StockType = item6[10:]
                            print StockType
                            print ShoudDate
                        else:
                            ShoudDate = "-"
                            StockType = item6.replace("-", "")
                        print query
                        print CapiRate
                        print Unit
                        print StockType
                        print ShoudDate

            if field_name == "gs_member":
                pass

            if field_name == "gs_changelist":
                pass

    except Exception as e:
        print(e)


if __name__ == '__main__':
    field_name = "gs_sockinfo"
    split(field_name)
