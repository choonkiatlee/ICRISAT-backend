import pandas as pd
import numpy as np

fct = pd.read_csv('Fct.csv', encoding='utf-8')
conv = pd.read_csv('RetentionFactors.csv', encoding='utf-8')

=======
weights = [100, 200, 300, 400, 500]
normalised_weights = [i/100 for i in weights]
fct_numbers = [174, 13, 14, 73, 84]
conv_numbers = [431, 431, 431, 431, 431]

output = []
for i in range(len(weights)):

=======
    fct_row = fct[fct["C_CODE"] == fct_numbers[i]]
    fct_row_np = np.array(fct_row)[0][3:]

    conv_row = conv[conv["R_Code"]==conv_numbers[i]]
    conv_row_np = np.array(conv_row)[0][2:]

    output_value = normalised_weights[i]*conv_row_np*fct_row_np
    output_value = np.append(fct_row["C_DESCR"], output_value)
    output.append(output_value)

print(output)
print(pd.DataFrame(output))
=======
print(output)
print(pd.DataFrame(output))
>>>>>>> 9939b04ceee9bd1c369f6bf467ea891d60cebb3d
