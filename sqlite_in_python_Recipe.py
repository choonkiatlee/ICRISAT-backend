import sqlite3
import csv
import pandas as pd


#creates or opens a file called icrisat.db with a SQLite3 DB
db = sqlite3.connect('icrisat.db')

#When we are done working with the DB we need to close the connection:



cursor = db.cursor()

cursor.execute('''
    create table recipes(recipe_code,  recipe_descr,
    recipe_type, recipe_type_descr ,ingr_code, ingr_descr , ingr_fraction,  ingr_fraction_type,  ingr_fraction_type_descr)
''')


df = pd.read_csv(r'/Users/junxiaoshen/Documents/GitHub/ICRISAT-backend/Recipes.csv')
df.to_sql('recipes', db, if_exists='append', index=False)

db.commit()
db.close()

#cursor.execute('''.mode csv''')

#cursor.execute('''import Recipes.csv recipes''')


#cursor.execute('''select ingr_code from recipes''')
