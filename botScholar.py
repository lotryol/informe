import fitz
import re
from scholarly import scholarly

# Función para dividir el texto en lotes de 500 palabras
def split_text_into_batches(text, batch_size=500):
    batches = []
    words = re.findall(r'\b\w+\b', text)  # Divide por palabras
    current_batch = []
    word_count = 0

    for word in words:
        current_batch.append(word)
        word_count += 1

        if word_count >= batch_size:
            batches.append(" ".join(current_batch))
            current_batch = []
            word_count = 0

    if current_batch:
        batches.append(" ".join(current_batch))

    return batches

# Ruta de tu archivo PDF
pdf_path = "FORMATO INFORME DE PASANTIA v 2023-1.pdf"  # Reemplaza con la ruta de tu archivo PDF
output_file = "resultados_google_scholar.txt"  # Nombre del archivo de salida

# Extraer texto del PDF
text = ""
pdf_document = fitz.open(pdf_path)
for page in pdf_document:
    text += page.get_text()

# Dividir el texto en lotes de 500 palabras
text_batches = split_text_into_batches(text, batch_size=100)
print(text_batches)

# Abrir el archivo de salida para escritura
with open(output_file, "w", encoding="utf-8") as output:
    # Buscar en Google Scholar y recopilar resultados
    for batch in text_batches:
        search_query = scholarly.search_pubs(batch)
        for i in range(5):  # Recopila los primeros 5 resultados
            result = next(search_query, None)
            if result:
                # Imprime el objeto result completo
                #print(result)
                output.write("Resultado completo:\n{}\n\n".format(result))

print("Resultados almacenados en '{}'.".format(output_file))
