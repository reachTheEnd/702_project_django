import demo
import numpy as np
from lightfm.datasets import fetch_movielens
from lightfm import LightFM
import pandas as pd
import sqlite3
import pandas as pd

conn = sqlite3.connect('db.sqlite3')

c = conn.cursor()

#db = pd.read_sql('select * from auth_user',conn)
#


db = pd.read_csv('users.txt',sep = '|',header=None)

print (db[1][0])

data = fetch_movielens(min_rating=4.0)

print(repr(data['train']))
print(repr(data['test']))

model = LightFM(loss='warp')

model.fit(data['train'], epochs=30, num_threads=2)

know_of_ml = a = np.empty((943, 10), dtype='U100')
rec_of_ml = np.empty((943, 10), dtype='U100')

for i in range(943):
    know_of_ml[i], rec_of_ml[i] = demo.sample_recommendation(model, data, [i])


