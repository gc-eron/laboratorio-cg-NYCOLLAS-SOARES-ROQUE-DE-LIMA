from pathlib import Path

import streamlit as st

raiz = Path(__file__).resolve().parent

st.set_page_config(
    page_title="Laboratório de Computação Gráfica",
    layout="centered",
)

# Cada atividade fica em seu próprio arquivo na pasta src.
paginas = [
    st.Page(str(raiz / "src/atv1.py"), title="Atv 1"),
    st.Page(str(raiz / "src/atv2.py"), title="Atv 2"),
    st.Page(str(raiz / "src/atv4.py"), title="Atv 4"),
    st.Page(str(raiz / "src/atv5.py"), title="Atv 5"),
    st.Page(str(raiz / "src/trabalho.py"), title="Trabalho"),
]

st.navigation(paginas).run()

