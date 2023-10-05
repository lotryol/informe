import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import spacy
import fitz
from docx import Document
import string
import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Descargar recursos de NLTK si no están disponibles
nltk.download("punkt")
nltk.download("stopwords")

# Configurar spaCy con el modelo de idioma en español
nlp = spacy.load("es_core_news_sm")

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
document_path = "docs/FORMATO INFORME DE PASANTIA v 2023-1.pdf"  # Reemplaza con la ruta de tu documento PDF o Word

# Extraer el texto del documento
if document_path.endswith(".pdf"):
    text = extract_text_from_pdf(document_path)
elif document_path.endswith(".docx"):
    text = extract_text_from_word(document_path)
else:
    print("Formato de archivo no compatible.")
    exit()

# Ejemplo de texto
texto = text

# Paso 4: Eliminación de caracteres especiales y signos de puntuación
texto = "".join([char for char in texto if char not in string.punctuation])

# Tokenización con NLTK
tokens_nltk = word_tokenize(texto, language="spanish")

# Eliminación de Stop Words con NLTK
stop_words = set(stopwords.words("spanish"))
filtered_tokens_nltk = [word for word in tokens_nltk if word.lower() not in stop_words]

# Lematización con spaCy
doc = nlp(texto)
lemmas_spacy = [token.lemma_ for token in doc]

# Paso 7: Construcción de Secuencias
# Definir la longitud máxima de las secuencias
max_seq_length = 50  # Puedes ajustar esta longitud según tus necesidades

# Convertir tokens a secuencias de índices
tokenizer = Tokenizer(num_words=100, oov_token="<OOV>")
tokenizer.fit_on_texts(lemmas_spacy)
sequences = tokenizer.texts_to_sequences(lemmas_spacy)

# Paso 8: Padding o Truncamiento
# Pad o trunca las secuencias para que tengan la misma longitud
padded_sequences = pad_sequences(sequences, maxlen=max_seq_length, padding="post", truncating="post")

# Imprimir resultados
print("Texto original:")
print(texto)
print("\nTokens (NLTK):")
print(tokens_nltk)
print("\nTokens sin Stop Words (NLTK):")
print(filtered_tokens_nltk)
print("\nLematización (spaCy):")
print(lemmas_spacy)
print("\nSecuencias de Índices:")
print(sequences)
print("\nSecuencias de Índices con Padding:")
print(padded_sequences)
