import locale
import ghostscript
def rescale_compress_pdf(input_pdf_path, output_pdf_path):
    args = [
        "ps2pdf", # actual value doesn't matter
        "-sDEVICE=pdfwrite",
        "-dCompatibilityLevel=1.4",
        "-dPDFSETTINGS=/ebook",
        "-dNOPAUSE", "-dQUIET", "-dBATCH",
        "-sOutputFile=" + output_pdf_path,
        "-dDEVICEWIDTHPOINTS=595", "-dDEVICEHEIGHTPOINTS=842", "-dPDFFitPage",
        "-f", input_pdf_path
        ]

    # arguments have to be bytes, encode them
    encoding = locale.getpreferredencoding()
    args = [a.encode(encoding) for a in args]
    
    ghostscript.Ghostscript(*args)

# Usage example
input_pdf_path = 'input.pdf'  # Replace with your input PDF file path
output_pdf_path = 'ouput.pdf'  # Replace with the desired output PDF file path
rescale_compress_pdf(input_pdf_path, output_pdf_path)

