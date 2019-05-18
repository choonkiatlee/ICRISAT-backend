import pandas as pd
import numpy as np

weight = 100
weight /= 100
fct_number = 12
conv_number = 431

fct = pd.read_csv('Fct.csv', encoding='utf-8')
fct_row = fct[fct["C_CODE"] == fct_number]
fct_row_np = np.array(fct_row)[0][3:]

conv = pd.read_csv('RetentionFactors.csv', encoding='utf-8')
conv_row = conv[conv["R_Code"]==conv_number]
conv_row_np = np.array(conv_row)[0][2:]

output_values = weight*conv_row_np*fct_row_np
output = np.append(fct_row["C_DESCR"], output_values)
print(output)

output = pd.DataFrame(output)

print(output)

var = list(fct.head(1))

for i in var:
    print(i)
