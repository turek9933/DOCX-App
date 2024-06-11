import sys
from docx2pdf import convert

def convert_docx_to_pdf(docx_files):
    for docx_file in docx_files:
        if not docx_file.endswith('.docx'):
            print(f"Plik {docx_file} nie jest plikiem .docx...")
            continue

        try:
            # Konwertuj plik .docx do .pdf i zapisz w tym samym katalogu
            output_file = docx_file.replace('.docx', '.pdf')
            convert(docx_file, output_file)
            print(f"Sukces: {docx_file} -> {output_file}")

        except Exception as e:
            print(f"Błąd podczas konwersji {docx_file}: {e}")

if len(sys.argv) < 2:
    print("Prawidłowa forma wywołania programu: python script.py <plik1.docx> <plik2.docx> ...")
    sys.exit(1)

docx_files = sys.argv[1:]

convert_docx_to_pdf(docx_files)