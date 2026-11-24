import streamlit as st

from src.reconhecimento import reconhecer_residuo

st.set_page_config(
    page_title="Ecokeras",
    page_icon="♻️",
    layout="centered"
)

st.title("♻️ Ecokeras")

st.subheader(
    "Inteligência Artificial para reconhecimento de resíduos"
)

st.write(
    "Envie uma imagem para identificar "
    "o material reciclável."
)

imagem = st.file_uploader(
    "Escolha uma imagem",
    type=["jpg", "jpeg", "png"]
)

if imagem is not None:

    st.image(
        imagem,
        caption="Imagem enviada",
        use_container_width=True
    )

    if st.button("Identificar resíduo"):

        try:
            with st.spinner("Analisando imagem..."):

                categoria, confianca = reconhecer_residuo(
                    imagem
                )

            st.success("Análise concluída!")

            st.subheader("Resultado da identificação")

            st.write(
                f"Material identificado: *{categoria.upper()}*"
            )

            st.write(
                f"Confiança da IA: *{confianca:.2f}%*"
            )

        except Exception as erro:

            st.error(
                f"Não foi possível analisar a imagem: {erro}"
            )

