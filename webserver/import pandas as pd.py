pip install pandas

import pandas as pd

# Load the Excel file
file_path = r'D:\EXPDATA\mainproj_PEPFAX\webserver\webserver\1304_uniprot.xlsx'
data = pd.read_excel(file_path)

# Function to clean up Gene Ontology fields
def clean_go_field(field):
    import re
    if pd.isna(field):
        return ''
    return re.sub(r'\[.*?\]', '', field).strip()

# Clean the Gene Ontology fields
data['Gene Ontology (cellular component)'] = data['Gene Ontology (cellular component)'].apply(clean_go_field)
data['Gene Ontology (biological process)'] = data['Gene Ontology (biological process)'].apply(clean_go_field)
data['Gene Ontology (molecular function)'] = data['Gene Ontology (molecular function)'].apply(clean_go_field)

# Convert to JSON
json_data = data.to_json(orient='records')

# Save to JSON file
output_json_path = r'D:\EXPDATA\mainproj_PEPFAX\webserver\webserver\1304_uniprot.json'
with open(output_json_path, 'w') as file:
    file.write(json_data)

