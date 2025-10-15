import json

data = {
    'name': 'tade',
    'age': 25,
    'occupation': 'engineer'
}


json_file = json.dumps(data)

with open('data.json', 'w', encoding='utf-8') as file:
    json.dump(data, file)


print(data)


def process_json(input_data: dict, filename: str) -> dict:
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(input_data, file)

    with open(filename, 'r', encoding='utf-8') as file:
        deserialized_data = json.load(file)

    return deserialized_data
