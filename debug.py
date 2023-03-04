import codecs
import json
inFilePath = "SubjectWise/questions/OnM/chapter4.txt"
lines =[]

with open(inFilePath, 'r') as file:
    lines = file.readlines()
# Remove newlines and join lines into a single string
text = ''.join([line.strip() for line in lines])

#  Parse the text as JSON
data = json.loads(text)

# Print the resulting JSON data
print(json.dumps(data, indent=4))
 