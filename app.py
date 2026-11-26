import streamlit as st

from src.reconhecimento import reconhecer_residuo

st.set_page_config(
    page_title="Ecokeras",
    page_icon="♻️",
    layout="centered"
)

st.markdown("""

<style>

.stApp {

    background-color: black;

}
st.title{
color: #8BC34A
}

h1 {

    color: forestgreen;

    text-align: center;

}

h2 {
    color: #A8C99A;

}

h3 {
    color:#F3F1E7;
}
p, label {

    color: #354B3D;

}

.stButton > button {

    background-color: yellow;

    color: white;

    border-radius: 10px;

    border: none;

    padding: 10px 25px;

    font-weight: bold;

}

.stButton > button:hover {

    background-color: yellow;

    color: white;

}

section[data-testid="stFileUploader"] {

    background-color: #C5E8A5;

    border-radius: 12px;

    padding: 15px;

}




[data-testid="stFileUploader"] section {
    background-color: white !important;
    border: 2px solid white !important;
    border-radius: 12px;
}


[data-testid="stFileUploader"] small {
    color: #354B3D !important;
}


[data-testid="stFileUploader"] button {
    background-color: #8BC34A !important;
    color: white !important;
}

</style>

""", unsafe_allow_html=True)



st.markdown('<h1 style="color: #8BC34A" >♻️ Ecokeras</h1>', unsafe_allow_html=True)
st.markdown('<h3 style="color: #F3F1E7;" >Inteligência Artificial para reconhecimento de resíduos</h3>', unsafe_allow_html=True)

col1, col2 , col3, col4 = st.columns(4)
with col1:
    with st.container(border=True):
        st.markdown('<h3 style="color: #347A50;" >Nossa história</h3>', unsafe_allow_html=True)
        st.markdown('<p style="color: white;" >A equipe notou o quanto o meio ambiente é importante e o quanto ele deve ser valorizado.</p>', unsafe_allow_html=True)
        
with col2:
    with st.container(border=True):
        st.markdown('<h3 style="color: #347A50;" >Nosso propósito</h3>', unsafe_allow_html=True)
        st.markdown('<p style="color: white;" >Utilizar a tecnologia para incentivar a reciclagem e a preservação do meio ambiente</p>', unsafe_allow_html=True)
with col3:
    with st.container(border=True):
            st.markdown('<p style="color: white;" >A produção de resíduos sólidos faz parte da vida cotidiana, sendo resultado das atividades domésticas, comerciais e industriais. Entretanto, o crescimento do consumo e o descarte inadequado desses materiais representam desafios importantes para a preservação ambiental.</p>', unsafe_allow_html=True)
with col4:
    with st.container(border=True):


        st.markdown('<p style="color: green;" >Verde: </p>', unsafe_allow_html=True)
        st.markdown('<p style="color: white;" >Vidro (Garrafas, potes, frascos e copos </p>', unsafe_allow_html=True)
        
        st.markdown('<p style="color: red;" >Vermelho: </p>', unsafe_allow_html=True)
        st.markdown('<p style="color: white;" >Plástico (garrafas PET, sacolas, potes, embalagens)</p>', unsafe_allow_html=True)
        st.markdown('<p style="color: blue;" >Azul: </p>', unsafe_allow_html=True)
        st.markdown('<p style="color: white;" >Papel e papelão (jornais, revistas, caixas, folhas)</p>', unsafe_allow_html=True)
        st.markdown('<p style="color: brown;" >Marrom: </p>', unsafe_allow_html=True)
        st.markdown('<p style="color: white;" >Orgânico (restos de alimentos, cascas de frutas e verduras)</p>', unsafe_allow_html=True)
        st.markdown('<p style="color: yellow;" >Amarelo: </p>', unsafe_allow_html=True)
        st.markdown('<p style="color: white;" >Metal (latas de alúminio e aço, tampas, embalagens metálicas)</p>', unsafe_allow_html=True)

st.markdown('<h3 style="color:  #8BC34A;" >Nossa IA tem como objetivo identificar o material reciclável  a partir de uma imagem enviada pelo usuário</h3>', unsafe_allow_html=True)

st.markdown(
    """
    <p style="color: white; ">Envie uma imagem para identificar o material reciclável. </p>
   
    """,
    unsafe_allow_html=True
)
imagem = st.file_uploader(
    "Escolha uma imagem", 
    type=["jpg", "jpeg", "png",]
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
