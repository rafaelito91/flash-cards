import json
import os

filename = "problems.json"


def get_data():
    if os.path.exists(filename):
        with open(filename, "r") as file:
            try:
                data = json.load(file)
                if not isinstance(data, list):
                    raise ValueError(f"The content of {filename} must be a JSON array.")
            except json.JSONDecodeError:
                raise ValueError(f"The file {filename} is not a valid JSON file.")
    else:
        # Initialize as an empty list if the file does not exist
        data = []

    return data


def save_data(data):
    # Write the updated data back to the file
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
