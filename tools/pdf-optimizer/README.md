# PDF Optimizer Script

A Python utility for optimizing PDF files by removing images and compressing content. This tool is particularly useful when preparing PDFs for text analysis, AI processing, or reducing storage space where images aren't needed.

## Features

- 🗑️ Removes images from PDFs while preserving text content
- 📦 Compresses PDF content
- 🔄 Supports batch processing of multiple PDFs
- 💻 Command-line interface for easy integration
- ✨ Preserves PDF metadata
- 🚀 Lightweight and easy to use

## Installation

1. Clone this repository:
```bash
git clone https://github.com/rangzen/cairn
cd tools/pdf-optimizer
```

2. Install the required dependency:
```bash
pip install PyPDF2
```
or
```bash
poetry install
```

## Usage

### As a Command-Line Tool

1. Optimize a single PDF file:
```bash
python pdf_optimizer.py input.pdf --output optimized.pdf
```

2. Process all PDFs in a directory:
```bash
python pdf_optimizer.py input_directory --batch
```

## Use Cases

1. **AI Text Analysis**: Prepare PDFs for AI models that only need text content
2. **Storage Optimization**: Reduce file sizes when images aren't necessary
3. **Email Attachments**: Create smaller PDFs for email transmission
4. **Batch Processing**: Optimize entire directories of PDFs for archival purposes

## Limitations

- The script removes all images from PDFs
- Some PDFs with complex structures might not be processed correctly
- The output PDF maintains text content but may have different formatting
- Password-protected PDFs are not supported

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## License

There is no licence, do what you want.

## Acknowledgments

- Built using [PyPDF2](https://pypdf2.readthedocs.io/)
- Inspired by the need for efficient PDF processing for AI applications

## Support

If you encounter any issues or have questions, please:
1. Check existing issues or create a new one
2. Provide sample PDFs that demonstrate the problem (if possible)
3. Include your Python version and PyPDF2 version

---
Made with ❤️ from QC.
