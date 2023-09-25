import os
import openpyxl
from barcode import EAN8
from barcode.writer import ImageWriter
from math import ceil
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Image as RLImage, Table, TableStyle

# Function to generate EAN-8 barcode and save it
def generate_barcode(patient_id, output_dir):
    try:
        barcode = EAN8(patient_id, writer=ImageWriter())
        barcode_file_path = os.path.join(output_dir, f"{patient_id}.png")
        barcode.save(barcode_file_path)
        return barcode_file_path
    except Exception as e:
        print(f"Error generating EAN-8 barcode for patient ID {patient_id}: {e}")
        return None

# Function to fit barcode images on A4-sized pages
def fit_barcodes_to_a4(barcodes, output_path):
    img_width, img_height = 210, 297  # A4 paper size in mm
    barcode_size = 60  # Size of each barcode image in mm
    barcodes_per_row = 6  # Number of barcodes per row

    rows = ceil(len(barcodes) / barcodes_per_row)
    doc = SimpleDocTemplate(output_path, pagesize=(img_width, img_height))
    elements = []

    data = [[RLImage(barcode, width=barcode_size, height=barcode_size) for barcode in barcodes[i:i+barcodes_per_row]] for i in range(0, len(barcodes), barcodes_per_row)]
    table = Table(data)
    table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('INNERGRID', (0, 0), (-1, -1), 0.25, (0, 0, 0)),
        ('BOX', (0, 0), (-1, -1), 0.25, (0, 0, 0)),
    ]))
    elements.append(table)

    doc.build(elements)

# Main function
def main():
    excel_file = "./excel/patientId.xlsx"
    output_dir = "./output"
    barcodes = []

    # Load patient IDs from Excel file
    try:
        wb = openpyxl.load_workbook(excel_file)
        sheet = wb.active
        for row in sheet.iter_rows(min_row=2, values_only=True):
            patient_id = str(row[0])
            if len(patient_id) == 8 and patient_id.isdigit():  # Check if patient_id is 8 digits long and contains only digits
                barcode = generate_barcode(patient_id, output_dir)
                if barcode:
                    barcodes.append(barcode)
        wb.close()
        a4_output_path = f"{output_dir}/a4_sheet.pdf"
        fit_barcodes_to_a4(barcodes, a4_output_path)
        print(f"Barcodes saved to {output_dir}")
        print(f"A4 sheet with barcodes saved to {a4_output_path}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
