import pandas as pd
import json

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

# Save the aggregated DataFrame to an Excel file
excel_path = 'aggregated_data.xlsx'
aggregated_df.to_excel(excel_path, index=False)

# Display the DataFrame to the user
# import ace_tools as tools; tools.display_dataframe_to_user(name="Aggregated Data", dataframe=aggregated_df)

# print(f"Aggregated data has been saved to {excel_path}")
