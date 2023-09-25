from barcode import Code128
from barcode.writer import ImageWriter
import openpyxl
import os

def generate_barcode(patient_id, output_dir):
    try:
        barcode = Code128(patient_id, writer=ImageWriter())
        barcode_file_path = os.path.join(output_dir, f"{patient_id}")
        barcode.save(barcode_file_path)
        return True
    except Exception as e:
        print(f"Error generating CODE128 barcode for patient ID {patient_id}: {e}")
        return False

def sanitize_patient_id(patient_id):
    return ''.join(filter(str.isdigit, patient_id))

def main():
    excel_file = "./excel/patientId.xlsx"
    output_dir = "./output"
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    try:
        wb = openpyxl.load_workbook(excel_file)
        sheet = wb.active
        for row in sheet.iter_rows(min_row=2, values_only=True):
            patient_id = str(row[0])
            if patient_id.strip():
                sanitized_id = sanitize_patient_id(patient_id)
                if len(sanitized_id) == 8:
                    if generate_barcode(sanitized_id, output_dir):
                        print(f"CODE128 barcode for patient ID {sanitized_id} saved to {output_dir}/{sanitized_id}.png")
                else:
                    print(f"Skipping invalid patient ID: {patient_id}")
        wb.close()
    except Exception as e:
        print(f"Error reading Excel file: {e}")

if __name__ == "__main__":
    main()
