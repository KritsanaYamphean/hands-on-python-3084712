import csv
import json
from pprint import pprint

EINSTEIN = {
    "birthplace": "Germany",
    "name": "Albert",
    "surname": "Einstein",
    "born": "1879-03-14",
    "category": "physics",
    "motivation": "for his services to Theoretical Physics...",
}

einstein_json = json.dumps(EINSTEIN) #parse dict to json
back_to_dict = json.loads(einstein_json) #parse json to dict
print(einstein_json)
pprint(back_to_dict)

with open("laureates.csv", "r") as f: #r is read mode
    reader = csv.DictReader(f)
    laureates = list(reader)


with open("laureates.json", "w") as f: #r is write mode
    json.dump(laureates, f, indent=2)
