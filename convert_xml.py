#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lxml import etree
from openpyxl import Workbook
import argparse
import os
import sys

def parse_args():
    parser = argparse.ArgumentParser(description="Convert any XML to Excel (industrial-ready)")
    parser.add_argument("xml_file", help="Input XML file path")
    parser.add_argument("-o", "--output", help="Output Excel file", default="output.xlsx")
    return parser.parse_args()

def flatten_element(element, parent_key=''):
    data = {}
    # attributes
    for attr, val in element.attrib.items():
        key = f"{parent_key}_{attr}" if parent_key else attr
        data[key] = val
    # text
    text = element.text.strip() if element.text else ''
    if text and not list(element):
        key = f"{parent_key}_value" if parent_key else 'value'
        data[key] = text
    # children
    for child in element:
        key = f"{parent_key}_{child.tag}" if parent_key else child.tag
        data.update(flatten_element(child, key))
    return data

def detect_rows(root):
    # detect repeated children
    for elem in root.iter():
        tags = [child.tag for child in elem]
        if tags and len(set(tags)) == 1 and len(tags) > 0:
            return list(elem)
    return list(root)

def xml_to_rows(xml_file):
    tree = etree.parse(xml_file)
    root = tree.getroot()
    rows = detect_rows(root)
    data_rows = [flatten_element(r) for r in rows]
    return data_rows

def write_excel(rows, output_file):
    if not rows:
        raise ValueError("No data to write")
    wb = Workbook()
    ws = wb.active
    # toate coloanele unice
    columns = sorted({k for r in rows for k in r.keys()})
    ws.append(columns)
    for r in rows:
        ws.append([r.get(c, '') for c in columns])
    wb.save(output_file)

def main():
    args = parse_args()
    if not os.path.exists(args.xml_file):
        print(f"[ERROR] File not found: {args.xml_file}")
        sys.exit(1)
    rows = xml_to_rows(args.xml_file)
    write_excel(rows, args.output)
    print(f"[SUCCESS] Excel created: {args.output}")

if __name__ == "__main__":
    main()
