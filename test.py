# -*- coding: utf-8 -*-
"""
Created on Sat May 18 14:47:28 2019

@author: jimmy
"""

import pandas as pd
import numpy as np

weight = 100
weight /= 100
fct_row_np = []
output = []
fct = pd.read_csv('Fct.csv', encoding='utf-8')
conv = pd.read_csv('RetentionFactors.csv', encoding='utf-8')
a = fct["C_CODE"].max()
print(a)

fct_number_array = [10, 11, 12]
conv_number = 431

for i in fct_number_array:
    fct_row = fct[fct["C_CODE"] == i]
    fct_row_np.append(np.array(fct_row)[0][3:])
    
print(fct_row)


conv_row = conv[conv["R_Code"]==conv_number]
conv_row_np = np.array(conv_row)[0][2:]


for n in range(len(fct_row_np)):
    output_values = weight*conv_row_np*fct_row_np[n]
    output.append(np.append(fct_row["C_DESCR"], output_values))
#print(output)

output = pd.DataFrame(output)

print(output)

var = list(fct.head(1))
#print(var)
