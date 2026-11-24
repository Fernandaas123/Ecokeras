import tensorflow as tf
import keras
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

CAMINHO_DATASET = BASE_DIR / "dataset"
CAMINHO_MODELOS = BASE_DIR / "src" / "modelos"

TAM_IMG = (180, 180)
LOTE = 32
EPOCAS = 15


treinamento = keras.utils.image_dataset_from_directory(
    CAMINHO_DATASET,
    validation_split=0.2,
    subset="training",
    seed=123,
    image_size=TAM_IMG,
    batch_size=LOTE
)

validation = keras.utils.image_dataset_from_directory(
    CAMINHO_DATASET,
    validation_split=0.2,
    subset="validation",
    seed=123,
    image_size=TAM_IMG,
    batch_size=LOTE
)

classes = treinamento.class_names

print("Categorias:", classes)

AUTOTUNE = tf.data.AUTOTUNE

treinamento = treinamento.prefetch(
    buffer_size=AUTOTUNE
)

validation = validation.prefetch(
    buffer_size=AUTOTUNE
)


modelo = keras.Sequential([
    keras.Input(shape=(180, 180, 3)),

    keras.layers.Rescaling(1./255),

    keras.layers.Conv2D(32, 3, activation="relu"),
    keras.layers.MaxPooling2D(),

    keras.layers.Conv2D(64, 3, activation="relu"),
    keras.layers.MaxPooling2D(),

    keras.layers.Conv2D(128, 3, activation="relu"),
    keras.layers.MaxPooling2D(),

    keras.layers.Flatten(),

    keras.layers.Dense(128, activation="relu"),

    keras.layers.Dropout(0.3),

    keras.layers.Dense(
        len(classes),
        activation="softmax"
    )
])

modelo.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)


historico = modelo.fit(
    treinamento,
    validation_data=validation,
    epochs=EPOCAS
)


CAMINHO_MODELOS.mkdir(parents=True, exist_ok=True)

modelo.save(CAMINHO_MODELOS / "ecokeras.keras")

with open(
    CAMINHO_MODELOS / "classes.json",
    "w",
    encoding="utf-8"
) as arquivo:
    json.dump(classes, arquivo, ensure_ascii=False)

print("IA treinada com sucesso!")


