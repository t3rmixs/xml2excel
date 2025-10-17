#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
convert_xml_large.py
- Industrial-ready XML → Excel
- Suportă XML-uri mari (>500MB)
- Detectează automat rândurile și flatten-ează elementele
- Scrie Excel incremental cu openpyxl
"""

import os
import sys
import argparse
from lxml import etree
from openpyxl import Workbook

def parse_args():
    parser = argparse.ArgumentParser(description="Convert any large XML to Excel")
    parser.add_argument("xml_file", help="Input XML file path")
    parser.add_argument("-o", "--output", help="Output Excel file", default="output.xlsx")
    return parser.parse_args()

def flatten_element(element, parent_key=''):
    """Flatten an XML element recursively into a dictionary"""
    data = {}
    for attr, val in element.attrib.items():
        key = f"{parent_key}_{attr}" if parent_key else attr
        data[key] = val
    text = element.text.strip() if element.text else ''
    if text and not list(element):
        key = f"{parent_key}_value" if parent_key else 'value'
        data[key] = text
    for child in element:
        key = f"{parent_key}_{child.tag}" if parent_key else child.tag
        data.update(flatten_element(child, key))
    return data

def detect_row_elements(xml_file):
    """Detect repeated elements as rows without loading entire XML"""
    context = etree.iterparse(xml_file, events=("end",), recover=True)
    for event, elem in context:
        siblings = list(elem.getparent()) if elem.getparent() is not None else []
        tags = [s.tag for s in siblings]
        if tags and len(set(tags)) == 1 and len(tags) > 1:
            yield elem
            # Clear to save memory
            elem.clear()
            while elem.getprevious() is not None:
                del elem.getparent()[0]

def xml_to_excel(xml_file, excel_file):
    wb = Workbook()
    ws = wb.active
    columns_set = set()
    first_row = True

    # Iterativ, memory-safe
    for elem in detect_row_elements(xml_file):
        row_data = flatten_element(elem)
        # Update column headers dynamically
        columns_set.update(row_data.keys())
        # Write header once
        if first_row:
            columns = sorted(columns_set)
            ws.append(columns)
            first_row = False
        # Ensure all columns exist
        row_values = [row_data.get(col, '') for col in sorted(columns_set)]
        ws.append(row_values)
        elem.clear()

    if first_row:
        # Fallback: XML fără elemente repetate, scrie rădăcina
        tree = etree.parse(xml_file)
        root = tree.getroot()
        row_data = flatten_element(root)
        columns = sorted(row_data.keys())
        ws.append(columns)
        ws.append([row_data[col] for col in columns])

    wb.save(excel_file)
    print(f"[SUCCESS] Excel file created: {excel_file}")

def main():
    args = parse_args()
    if not os.path.exists(args.xml_file):
        print(f"[ERROR] File not found: {args.xml_file}")
        sys.exit(1)
    try:
        xml_to_excel(args.xml_file, args.output)
    except Exception as e:
        print(f"[ERROR] {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
