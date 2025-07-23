#!/usr/bin/env python3
import csv
import json
import os

def process_array_field(value):
    """
    Splits a newline-separated string into a list of strings.
    Each item is stripped of whitespace. Empty items are removed.
    Returns an empty list if the input is empty.
    """
    if not value:
        return []
    return [item.strip() for item in value.strip().split('\n') if item.strip()]

def convert_registries_to_json(csv_path, json_path):
    """
    Reads the registries CSV file, processes its rows according to specified
    data types, and writes the result to a JSON file.
    """
    records = []
    print(f"Processing {csv_path}...")
    try:
        with open(csv_path, mode='r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                # The first column name in registries.csv is 'tld'
                tld = row.get('tld', '').strip()
                if not tld:
                    continue  # Skip rows that don't have a TLD

                record = {
                    'tld': tld,
                    'name': process_array_field(row.get('name')),
                    'link': process_array_field(row.get('link')),
                    'email': process_array_field(row.get('email')),
                    'form': process_array_field(row.get('form')),
                    'api': row.get('api', '').strip() or None,
                    'notes': row.get('notes', '').strip() or None,
                    'found': row.get('found', '').strip() or None,
                    'as_of': row.get('as_of', '').strip() or None,
                }
                records.append(record)
    except FileNotFoundError:
        print(f"Error: Input file not found at {csv_path}")
        return
    except Exception as e:
        print(f"An error occurred while processing {csv_path}: {e}")
        return

    try:
        with open(json_path, mode='w', encoding='utf-8') as json_file:
            json.dump(records, json_file, indent=2, ensure_ascii=False)
        print(f"Successfully converted {csv_path} to {json_path}")
    except Exception as e:
        print(f"An error occurred while writing to {json_path}: {e}")

def convert_registrars_to_json(csv_path, json_path):
    """
    Reads the registrars CSV file, processes its rows according to specified
    data types, and writes the result to a JSON file.
    """
    records = []
    print(f"Processing {csv_path}...")
    try:
        with open(csv_path, mode='r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                iana_id_str = row.get('iana_id', '').strip()
                if not iana_id_str:
                    continue  # Skip rows without an IANA number

                try:
                    iana_id = int(iana_id_str)
                except ValueError:
                    print(f"Warning: Could not convert IANA number '{iana_id_str}' to int. Skipping row: {row}")
                    continue

                record = {
                    'iana_id': iana_id,
                    'name': row.get('name', '').strip() or None,
                    'link': process_array_field(row.get('link')),
                    'email': process_array_field(row.get('email')),
                    'form': process_array_field(row.get('form')),
                    'api': row.get('api', '').strip() or None,
                    'notes': row.get('notes', '').strip() or None,
                    'found': row.get('found', '').strip() or None,
                    'as_of': row.get('as_of', '').strip() or None,
                }
                records.append(record)
    except FileNotFoundError:
        print(f"Error: Input file not found at {csv_path}")
        return
    except Exception as e:
        print(f"An error occurred while processing {csv_path}: {e}")
        return

    try:
        with open(json_path, mode='w', encoding='utf-8') as json_file:
            json.dump(records, json_file, indent=2, ensure_ascii=False)
        print(f"Successfully converted {csv_path} to {json_path}")
    except Exception as e:
        print(f"An error occurred while writing to {json_path}: {e}")

def main():
    """Main function to orchestrate the CSV to JSON conversion."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    convert_registries_to_json(os.path.join(script_dir, 'registries.csv'), os.path.join(script_dir, 'registries.json'))
    print("-" * 20)
    convert_registrars_to_json(os.path.join(script_dir, 'registrars.csv'), os.path.join(script_dir, 'registrars.json'))

if __name__ == '__main__':
    main()