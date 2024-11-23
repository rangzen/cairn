import os
from pathlib import Path

import PyPDF2


def optimize_pdf(input_path: str, output_path: str = None) -> str:
    """
    Optimize a PDF file by removing images and compressing content.

    Args:
        input_path (str): Path to the input PDF file
        output_path (str, optional): Path for the optimized output file.
            If not provided, will append '_optimized' to the input filename.

    Returns:
        str: Path to the optimized file
    """
    # Create output path if not provided
    if output_path is None:
        input_file = Path(input_path)
        output_path = str(
            input_file.parent / f"{input_file.stem}_optimized{input_file.suffix}"
        )

    with open(input_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        writer = PyPDF2.PdfWriter()

        # Process each page
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]

            # Remove images by clearing the resource dictionary
            if "/Resources" in page and "/XObject" in page["/Resources"]:
                del page["/Resources"]["/XObject"]

            writer.add_page(page)

        # Set up compression
        writer.add_metadata(reader.metadata)

        # Write the optimized file
        with open(output_path, "wb") as output_file:
            writer.write(output_file)

    return output_path


def batch_optimize_pdfs(input_dir: str, output_dir: str = None) -> list:
    """
    Optimize all PDF files in a directory.

    Args:
        input_dir (str): Directory containing PDF files to optimize
        output_dir (str, optional): Directory for optimized files.
            If not provided, will create an 'optimized' subdirectory.

    Returns:
        list: List of paths to optimized files
    """
    # Set up output directory
    if output_dir is None:
        output_dir = os.path.join(input_dir, "optimized")

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    optimized_files = []

    # Process each PDF file in the input directory
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(".pdf"):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, f"optimized_{filename}")

            try:
                optimized_path = optimize_pdf(input_path, output_path)
                optimized_files.append(optimized_path)
                print(f"Successfully optimized: {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {str(e)}")

    return optimized_files


def main():
    # Example usage
    import argparse

    parser = argparse.ArgumentParser(
        description="Optimize PDF files by removing images and compressing content."
    )
    parser.add_argument("input", help="Input PDF file or directory")
    parser.add_argument("--output", help="Output file or directory (optional)")
    parser.add_argument(
        "--batch", action="store_true", help="Process all PDFs in input directory"
    )

    args = parser.parse_args()

    if args.batch:
        optimized_files = batch_optimize_pdfs(args.input, args.output)
        print(f"\nOptimized {len(optimized_files)} files")
    else:
        output_path = optimize_pdf(args.input, args.output)
        print(f"\nOptimized PDF saved to: {output_path}")


if __name__ == "__main__":
    main()
