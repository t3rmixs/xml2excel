# XML2Excel Converter 📄➡️📊

Convert any **XML** file to **Excel (.xlsx)** using Python. This tool supports both small and large XML files by automatically detecting the XML structure and efficiently flattening attributes and sub-elements into a clean tabular format.

---

## ✨ Features
* **Automatic XML structure detection** for simplified usage.
* **Flattening** of attributes and sub-elements into Excel columns.
* **Memory-efficient** processing for handling very large files.
* **Cross-platform** compatible: Works on Linux, macOS, and Windows.
* **Two dedicated converter scripts:**
    * `convert_xml.py` → Optimized for **small to medium** XML files.
    * `convert_xml_large.py` → Designed for **large** XML files **(>500MB)**.

---

## ⚙️ Installation

Virtual environments are **highly recommended** to manage dependencies.

### Linux / macOS

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/t3rmixs/xml2excel.git
    cd xml2excel
    ```
2.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv xml2excel_env
    source xml2excel_env/bin/activate
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
<img width="1468" height="677" alt="Image" src="https://github.com/user-attachments/assets/cc10a2e6-2256-47ae-9c55-4ee42df47ffa" />


### Windows (cmd / PowerShell)

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/t3rmixs/xml2excel.git
    cd xml2excel
    ```
2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv xml2excel_env
    .\xml2excel_env\Scripts\activate
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

---

## 🚀 Usage



Make sure you have activated your virtual environment before running the scripts.   

```bash
    source xml2excel_env/bin/activate
   ```

### For Standard (Small/Medium) XML Files

<img width="1483" height="694" alt="Image" src="https://github.com/user-attachments/assets/f1b36e9f-2a25-40a6-b5bc-98e691e2c6e5" />


Use `convert_xml.py`:

```bash
python3 convert_xml.py small.xml -o result_filename_small.xlsx
  ```
  *Replace `small.xml` with your XML file path and `result_filename_small.xlsx` with the desired output filename.*

### For Large XML Files (>500MB)

<img width="1496" height="704" alt="Image" src="https://github.com/user-attachments/assets/c5edad97-914f-4c6a-84fb-91bfb119dfd7" />

Use the memory-efficient `convert_xml_large.py`:

```bash
python3 convert_xml_large.py large.xml -o result_filename_large.xlsx
 ```
*Replace `large.xml` with your XML file path and `result_filename_large.xlsx` with the desired output filename.*

---

## 📝 Notes
* Virtual environments are recommended to avoid dependency conflicts.
* Use `convert_xml.py` for small/medium XML files and `convert_xml_large.py` for large XML files.
* Please `upload` and `open` on `google drive` to prevent errors while open the result file.
---

## 🤝 Contributing

Submit issues or pull requests. Follow Python best practices and ensure cross-platform compatibility.

---

## ⚖️ License

Please review the terms of use and distribution in the **LICENSE** file located in the root of the project.
