import sqlite3
import csv
import pandas as pd


#creates or opens a file called icrisat.db with a SQLite3 DB
db = sqlite3.connect('icrisa.db')

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

rr
#cursor.execute('''select ingr_code from recipes''')
'''
user1 = cursor.fetchone() #retrieve the first row
print(user1[0]) #Print the first column retrieved(user's name)
all_rows = cursor.fetchall()
for row in all_rows:
    # row[0] returns the first column in the query (name), row[1] returns email column.
    print('{0} : {1}, {2}'.format(row[0], row[1], row[2]))
    '''
