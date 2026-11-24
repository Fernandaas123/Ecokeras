
import keras
import numpy as np
import json

from pathlib import Path
from PIL import Image

BASE_DIR = Path(__file__).resolve().parent.parent
CAMINHO_MODELOS = BASE_DIR / "src" / "modelos"

modelo = keras.models.load_model(
    CAMINHO_MODELOS / "ecokeras.keras"
)

with open(
    CAMINHO_MODELOS / "classes.json",
    "r",
    encoding="utf-8"
) as arquivo:
    classes = json.load(arquivo)


def reconhecer_residuo(caminho_imagem):

    imagem = Image.open(caminho_imagem)

    imagem = imagem.convert("RGB")

    imagem = imagem.resize((180, 180))

    imagem = np.array(imagem)

    imagem = np.expand_dims(imagem, axis=0)

    previsao = modelo.predict(imagem, verbose=0)

    classe_predita = np.argmax(previsao[0])

    categoria = classes[classe_predita]

    confianca = float(
        previsao[0][classe_predita] * 100
    )

    return categoria, confianca
