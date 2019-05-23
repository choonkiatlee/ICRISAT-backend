import pandas as pd
import numpy as np
import json
import sqlite3
from test_script import *

with open('json_test_data.txt') as json_file:
    json_string = json_file.read()
data = json.loads(json_string)

add_data_to_spreadsheet(data)
