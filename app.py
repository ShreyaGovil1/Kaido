import pandas as pd
import json
import matplotlib.pyplot as plt

# Load the JSON data
with open('data.json') as file:
    data = json.load(file)

# Convert the JSON data to a DataFrame
df = pd.DataFrame(data)

# Aggregate the data based on assetName
aggregated_df = df.groupby('assetName').agg({
    'quantity': 'sum',
    'lastPurchasePrice': 'mean',
    'totalAmount': 'sum'
}).reset_index()

# Calculate the sum of totalAmount for all unique assetNames
capital_gain = aggregated_df['totalAmount'].sum()
new_row = {'assetName':"Realised Capital Gain",'totalAmount':capital_gain}
aggregated_df = aggregated_df.append(new_row, ignore_index=True)


# Save the aggregated DataFrame and total sum to an Excel file
excel_path = 'aggregated_data.xlsx'
with pd.ExcelWriter(excel_path) as writer:
    aggregated_df.to_excel(writer, sheet_name='Aggregated Data', index=False)
    summary_df = pd.DataFrame({' Realised Capital Gain': [capital_gain]})
    summary_df.to_excel(writer, sheet_name='Summary', index=False)

# Convert the Excel to PDF by first displaying it as a table in Matplotlib
pdf_path = 'output.pdf'

# Create a figure and axis to plot the DataFrame
fig, ax = plt.subplots(figsize=(8, 4))

# Hide the axes
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)
ax.set_frame_on(False)

# Add the table and set its size
table = ax.table(cellText=aggregated_df.values, colLabels=aggregated_df.columns, cellLoc='center', loc='center')

# Adjust the font size and scale of the table to fit within the figure
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.2)

# Save the figure as a PDF
plt.savefig(pdf_path, format='pdf')