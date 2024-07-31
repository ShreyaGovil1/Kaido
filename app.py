import pandas as pd
import json
from spire.xls import *
from spire.xls.common import *

# Load the JSON data
with open('data.json') as file:
    data = json.load(file)

# Convert the JSON data to a DataFrame
df = pd.DataFrame(data)

# Aggregate the data based on assetName
aggregated_df = df.groupby('assetName').agg({
    'quantity': 'sum',
    'lastPurchasePrice': 'sum',
    'totalAmount': 'sum'
}).reset_index()

capital_gain = df['totalAmount'].sum()
new_row = {'totalAmount':capital_gain}
aggregated_df = aggregated_df.append(new_row, ignore_index=True)

# Save the aggregated DataFrame to an Excel file
excel_path = 'aggregated_data.xlsx'
aggregated_df.to_excel(excel_path, index=False)


pdf_path='output.pdf'



#Create a workbook
workbook = Workbook()
#Load an Excel XLS or XLSX file
workbook.LoadFromFile(excel_path)

#Fit each worksheet to one page
workbook.ConverterSetting.SheetFitToPage = True
#convert the Excel file to PDF format
workbook.SaveToFile(pdf_path, FileFormat.PDF)
workbook.Dispose()
