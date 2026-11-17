from pathlib import Path

import numpy as np
import streamlit as st
from PIL import Image, ImageOps, UnidentifiedImageError

st.title("Atv 4: RGB")

caminho_foto = Path(__file__).resolve().parents[1] / "imagens" / "foto.jpg"

st.header("1. Leitura da foto")
col1, col2 = st.columns(2)

fonte = caminho_foto
if not caminho_foto.is_file():
    fonte = col1.file_uploader("Selecione sua fotografia", type=["jpg", "jpeg", "png"])
    if fonte is None:
        col2.info("Selecione uma foto ou salve-a como imagens/foto.jpg na raiz do projeto.")
        st.stop()

try:
    with Image.open(fonte) as foto:
        img = np.array(ImageOps.exif_transpose(foto).convert("RGB"))
except (UnidentifiedImageError, OSError):
    st.error("Não foi possível abrir a fotografia. Confira o arquivo selecionado.")
    st.stop()

col1.image(img, caption="Fotografia em RGB")
col2.text(f"Dimensões (altura, largura, canais): {img.shape}")
if img.shape[0] > 100 and img.shape[1] > 100:
    col2.text(f"Pixel (100, 100): {img[100, 100]}")
else:
    col2.info("O pixel (100, 100) exige uma foto com pelo menos 101 × 101 pixels.")

st.header("2. Canais")
col1, col2 = st.columns(2)

for indice, canal in enumerate(("R", "G", "B")):
    intensidade = img[:, :, indice]
    col1.image(intensidade, caption=canal)

    isolado = np.zeros_like(img)
    isolado[:, :, indice] = intensidade
    col2.image(isolado, caption=f"Só {canal}")

st.header("3. Cubo e BGR")
col1, col2 = st.columns(2)

vertices = {
    "Amarelo": (255, 255, 0),
    "Vermelho": (255, 0, 0),
    "Verde": (0, 255, 0),
    "Azul": (0, 0, 255),
}
for nome, rgb in vertices.items():
    quadrado = np.zeros((80, 80, 3), dtype=np.uint8)
    quadrado[:, :] = rgb
    col1.image(quadrado, caption=f"{nome} {rgb}")

col2.image(img, channels="BGR", caption="Foto interpretada como BGR")

st.header("4. Tons de cinza")
col1, col2 = st.columns(2)

r = img[:, :, 0].astype(float)
g = img[:, :, 1].astype(float)
b = img[:, :, 2].astype(float)
media = ((r + g + b) / 3).astype(np.uint8)
ponderada = (0.299 * r + 0.587 * g + 0.114 * b).astype(np.uint8)
col1.image(media, caption="Média")
col2.image(ponderada, caption="Média ponderada")


