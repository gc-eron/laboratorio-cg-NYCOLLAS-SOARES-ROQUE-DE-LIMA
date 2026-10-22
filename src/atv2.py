import numpy as np
import streamlit as st


def ampliar(imagem, k=30):
    """Amplia a imagem de pixels repetindo linhas e colunas."""
    return imagem.repeat(k, axis=0).repeat(k, axis=1)


st.title("Atividade 2 — Imagem como matriz")
st.write("Desenhando uma bandeira com NumPy e exibindo seus pixels no Streamlit.")

# Bandeira da Colômbia: 12 linhas, 18 colunas e três canais (R, G, B).
bandeira = np.zeros((12, 18, 3), dtype=np.uint8)

# A metade superior é amarela. As outras duas faixas têm 1/4 cada.
bandeira[:6, :] = (252, 209, 22)   # Amarelo
bandeira[6:9, :] = (0, 56, 147)    # Azul
bandeira[9:, :] = (206, 17, 38)    # Vermelho

st.subheader("Bandeira da Colômbia")
st.image(
    ampliar(bandeira),
    caption="Bandeira desenhada em pixels com uma matriz NumPy RGB (12 × 18).",
    width=540,
)
st.write("Formato (altura, largura, canais RGB):", bandeira.shape)
st.write("Cores utilizadas: amarelo (252, 209, 22), azul (0, 56, 147) e vermelho (206, 17, 38).")

st.divider()
st.header("Experimentos da aula")

# Experimento 1: 8 x 8 pixels pretos.
imagem_preta = np.zeros((8, 8), dtype=np.uint8)
st.subheader("1. Imagem preta")
st.image(ampliar(imagem_preta), width=240)
st.write(imagem_preta)

# Experimento 2: um pixel branco na linha 2, coluna 5.
imagem_pixel = imagem_preta.copy()
imagem_pixel[2, 5] = 255
st.subheader("2. Um pixel branco")
st.image(ampliar(imagem_pixel), width=240)
st.write(imagem_pixel)

# Experimento 3: pintar a metade inferior de cinza.
imagem_metade = imagem_pixel.copy()
imagem_metade[4:, :] = 128
st.subheader("3. Metade inferior cinza")
st.image(ampliar(imagem_metade), width=240)
st.write(imagem_metade)

# Experimento 4: exemplo com três faixas de cores RGB.
faixas = np.zeros((6, 9, 3), dtype=np.uint8)
faixas[:2, :] = (110, 50, 150)   # Roxo
faixas[2:4, :] = (240, 190, 40) # Dourado
faixas[4:, :] = (30, 160, 150)  # Turquesa
st.subheader("4. Imagem colorida (RGB)")
st.image(ampliar(faixas), width=270)
st.write("Formato da matriz:", faixas.shape)
