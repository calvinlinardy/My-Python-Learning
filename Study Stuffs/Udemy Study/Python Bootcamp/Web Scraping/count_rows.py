import os
import pandas as pd

total_data = 0

filepath = '/Users/clcx/Documents/Calvin/CRM/Winna'

for fold,subfold,files in os.walk(filepath):
    for xl in files:
        if(xl[-4::] == 'xlsx'):
            pd_xl_file = pd.ExcelFile(filepath+'/'+xl)
            df = pd_xl_file.parse('Sheet1')
            dim = df.shape
            total_data += dim[0]

print(total_data)