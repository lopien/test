import sys
import json

with open('tests.json') as f:
    tests_json = json.load(f)

with open('values.json') as f:
    values_json = json.load(f)

def test3(tests, values):
    for test in tests:
        if 'values' in test:
            test3(test['values'], values)    
        for value in values['values']:
            if test['id'] == value['id'] and 'value' in test:
                test['value'] = value['value']
             
test3(tests_json['tests'], values_json)

with open('report.json', 'w', encoding='utf-8') as jsonf: 
    jsonString = json.dumps(tests_json, indent=4, ensure_ascii=False)
    jsonf.write(jsonString)