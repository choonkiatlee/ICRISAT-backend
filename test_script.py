import pandas

x = 12
fct = pandas.read_csv('Fct.csv', encoding='utf-8')
fct_row = fct[fct["C_CODE                   "] == x]
print(fct_row)

conv = pandas.read_csv('RetentionFactors.csv', encoding='utf-8')
conv_row = conv[conv["R_Code"]==431]
print(conv_row)

transpose_conv = conv_row.T
transpose_fct = fct_row.T

fct_array = transpose_fct.iloc[3:].values.T[0]
conv_array = transpose_conv.iloc[2:].values.T[0]

print(conv_array)
