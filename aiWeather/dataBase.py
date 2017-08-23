#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql

def getConn():
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='weather')
    return conn

def getCur():
    cur = getConn().cursor()
    return cur

#--查询
def selectSql(sql):
    cur=getCur()
    cur.execute(sql)#"SELECT count(1) FROM weather"
    for r in cur.fetchall():
        print(r)
    getConn().close()

#--插入
def insertSql(sql):
    cur=getCur()
    try:
        cur.execute(sql)
        getConn().commit()
    except:
        getConn().rollback()
    getConn().close()

# selectSql("SELECT count(1) FROM weather")
