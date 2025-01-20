import sys
import os
from pdf2image import convert_from_path

def pdf_to_png(filepath):
    images = convert_from_path(filepath)
    for page_num, image in enumerate(images):
        image.save(f"{filepath}_{page_num}.png")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python app.py <filepath>")
        sys.exit(1)
    filepath = sys.argv[1]
    if not filepath.endswith(".pdf"):
        print("Please provide a .pdf file")
        sys.exit(1)
    if not os.path.exists(filepath):
        print("File does not exist")
        sys.exit(1)
    pdf_to_png(filepath)
    print("PDF converted to PNG")
    sys.exit(0)
