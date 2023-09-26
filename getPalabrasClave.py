from docx import Document
from collections import Counter
from nltk.corpus import stopwords
import nltk
import string

# Descargar recursos de NLTK para el idioma español
nltk.download('stopwords')

# Función para extraer palabras clave del contenido del documento en español excluyendo palabras específicas
def extract_keywords(docx_path, num_keywords=5):
    doc = Document(docx_path)
    
    # Recopilar todo el texto del documento
    full_text = ""
    for paragraph in doc.paragraphs:
        full_text += paragraph.text + " "

    # Tokenizar el texto y eliminar stopwords y signos de puntuación
    translator = str.maketrans('', '', string.punctuation)
    words = nltk.word_tokenize(full_text, language='spanish')  # Tokenización en español
    words = [word.lower() for word in words]

    # Lista de palabras a excluir
    exclude_words = ["datos", "pasantía", "clientes", "desarrollo","colombia","keyrus","sas","empresa"]

    # Filtrar palabras a excluir
    words = [word for word in words if word not in stopwords.words('spanish') and word not in exclude_words]
    words = [word.translate(translator) for word in words]

    # Contar la frecuencia de las palabras
    word_freq = Counter(words)

    # Obtener las palabras clave más frecuentes
    keywords = word_freq.most_common(num_keywords)

    return [keyword for keyword, _ in keywords]

# Ruta de tu documento Word en español
document_path = "FORMATO INFORME DE PASANTIA v 2023-1.docx"  # Reemplaza con la ruta de tu documento Word en español
num_keywords = 15  # Cambia el número de palabras clave que deseas obtener

# Extraer palabras clave del documento en español
keywords = extract_keywords(document_path, num_keywords)

# Imprimir las palabras clave
print("Palabras clave extraídas del documento en español (excluyendo palabras específicas):")
for keyword in keywords:
    print(keyword)
