import json

from GenerateDataEntryPoint import traverse_json

if __name__ == "__main__":
    with open("data/samples/single/sample1.json") as f:
        json_data = json.load(f)
        data = traverse_json(json_data)
        with open("output/dataEntryPoint.json", "w") as f:
            f.write(data)