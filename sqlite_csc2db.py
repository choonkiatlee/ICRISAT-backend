sqlite3 icrisat.db #create the dababase for all the tables created
create table recipes(recipe_code,  recipe_descr, recipe_type, recipe_type_descr ,ingr_code, ingr_descr , ingr_fraction,  ingr_fraction_type,  ingr_fraction_type_descr);
.mode csv #go to csv mode
.import Recipes.csv recipes # import the csv file data to the tables
select ingr_code from recipes; # to verify that the table has been created
