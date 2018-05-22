import demo
import numpy as np
from lightfm.datasets import fetch_movielens
from lightfm import LightFM
import pandas as pd
import sqlite3
import pandas as pd

db = pd.read_csv('users.txt',sep = '|',header=None)

item = pd.read_csv('item.txt', sep='|', encoding='latin-1',header=None)


print (item[2][266])


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
#    know_of_ml[i], rec_of_ml[i] = demo.sample_recommendation(model, 
#              data, 
#              [i])

conn = sqlite3.connect('db.sqlite3')

c = conn.cursor()

objectives = pd.read_sql('select * from auth_user',conn)

objectives2 = pd.read_sql('select * from post_user_information', conn)

objectives3 = pd.read_sql('select * from post_movie_information', conn)

for i in range(1682):
    if i == 266:
        pass
        
#        c.execute("insert into post_movie_information (name,website, date) values  (?,?,?)", ("Showtimes for Life of the Party","https://www.imdb.com/title/tt5619332/","12-12-2000"))
        
        
    elif i == 1357:
        pass
    
        
    elif i == 1358:
        pass
        
    else:
        name = item[1][i]
        date = item[2][i]
        
        website=item[4][i]
        
            
            
        c.execute("insert into post_movie_information (name,website, date) values  (?,?,?)", (name,website,date))
        


conn.commit()

conn.close()







#user = 'user'
#
#count = 1
#
#user_id = 6
#
#for i in range(943):
#    
#    name = user + str(count)
#    count+=1
#    user_id += 1
#    
#    age = int(db[1][i])
#    gender = db[2][i]
#    occupation = db[3][i]
#    
#    k1 = know_of_ml[i][0]
#    k2 = know_of_ml[i][1]
#    k3 = know_of_ml[i][2]
#    k4 = know_of_ml[i][3]
#    k5 = know_of_ml[i][4]
#    k6 = know_of_ml[i][5]
#    k7 = know_of_ml[i][6]
#    k8 = know_of_ml[i][7]
#    k9 = know_of_ml[i][8]
#    k10 = know_of_ml[i][9]
#    
#    r1 = rec_of_ml[i][0]
#    r2 = rec_of_ml[i][1]
#    r3 = rec_of_ml[i][2]
#    r4 = rec_of_ml[i][3]
#    r5 = rec_of_ml[i][4]
#    r6 = rec_of_ml[i][5]
#    r7 = rec_of_ml[i][6]
#    r8 = rec_of_ml[i][7]
#    r9 = rec_of_ml[i][8]
#    r10 = rec_of_ml[i][9]
#
#    c.execute("insert into post_user_information (user_id,age,gender,occupation,know_m_1,know_m_2,know_m_3, know_m_4,know_m_5,know_m_6, know_m_7, know_m_8, know_m_9, know_m_10, rec_m_1, rec_m_2, rec_m_3, rec_m_4, rec_m_5, rec_m_6,rec_m_7, rec_m_8,rec_m_9,rec_m_10) values  (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (user_id, age,gender,occupation,k1,k2,k3, k4,k5,k6, k7, k8, k9, k10, r1, r2, r3, r4, r5, r6,r7, r8,r9,r10))






    



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


