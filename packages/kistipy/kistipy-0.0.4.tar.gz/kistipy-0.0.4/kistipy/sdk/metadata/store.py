import json
import os

metadata_path = os.path.join('data', 'metadata')

metadata_store = {}
if not metadata_store:
    for file_name in os.listdir(metadata_path):
        metadata_key = os.path.splitext(os.path.basename(file_name))[0]
        with open(os.path.join(metadata_path, file_name), 'r') as metadata_file:
            data = metadata_file.read()
            metadata_store[metadata_key] = json.loads(data)