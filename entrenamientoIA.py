import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np

# Datos de entrenamiento
sentences = [
    "Me encanta esta película, es increíble.",
    "No me gustó el final, fue aburrido.",
    "El libro es genial, lo recomiendo.",
    "No volvería a ver eso nunca más.",
    "Esta comida es deliciosa, definitivamente regresaré.",
    "El servicio en este restaurante es terrible, no lo recomendaría.",
    "Me encantó la actuación de los actores en esa película.",
    "El clima hoy es perfecto para pasar el día al aire libre.",
    "El tráfico en la ciudad durante la hora punta es insoportable.",
    "Este concierto fue fenomenal, lo pasé genial.",
    "La conferencia fue aburrida, no aprendí nada nuevo.",
    "Las vacaciones en la playa fueron relajantes y maravillosas.",
    "Odio tener que hacer tanta tarea todos los días.",
    "El nuevo videojuego es adictivo, no puedo dejar de jugar.",
    "La presentación de ayer en la reunión de trabajo fue desastrosa.",
    "El parque de atracciones estaba lleno de diversión y emoción.",
    "Este hotel es horrible, la habitación estaba sucia y ruidosa.",
    "El concierto de anoche fue decepcionante, no cumplieron las expectativas.",
    "Me encanta esta canción, no puedo dejar de escucharla.",
    "El museo tenía una colección impresionante de arte.",
    "Este juego es aburrido",
    "Estoy cansado Jefe"
]

labels = [1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0]
# 1 para sentimientos positivos, 0 para sentimientos negativos

# Tokenización y preprocesamiento de texto
tokenizer = Tokenizer(num_words=100, oov_token="<OOV>")
tokenizer.fit_on_texts(sentences)
word_index = tokenizer.word_index
sequences = tokenizer.texts_to_sequences(sentences)
padded_sequences = pad_sequences(sequences, maxlen=5, padding="post", truncating="post")

# Convierte tus listas de secuencias y etiquetas a arrays numpy
padded_sequences = np.array(padded_sequences)
labels = np.array(labels)

# Construcción del modelo
model = keras.Sequential([
    keras.layers.Embedding(input_dim=len(word_index) + 1, output_dim=16, input_length=10),
    keras.layers.Flatten(),
    keras.layers.Dense(6, activation="relu"),
    keras.layers.Dense(1, activation="sigmoid")
])

model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])

# Entrenamiento del modelo
model.fit(padded_sequences, labels, epochs=1000)

# Guardar el modelo entrenado
model.save("modelo.h5")
