import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

import sys
from docling.document_converter import DocumentConverter

def pdf_to_markdown(pdf_path: str, output_path: str) -> None:
    """
    Converts a PDF file to Markdown format and exports the content to a text file.

    Args:
        pdf_path (str): Path to the input PDF file.
        output_path (str): Path to the output text file where Markdown content will be saved.
    """
    try:
        # Initialize the DocumentConverter
        converter = DocumentConverter()

        # Convert the PDF to Markdown
        result = converter.convert(pdf_path)
        markdown_content = result.document.export_to_markdown()

        # Write the Markdown content to the output text file
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(markdown_content)
        
        print(f"Markdown content exported successfully to: {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":

    # Example usage
    pdf_path = sys.argv[1] # Replace with your PDF file path
    output_path = sys.argv[2] # Replace with your desired output text file path
    pdf_to_markdown(pdf_path, output_path)
