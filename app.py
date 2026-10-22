import streamlit as st

st.set_page_config(
    page_title="Laboratório de Computação Gráfica",
    layout="centered",
)

# Cada atividade fica em seu próprio arquivo na pasta src.
paginas = [
    st.Page("src/atv1.py", title="Atv 1"),
    st.Page("src/atv2.py", title="Atv 2"),
]

st.navigation(paginas).run()
