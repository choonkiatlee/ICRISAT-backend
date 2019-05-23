import pandas as pd
import numpy as np
import json
import datetime

class BackendCalculator:

    def __init__(self):
        #Data files required
        self.fct = pd.read_csv('Fct.csv', encoding='utf-8')
        self.conv = pd.read_csv('RetentionFactors.csv', encoding='utf-8')

    #Function with JSON dictionary as the input
    def add_data_to_spreadsheet(self,data):
                
        test_output = pd.read_csv('test_output2.csv', encoding='utf-8')

        # For now, we use a kinda hacky method to extract all the ingredients quickly, but it might be worth spending the 
        # time to do this properly by separating it into different functions or something?
        foodIngredientsList = [foodItem.get("ingredients",[]) for foodItem in data.get("listOfFoods",[])]
        listOfIngredients = []
        for ingredientList in foodIngredientsList:
            for ingredient in ingredientList:
                listOfIngredients.append(ingredient)
        # Conv numbers are not returned at this moment! 
        # For the demo, we just populate it with a random list of conv_numbers
        conv_numbers = self.conv.sample(len(listOfIngredients))["R_Code"].tolist()
        
        fct_numbers = [food_item["fctCode"] for food_item in listOfIngredients]
        # conv_numbers = [food_item["rCode"] for food_item in listOfIngredients]
        
        weights = [food_item["measurement"]/100 for food_item in listOfIngredients]
        brirthDate = datetime.datetime.strptime( data["interviewData"]["respondent"]["birthDate"], "%Y-%m-%d %H:%M:%S.%f")
        data_header = [data["interviewData"]["respondent"]["name"], self.calculate_age(brirthDate), "M"]

        #individual_matrix is used to calculate total micro and macro nutrients intake
        individual_matrix = []

        #Calculates the whole input data
        for i in range(len(weights)):
            fct_row = self.fct[self.fct["C_CODE"] == fct_numbers[i]]
            fct_row_np = np.array(fct_row)[0][3:]

            conv_row = self.conv[self.conv["R_Code"]==conv_numbers[i]]
            conv_row_np = np.array(conv_row)[0][2:]

            output_value = weights[i]*conv_row_np*fct_row_np
            individual_matrix.append(output_value)

        #This gives us the total consumption of one person
        ind_data = sum(individual_matrix)
        ind_data = np.concatenate((data_header,ind_data))

        #Columns need to have the same column headers to append to each other
        columns = self.conv.head(1)
        del columns['R_Code']
        del columns['R_Descr']
        header = ["Name", "Age", "Gender"]
        ind_data_pd = (pd.DataFrame(ind_data)).T
        ind_data_pd.columns = header + list(columns)

        test_output = test_output.append(ind_data_pd, ignore_index=True)
        test_output.to_csv('test_output2.csv', index=False)

        print("Output written!")

        # print(test_output)

    @staticmethod
    def calculate_age(born):
        today = datetime.date.today()
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
