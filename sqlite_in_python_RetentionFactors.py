import sqlite3
import csv
import pandas as pd


#creates or opens a file called icrisat.db with a SQLite3 DB
db = sqlite3.connect('icrisat.db')

#When we are done working with the DB we need to close the connection:



cursor = db.cursor()

cursor.execute('''
    create table RetentionFactors(R_Code,R_Descr,R_DryM,R_Water,R_Energy,R_Protein,R_Lipid,R_Cho,R_Fiber,R_Ca,R_Fe,R_Zn,R_VitC,R_Thiamin,R_Riboflavin,R_Niacin,R_VitB_6,R_Folate_food,R_FolicAcid,R_Folate_total,R_Folate_DFE,R_VitB_12,R_VitA_IU,R_VitA_RE,R_Retinol,R_AlphaCarotene,R_BetaCarotene,R_BetaCryptoxanthin)
''')


df = pd.read_csv(r'/Users/junxiaoshen/Documents/GitHub/ICRISAT-backend/RetentionFactors.csv')
df.to_sql('RetentionFactors', db, if_exists='append', index=False)

db.commit()
db.close()

#cursor.execute('''.mode csv''')

#cursor.execute('''import Recipes.csv recipes''')


#cursor.execute('''select ingr_code from recipes''')
