import json

data = []
with open('first_20_lines.txt') as f:
    for line in f:
        data.append(json.loads(line))
data = json.loads(line);
print data[u'text']

         

     
