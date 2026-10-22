# Laboratório de Computação Gráfica

Projeto com menu Streamlit e atividades organizadas em arquivos separados.

## Executar no Windows

Abra o CMD na pasta `laboratorio-cg` e execute:

```cmd
uv sync
uv run streamlit run app.py
```

Abra o link exibido no terminal (geralmente http://localhost:8501) e, no menu lateral, escolha **Atv 2** para ver a bandeira da Colômbia e os experimentos de imagem como matriz.

## Estrutura

```text
laboratorio-cg/
├── app.py                 # Menu do Streamlit
├── src/
│   ├── atv1.py            # Página da atividade 1
│   ├── atv2.py            # Bandeira RGB e experimentos
│   └── laboratorio_cg/    # Pacote original criado pelo uv
│       └── __init__.py
├── pyproject.toml
└── uv.lock
```

## Nota sobre o arquivo original

No ZIP recebido, `src/laboratorio_cg/app.py` e `src/laboratorio_cg/atv2.py` estavam vazios, e não existia um `app.py` na raiz. Foi criado o menu exigido pela aula, assim como a página da bandeira. A **Atv 1** foi reconstruída como uma página simples, porque seu conteúdo original não estava no ZIP.

O pacote de correção não inclui `.git/` nem `.venv/` (são arquivos locais desnecessários para compartilhar). **Ao copiar esses arquivos para a pasta original, mantenha a pasta `.git` existente** para continuar usando `git add`, `git commit` e `git push` normalmente.
