import sqlite3
import csv
import pandas as pd


#creates or opens a file called icrisat.db with a SQLite3 DB
db = sqlite3.connect('icrisat.db')

#When we are done working with the DB we need to close the connection:



cursor = db.cursor()

cursor.execute('''
    create table ConvFactors(conv_codetype,conv_foodcode,conv_food_descr,conv_method,conv_method_descr,conv_stdvol,conv_stdvol_descr,conv_size,conv_size_descr,conv_factor,conv_unit,conv_unit_descr,conv_nobs,conv_source,conv_source_descr,,,,source2 (Mourad))
''')


df = pd.read_csv(r'/Users/junxiaoshen/Documents/GitHub/ICRISAT-backend/ConvFactors.csv')
df.to_sql('ConvFactors', db, if_exists='append', index=False)

db.commit()
db.close()

#cursor.execute('''.mode csv''')

#cursor.execute('''import Recipes.csv recipes''')


#cursor.execute('''select ingr_code from recipes''')
