import pandas as pd
import numpy as np
import json

#Function with JSON dictionary as the input
def add_data_to_spreadsheet(data):
    #Data files required
    fct = pd.read_csv('Fct.csv', encoding='utf-8')
    conv = pd.read_csv('RetentionFactors.csv', encoding='utf-8')
    test_output = pd.read_csv('test_output2.csv', encoding='utf-8')

    fct_numbers = [food_item["fctNo"] for food_item in data["listOfFoods"]]
    conv_numbers = [food_item["rCode"] for food_item in data["listOfFoods"]]
    weights = [food_item["foodWeight"]/100 for food_item in data["listOfFoods"]]
    data_header = [data["interviewData"]["respondent"]["name"], data["interviewData"]["respondent"]["telephone"], "M"]

    #individual_matrix is used to calculate total micro and macro nutrients intake
    individual_matrix = []

    #Calculates the whole input data
    for i in range(len(weights)):
        fct_row = fct[fct["C_CODE"] == fct_numbers[i]]
        fct_row_np = np.array(fct_row)[0][3:]

        conv_row = conv[conv["R_Code"]==conv_numbers[i]]
        conv_row_np = np.array(conv_row)[0][2:]

        output_value = weights[i]*conv_row_np*fct_row_np
        individual_matrix.append(output_value)

    #This gives us the total consumption of one person
    ind_data = sum(individual_matrix)
    ind_data = np.concatenate((data_header,ind_data))

    #Columns need to have the same column headers to append to each other
    columns = conv.head(1)
    del columns['R_Code']
    del columns['R_Descr']
    header = ["Name", "Age", "Gender"]
    ind_data_pd = (pd.DataFrame(ind_data)).T
    ind_data_pd.columns = header + list(columns)

    test_output = test_output.append(ind_data_pd, ignore_index=True)
    test_output.to_csv('test_output2.csv', index=False)

    print(test_output)
