import csv
import json
import os

SYSTEM_SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))

DATA_ADS = SYSTEM_SCRIPT_DIR+"/data/ads.csv"
JSON_ADS = 'ads.json'

DATA_CAT = SYSTEM_SCRIPT_DIR+"/data/categories.csv"
JSON_CAT = 'categories.json'

# def convert_file(csv_file, json_file=None):
#     result = []
#     with open(csv_file, encoding='utf-8') as csvf:
#         for row in csv.DictReader(csvf):
#             print(row)
#     pass
# convert_file(DATA_ADS)

# for entry in os.scandir('.'):
#     if entry.is_file():
#         print(entry.name)

def convert_file(csv_file, model_name, json_file):
    result = []
    with open(csv_file, encoding='utf-8') as csvf:
        for row in csv.DictReader(csvf):
            to_add = {'model': model_name, 'pk': int(row['Id'] if 'Id' in row else row['id'])}

            if 'Id' in row:
                del row['Id']
            else:
                del row['id']

            if 'is_published' in row:
                if row['is_published'] == "TRUE":
                    del row['is_published']
                    row['is_published'] = True
                    #row.update(is_published=True)
                else:
                    del row['is_published']
                    row['is_published'] = False
                    #row.update(is_published=False)

            if 'price' in row:
                row['price'] = int(row['price'])

            # print(row)
            # print("_____")
            # print(to_add)

            to_add['fields'] = row
            result.append(to_add)

    with open(json_file, 'w', encoding='utf-8') as jsf:
        jsf.write(json.dumps(result, ensure_ascii=False))


convert_file(DATA_ADS, "ads.ad", JSON_ADS)
convert_file(DATA_CAT, "ads.category", JSON_CAT)
