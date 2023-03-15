import json

# Load JSON data from file
with open('SubjectWise/Results/SE/Chapter10.json',encoding='utf-8') as f:
    data = json.load(f)

# Define the key to check for
key_to_check = 'marks'

# Loop through each entry and check if the key is missing
for entry in data:
    if key_to_check not in entry:
        print(f"Key '{key_to_check}' is missing in entry: {entry}")