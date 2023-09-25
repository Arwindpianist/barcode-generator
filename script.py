from barcode import EAN13

from barcode.writer import ImageWriter

number = str(input("Please enter the patient ID:"))

barcode = EAN13(number, writer=ImageWriter())

barcode.save("barcode")
