import json

def document_json_structure(data, indent=0):
    if isinstance(data, dict):
        for key, value in data.items():
            print('  ' * indent + f"{key}: {type(value).__name__}")
            document_json_structure(value, indent + 1)
    elif isinstance(data, list):
        if len(data) > 0:
            print('  ' * indent + f"List of {type(data[0]).__name__}")
            document_json_structure(data[0], indent + 1)
        else:
            print('  ' * indent + "Empty list")
    else:
        print('  ' * indent + f"{type(data).__name__}")

def main():
    json_file_path = 'path/to/your/json/file.json'
    with open(json_file_path, 'r') as file:
        data = json.load(file)
        document_json_structure(data)

if __name__ == "__main__":
    main()