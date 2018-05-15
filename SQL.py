import sqlite3
import pandas as pd

conn = sqlite3.connect('db.sqlite3')

c = conn.cursor()

db = pd.read_sql('select * from auth_user',conn)
#
var1 = 'pbkdf2_sha256$100000$ne5voLYrJRcd$3ZkezWgFcSIkfuv5pDi5BGjsRby4cg/eGYbgSSKO9ZI='
var2 = '1'
var3 = 'test100'
var4 = 'joe4'
var5 = 'black'
var6 = '778337607@qq.com'
var7 = '1'
var8 = '1'
var9 = '2018-05-02 00:45:11.377323'

c.execute("insert into auth_user (password,is_superuser,username,first_name,last_name,email,is_staff,is_active,date_joined) values  (?,?,?,?,?,?,?,?,?)", (var1, var2, var3,var4,var5,var6,var7,var8,var9))
#c.execute("insert into auth_user (password,is_superuser,username,first_name,last_name,email,is_staff,is_active,date_joined) values ('pbkdf2_sha256$100000$nUaEBMCs4Ai5$wMLFBbuGxfn1L3zlhnB1/hCGWjfqWl7JxMS0yt+S/fE=','1','test2','joe3','fuck','778337607@qq.com','1','1','2018-05-02 00:45:11.377323');")




conn.commit()

conn.close()