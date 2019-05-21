import sqlite3
import csv
import pandas as pd


#creates or opens a file called icrisat.db with a SQLite3 DB
db = sqlite3.connect('icrisa.db')

#When we are done working with the DB we need to close the connection:



cursor = db.cursor()

cursor.execute('''
    create table Groups(G_Number,G_Descr,G_Food_Code,G_Food_Descr)
''')


df = pd.read_csv(r'/Users/junxiaoshen/Documents/GitHub/ICRISAT-backend/Groups.csv')
df.to_sql('Groups', db, if_exists='append', index=False)

db.commit()
db.close()

#cursor.execute('''.mode csv''')

#cursor.execute('''import Recipes.csv recipes''')


#cursor.execute('''select ingr_code from recipes''')
