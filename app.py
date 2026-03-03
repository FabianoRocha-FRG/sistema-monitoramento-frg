# -----------------------------
# IDENTIDADE VISUAL FRG - PRETO & DOURADO
# -----------------------------
st.markdown("""
<style>

/* Fundo geral */
.stApp {
    background-color: #0B0B0B;
    color: #FFFFFF;
}

/* Títulos */
h1, h2, h3, h4 {
    color: #C6A54A;
    font-family: 'Segoe UI', sans-serif;
    letter-spacing: 1px;
}

/* Texto padrão */
p, label, div {
    color: #FFFFFF;
}

/* Linha divisória */
hr {
    border: 1px solid #C6A54A;
}

/* Remove rodapé padrão Streamlit */
footer {visibility: hidden;}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# TÍTULO PRINCIPAL INSTITUCIONAL
# -----------------------------
st.markdown("""
<div style='text-align: center; padding-top: 10px;'>
    <h1 style='font-size: 42px; margin-bottom: 5px;'>
        ATLAS LEGISLATIVO FRG
    </h1>
    <h4 style='color: #FFFFFF; font-weight: 300; margin-top: 0px;'>
        Plataforma de Inteligência e Monitoramento Legislativo Federal
    </h4>
</div>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)