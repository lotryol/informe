import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np

# Cargar el modelo entrenado
model = keras.models.load_model("modelo.h5")


# Define el nombre del archivo de texto
nombre_archivo = "inputs.txt"

# Inicializa una lista vacía para almacenar las oraciones
oraciones = []

# Abre el archivo de texto en modo lectura
with open(nombre_archivo, "r", encoding="utf-8") as archivo:
    # Lee cada línea del archivo (cada línea debe contener una oración)
    for linea in archivo:
        # Elimina los espacios en blanco y caracteres especiales al principio y al final de la línea
        linea = linea.strip()
        # Añade la línea a la lista de oraciones
        oraciones.append(linea)

# Ahora, la lista 'oraciones' contiene todas las oraciones del archivo
# Puedes acceder a las oraciones individualmente o realizar cualquier operación que desees con ellas.

# oracion = ""
# Nuevas frases para predecir el sentimiento
# for oracion in oraciones:
    # prediction = [[0]]
    # print(prediction)
    # print(oracion)
    oracion = input()
    test_sentence = [oracion]
    tokenizer = Tokenizer(num_words=100, oov_token="<OOV>")
    print("soy el tokenizer")
    print(tokenizer)
    tokenizer.fit_on_texts(test_sentence)
    test_sequence = tokenizer.texts_to_sequences(test_sentence)
    print("spy el test_secuence")
    print(test_sequence)
    test_padded = pad_sequences(test_sequence, maxlen=10, padding="post", truncating="post")
    print("soy el test_padded")
    print(test_padded)

    # Hacer predicciones
    prediction = model.predict(test_padded)
    print(prediction)

    if prediction >= 0.5:
        print("Sentimiento positivo")
    else:
        print("Sentimiento negativo")
