import sqlite3
import csv
import pandas as pd


#creates or opens a file called icrisat.db with a SQLite3 DB
db = sqlite3.connect('icrisat.db')

list_of_csv_files = ['Fct.csv','RetentionFactors.csv','Recipes.csv']


#When we are done working with the DB we need to close the connection:
for csv_filename in list_of_csv_files:

    df = pd.read_csv(csv_filename)

    # Create table command
    table_command = "create table " + os.path.splitext(csv_filename)[0] + "(" + ','.join(df.columns) + ")"

    cursor = db.cursor()
    cursor.execute(table_command)
    df.to_sql(os.path.splitext(csv_filename)[0], db, if_exists='append', index=False)

    db.commit()
    
db.close()

#cursor.execute('''.mode csv''')

#cursor.execute('''import Recipes.csv recipes''')


#cursor.execute('''select ingr_code from recipes''')
