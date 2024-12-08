import sys
import os
from PyPDF2 import PdfReader, PdfWriter

def extract_pages(input_pdf, output_pdf, start_page, end_page):
    try:
        reader = PdfReader(input_pdf)
        writer = PdfWriter()

        # Ensure pages are within valid range
        num_pages = len(reader.pages)
        if start_page < 1 or end_page > num_pages or start_page > end_page:
            print(f"Invalid page range. The document has {num_pages} pages.")
            return

        # Add pages to the writer
        for i in range(start_page - 1, end_page):  # Pages are zero-indexed
            writer.add_page(reader.pages[i])

        # Write to output file
        with open(output_pdf, "wb") as output_file:
            writer.write(output_file)

        print(f"Extracted pages {start_page} to {end_page} into '{output_pdf}'")
    except FileNotFoundError:
        print(f"Error: File '{input_pdf}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python extract_pdf_pages.py <input_pdf> <output_pdf> <start_page> <end_page>")
        sys.exit(1)

    input_pdf = sys.argv[1]
    output_pdf = sys.argv[2]
    try:
        start_page = int(sys.argv[3])
        end_page = int(sys.argv[4])
    except ValueError:
        print("Error: start_page and end_page must be integers.")
        sys.exit(1)

    extract_pages(input_pdf, output_pdf, start_page, end_page)