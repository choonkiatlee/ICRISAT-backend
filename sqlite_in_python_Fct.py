import sqlite3
import csv
import pandas as pd


#creates or opens a file called icrisat.db with a SQLite3 DB
db = sqlite3.connect('icrisat.db')

#When we are done working with the DB we need to close the connection:



cursor = db.cursor()

cursor.execute('''
    create table Fct(C_CODE,C_STATE,C_DESCR,C_DRYMATTER_G,C_WATER_G,C_ENERG_KCAL,C_PROTEIN_G,C_LIPID_TOT_G,C_CARBOHYDRT_G,C_FIBER_TD_G,C_CALCIUM_MG,C_IRON_MG,C_ZINC_MG,C_VIT_C_MG,C_THIAMIN_MG,C_RIBOFLAVIN_MG,C_NIACIN_MG,C_VIT_B6_MG,C_FOLATE_TOT_MCG,C_FOLIC_ACID_MCG,C_FOOD_FOLATE_MCG,C_FOLATE_MCG_DFE,C_VIT_B12_MCG,C_VIT_A_IU,C_VIT_A_MCG_RAE,C_RETINOL_MCG,C_ALPHA_CAROT_MCG,C_BETA_CAROT_MCG,C_BETA_CRYPT_MCG)
''')


df = pd.read_csv(r'/Users/junxiaoshen/Documents/GitHub/ICRISAT-backend/Fct.csv')
df.to_sql('Fct', db, if_exists='append', index=False)

db.commit()
db.close()

#cursor.execute('''.mode csv''')

#cursor.execute('''import Recipes.csv recipes''')


#cursor.execute('''select ingr_code from recipes''')
