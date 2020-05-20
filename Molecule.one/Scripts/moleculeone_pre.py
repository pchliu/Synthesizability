#prepare file to submit to molecule.one and submit

import sys
import requests
import json

input_file = sys.argv[1] #input .csv file
output_file = sys.argv[2] #output .json file to submit to molecule.one
response_file = sys.argv[3] #saves responses from submission
api_token = sys.argv[4] # api token to used for submission

f = open(input_file, 'r')
temp = f.read().splitlines()
data = []
for line in temp:
    data.append(line.split(',')[1])

with open(output_file, 'w') as file:
        file.write('"targets": ' + str(data).replace("'", '"') + "}")

url = "https://app.molecule.one/api/v1/batch-search"
headers = {
    "Content-Type": "application/json",
    "Authorization": "ApiToken-v1 " + str(api_token)
}
molecules = open(output_file)
r = requests.post(url, data=molecules, headers=headers)
molecules.close()
with open(response_file, 'w') as f:
    json.dump(r.json(), f)
