import fitz  # PyMuPDF para documentos PDF
from docx import Document
from google_scholar_py import scrape_google_scholar

# Función para extraer texto de documentos Word
def extract_text_from_word(docx_path):
    doc = Document(docx_path)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text

# Función para extraer texto de documentos PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    pdf_document = fitz.open(pdf_path)
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        text += page.get_text()
    return text

# Ruta de tu documento PDF o Word
document_path = "FORMATO INFORME DE PASANTIA v 2023-1.docx"  # Reemplaza con la ruta de tu documento PDF o Word
output_path = "informe_de_similitudes.txt"  # Ruta para guardar el informe

# Extraer el texto del documento
if document_path.endswith(".pdf"):
    text = extract_text_from_pdf(document_path)
elif document_path.endswith(".docx"):
    text = extract_text_from_word(document_path)
else:
    print("Formato de archivo no compatible.")
    exit()

# Realizar una búsqueda en Google Scholar
query = text  # Utiliza el texto del documento como consulta
results = scrape_google_scholar(query)

# Guardar el informe en un archivo de texto
with open(output_path, "w", encoding="utf-8") as report_file:
    for result in results:
        report_file.write(f"Fuente: {result['title']}\n")
        report_file.write(f"Enlace: {result['url']}\n")
        report_file.write(f"Fragmento Similar:\n{result['snippet']}\n\n")

print(f"Informe de similitudes generado en '{output_path}'.")
