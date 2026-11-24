import cv2
import numpy as np
import streamlit as st
from PIL import Image
from pathlib import Path

st.title("Trabalho de Computação Gráfica")
st.write("Ajuste os controles para observar cinco operações na foto.")

raiz = Path(__file__).resolve().parents[1]
foto = Image.open(raiz / "imagens" / "foto.png").convert("RGB")
imagem = np.array(foto)

st.header("1. Saturação")
saturacao = st.slider("Intensidade da saturação (%)", 0, 200, 100)
hsv_saturacao = cv2.cvtColor(imagem, cv2.COLOR_RGB2HSV)
hsv_saturacao[:, :, 1] = np.clip(hsv_saturacao[:, :, 1] * saturacao / 100, 0, 255).astype(np.uint8)
resultado_saturacao = cv2.cvtColor(hsv_saturacao, cv2.COLOR_HSV2RGB)
st.image(resultado_saturacao, caption="Foto com saturação ajustada", use_container_width=True)

st.header("2. Brilho")
brilho = st.slider("Ajuste do brilho", -100, 100, 0)
hsv_brilho = cv2.cvtColor(imagem, cv2.COLOR_RGB2HSV)
hsv_brilho[:, :, 2] = np.clip(hsv_brilho[:, :, 2].astype(np.int16) + brilho, 0, 255).astype(np.uint8)
resultado_brilho = cv2.cvtColor(hsv_brilho, cv2.COLOR_HSV2RGB)
st.image(resultado_brilho, caption="Foto com brilho ajustado", use_container_width=True)

st.header("3. Matiz girada")
giro = st.slider("Giro da matiz", 0, 179, 0)
hsv_matiz = cv2.cvtColor(imagem, cv2.COLOR_RGB2HSV)
hsv_matiz[:, :, 0] = (hsv_matiz[:, :, 0].astype(np.int16) + giro) % 180
resultado_matiz = cv2.cvtColor(hsv_matiz, cv2.COLOR_HSV2RGB)
st.image(resultado_matiz, caption="Foto com matiz girada", use_container_width=True)

st.header("4. Tons de cinza")
metodo_cinza = st.selectbox("Método para calcular o cinza", ["Média simples", "Média ponderada"])
if metodo_cinza == "Média simples":
    cinza = np.mean(imagem, axis=2)
else:
    cinza = 0.299 * imagem[:, :, 0] + 0.587 * imagem[:, :, 1] + 0.114 * imagem[:, :, 2]
resultado_cinza = np.stack((cinza, cinza, cinza), axis=2).astype(np.uint8)
st.image(resultado_cinza, caption="Foto em tons de cinza", use_container_width=True)

st.header("5. Negativo")
resultado_negativo = 255 - imagem
st.image(resultado_negativo, caption="Negativo da foto", use_container_width=True)
