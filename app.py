import sys
from pdf2image import convert_from_path

def main():
    if len(sys.argv) < 2:
        print("Usage: pdf2png <pdf_file>")
        sys.exit(1)
    
    pdf_file = sys.argv[1]
    try:
        images = convert_from_path(pdf_file)
        for i, image in enumerate(images):
            image.save(f"output_page_{i + 1}.png", "PNG")
        print(f"Converted {len(images)} pages from {pdf_file} to PNG.")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
