#!/usr/bin/env python3

import yaml
import argparse
import ipaddress

parser = argparse.ArgumentParser(
    description="Fixing malformed records")
parser.add_argument(
    "--file", 
    required=True, 
    help="Config to be fixed")

args = parser.parse_args()

def fix_yaml(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)

    for key, value in data.items():
        if 'value' in value and isinstance(value['value'], str) and not value['value'].endswith('.'):
            if value['type'] == "CNAME":
                value['value'] += '.'
                print(value['value']+" add missing trailing .")
            elif value['type'] == "Route53Provider/ALIAS":
                value['value']['name'] += '.'
                print(value['value']['name']+" add missing trailing .")

    with open(file_path, 'w') as file:
        yaml.dump(
            data, 
            file, 
            default_flow_style=False)

def main():
    fix_yaml(args.file)

if __name__ == '__main__':
    main()
