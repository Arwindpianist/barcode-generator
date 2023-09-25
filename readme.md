# Barcode Generator

This repository contains a Python script to generate barcodes from patient IDs stored in an Excel sheet and another script to arrange these barcodes into A4-sized sheets for easy printing.

## Prerequisites

Before running the scripts, ensure that you have the following dependencies installed:

- Python 3.x
- Required Python packages (install them using `pip install -r requirements.txt`):
  - `openpyxl`
  - `barcode`
  - `reportlab`
  - `Pillow`

## Getting Started

Follow these steps to generate and arrange barcodes:

### 1. Clone the Repository

Clone this repository to your local machine using Git:

```
git clone https://github.com/Arwindpianist/barcode-generator.git
```

### 2. Prepare Your Data

- Open the `patientId.xlsx` Excel file located in the `./excel/` directory.
- Add patient IDs (8 digits) in the first column (Column A). Ensure that each patient ID is in a separate row.

### 3. Generate Barcodes

Run the `script.py` script to generate barcodes from the patient IDs:

```
python script.py
```


The generated barcode images will be saved in the `./output/` directory.

### 4. Arrange Barcodes

Run the `arrange.py` script to arrange the generated barcodes into A4-sized sheets:

```
python arrange.py
```


The arranged barcode sheets will be saved in the `./output/arranged/` directory.

## Customization

- You can customize the number of columns and rows per A4 sheet in the `arrange.py` script by modifying the `columns` and `rows` variables.

## Troubleshooting

- If you encounter any issues or errors during barcode generation or arrangement, please check the error messages and ensure that your patient IDs are correctly formatted.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


