import json
file_path = 'restaurant_data.json'


def load_json(path):
    with open(f"{file_path}restaurant_data.json", "r") as file:
        restaurant_data = json.load(file)