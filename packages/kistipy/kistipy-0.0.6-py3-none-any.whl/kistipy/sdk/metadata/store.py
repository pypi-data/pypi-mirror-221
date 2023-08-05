import json
import os

metadata_path = 'metadata'

metadata_store = {}
if not metadata_store and os.path.exists(metadata_path):
    for file_name in os.listdir(metadata_path):
        metadata_key = os.path.splitext(os.path.basename(file_name))[0]
        with open(os.path.join(metadata_path, file_name), 'r') as metadata_file:
            data = metadata_file.read()
            metadata_store[metadata_key] = json.loads(data)