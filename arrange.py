from reportlab.platypus import SimpleDocTemplate, Image
from reportlab.lib.pagesizes import A4
from math import ceil
import os


def get_barcode_image_paths(output_dir):
    return [os.path.join(output_dir, file) for file in os.listdir(output_dir) if file.endswith('.png')]


def arrange_barcodes_into_a4_pages(barcode_image_paths, output_pdf_path):
    doc = SimpleDocTemplate(output_pdf_path, pagesize=A4)
    page_story = []

    columns = 5  
    rows = 8     

    num_pages = ceil(len(barcode_image_paths) / (columns * rows))

    for page_num in range(num_pages):
        page_story = []

        for i in range(columns * rows):
            barcode_index = page_num * (columns * rows) + i

            if barcode_index >= len(barcode_image_paths):
                break

            barcode_path = barcode_image_paths[barcode_index]

            img = Image(barcode_path)
            img.drawWidth = A4[0] / columns
            img.drawHeight = A4[1] / rows
            page_story.append(img)

        doc.build(page_story)

if __name__ == "__main__":
    output_dir = "./output"
    output_pdf_path = "./output/barcodes_arranged.pdf"

    barcode_image_paths = get_barcode_image_paths(output_dir)

    if barcode_image_paths:
        arrange_barcodes_into_a4_pages(barcode_image_paths, output_pdf_path)
        print(f"Barcodes arranged into A4-sized pages and saved to {output_pdf_path}")
    else:
        print("No barcode images found in the 'output' directory.")
