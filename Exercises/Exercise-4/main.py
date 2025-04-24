import os
import glob
import json
import csv

def flatten_json(nested_json, parent_key='', sep='_'):
    """Flatten nested JSON (dict and list) into a single-level dictionary."""
    items = []
    for k, v in nested_json.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_json(v, new_key, sep=sep).items())
        elif isinstance(v, list):
            for i, item in enumerate(v):
                items.extend(flatten_json({f"{i}": item}, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def json_to_csv(json_path):
    """Convert a JSON file to CSV, saving next to original file."""
    try:
        with open(json_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except json.JSONDecodeError as e:
        print(f"[✘] Error reading JSON file {json_path}: {e}")
        return
    except FileNotFoundError:
        print(f"[✘] File not found: {json_path}")
        return

    # Handle both single JSON objects and lists
    if isinstance(data, list):
        flat_data = [flatten_json(item) for item in data]
    else:
        flat_data = [flatten_json(data)]

    if not flat_data:
        print(f"[!] No valid data to write from: {json_path}")
        return

    csv_path = json_path.replace('.json', '.csv')

    try:
        with open(csv_path, 'w', newline='', encoding='utf-8-sig') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=flat_data[0].keys())
            writer.writeheader()
            for row in flat_data:
                writer.writerow(row)
        print(f"[✔] Converted: {json_path} → {csv_path}")
    except Exception as e:
        print(f"[✘] Error writing CSV file {csv_path}: {e}")

def main():
    data_dir = "data"
    os.makedirs(data_dir, exist_ok=True)
    print(f"[+] Scanning directory: {data_dir}")

    json_files = glob.glob(os.path.join(data_dir, '**/*.json'), recursive=True)

    if not json_files:
        print("[!] No JSON files found.")
        return

    for path in json_files:
        json_to_csv(path)

if __name__ == "__main__":
    main()
