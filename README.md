# xml2excel
Convert XML files to Excel (.xlsx) using Python, supporting large files and automatic structure detection

# XML2Excel Converter

Convert any XML file to Excel (.xlsx) using Python. Supports both small and large XML files with automatic detection of XML structure and flattening of attributes and sub-elements.

## Features
- Automatic XML structure detection
- Flatten attributes and sub-elements into Excel columns
- Memory-efficient for large files
- Cross-platform: Linux, macOS, Windows
- Two converter scripts:
  - convert_xml.py → for small to medium XML files
  - convert_xml_large.py → for large XML files (>500MB)

## Project Structure
xml2excel/
├── README.md
├── requirements.txt
├── convert_xml.py
├── convert_xml_large.py
└── simple.xml
├── large.xml

## Installation

Linux / macOS:
1. Clone the repository:
   git clone https://github.com/t3rmix/xml2excel.git
   cd xml2excel
   
2. Create a virtual environment and activate it:
   python3 -m venv xml2excel_env
   source xml2excel_env/bin/activate
   
3. Install dependencies:
   pip install -r requirements.txt

Windows (cmd / PowerShell):

1. Clone the repository:
   git clone https://github.com/username/xml2excel.git
   cd xml2excel
   
2. Create a virtual environment and activate it:
   python -m venv xml2excel_env
   xml2excel_env\Scripts\activate
   
3. Install dependencies:
   pip install -r requirements.txt

## Usage

For standard(small) XML files:
   python convert_xml.py simple.xml -o result_filename.xlsx
Replace `simple.xml` with your XML file path and `result_filename_simple.xlsx` with the desired output filename.

For large XML files:
   python convert_xml_large.py large.xml -o result_filename_large..xlsx

Replace `large.xml` with your XML file path and `result_filename_large.xlsx` with the desired output filename.

## Notes
- Virtual environments are recommended to avoid dependency conflicts.
- Use `convert_xml.py` for small/medium XML files and `convert_xml_large.py` for large XML files.

## Contributing
Submit issues or pull requests. Follow Python best practices and ensure cross-platform compatibility.

## License
Please review the terms of use and distribution in the LICENSE file located in the root of the project.
