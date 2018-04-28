import json
import pandas
from pprint import pprint

data = json.load(open('Pakendi_klassik.json'))
output_dict = dict()
for element in data:
    if element['code'] not in output_dict:
        output_dict[element['code']] = element['description']

rows_list = []
headers = ['code', 'ET', 'EN', 'RU']

for key, value in output_dict.items():
    rows_list.append([key, value['ET'], value['EN'], value['RU']])

df = pandas.DataFrame(rows_list, columns=headers)
df.to_csv('pakendi_klasik.csv', index=False)
