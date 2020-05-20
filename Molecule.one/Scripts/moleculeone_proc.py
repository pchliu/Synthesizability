#processing results from molecule.one's json output

import json
import sys
import pandas as pd
import requests

input_file = sys.argv[1] #input .json file
output_file = sys.argv[2] #output raw .csv file with score (note you have to replace 10.0 with 0.0 via sed)
output_file_chemprop = sys.argv[3] #output processed .csv file, possible to go directly to chemprop
molecule_output_file = sys.argv[4] #output .csv file of just the molecules (without errors)
batch_id = sys.argv[5]
api_token = sys.argv[6] # api token to used for submission

url = "https://app.molecule.one/api/v1/batch-search" + str(batch_id)
headers = {
    "Content-Type": "application/json",
    "Authorization": "ApiToken-v1 " + str(api_token)
}
r = requests.get(url, headers=headers)
with open(input_file, 'w') as f: #note, sometimes there's extra information from the raw .json file, may need preprocessing
    f.write(r.content)

data = json.loads(r.content)

#with open(input_file, 'r', encoding='utf-8') as f:
#    data = json.loads(f.read())

proc_data = []
for dictionary in data:
    if 'error' not in dictionary.values():
        proc_data.append(dictionary)

for dictionary in proc_data:
    dictionary.pop('status')
    dictionary.pop('reactionCount')

result = pd.DataFrame(proc_data)
result['result'] = result['result'].astype(float)
result.to_csv(output_file, header=False, index=False)

result.replace(10.0, 0.0, inplace=True) #replaces 10.0 for nonsythesiazble molecules as 0.0 or -1.0 or -5.0
result.to_csv(output_file_chemprop, header=False, index=False)
#result.loc[result['result'] > 0.5, 'result'] = 1.0
#result[1] = result['result'].astype(int)
for dictionary in proc_data:
    dictionary.pop('result')

result = pd.DataFrame(proc_data) #outputs just the molecules
result.to_csv(molecule_output_file, header=False, index=False)
