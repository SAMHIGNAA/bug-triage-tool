import csv
import json

def read_bugs(file_path):
    bugs = []

    try:
        if file_path.endswith(".csv"):
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                bugs = list(reader)

        elif file_path.endswith(".json"):
            with open(file_path, 'r') as file:
                bugs = json.load(file)

        else:
            print("Unsupported file format")

    except Exception as e:
        print(f"Error: {e}")

    return bugs