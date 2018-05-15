import demo
import numpy as np
from lightfm.datasets import fetch_movielens
from lightfm import LightFM
import pandas as pd
import sqlite3
import pandas as pd

#db = pd.read_csv('users.txt',sep = '|',header=None)
#
#print (db[1][0])
#
#data = fetch_movielens(min_rating=4.0)
#
#print(repr(data['train']))
#print(repr(data['test']))
#
#model = LightFM(loss='warp')
#
#model.fit(data['train'], epochs=30, num_threads=2)
#
#know_of_ml = np.empty((943, 10), dtype='U100')
#rec_of_ml = np.empty((943, 10), dtype='U100')
#
#for i in range(943):
#    know_of_ml[i], rec_of_ml[i] = demo.sample_recommendation(model, data, [i])

conn = sqlite3.connect('db.sqlite3')

c = conn.cursor()



#objectives = pd.read_sql('select * from auth_user',conn)
#
#objectives2 = pd.read_sql("SELECT name FROM db.sqlite3 WHERE type='table'", conn)

#password = 'pbkdf2_sha256$100000$ne5voLYrJRcd$3ZkezWgFcSIkfuv5pDi5BGjsRby4cg/eGYbgSSKO9ZI='
#
#user = 'user'
#
#count = 1
#
#is_superuser = '1'
#
#is_staff = '1'
#
#email = '778337607@qq.com'
#
#first_name = ' '
#
#last_name = ' '
#
#is_active = '1'
#
#date_joined = ' '
#
#for i in range(943):
#    
#    name = user + str(count)
#    count+=1
#    c.execute("insert into auth_user (password,is_superuser,username,email,is_staff,is_active, first_name,last_name,date_joined) values  (?,?,?,?,?,?,?,?,?)", (password, is_superuser, name,email,is_staff,is_active,first_name,last_name,date_joined))
#
#conn.commit()
#
#conn.close()

#res = c.execute("SELECT name FROM sqlite_master WHERE type='table';")
#for name in res:
#    print (name[0])


