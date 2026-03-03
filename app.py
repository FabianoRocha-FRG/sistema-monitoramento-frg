import streamlit as st

# -----------------------------
# CONFIGURAÇÃO DA PÁGINA
# -----------------------------
st.set_page_config(
    page_title="Atlas Legislativo - FRG Consultoria Política",
    page_icon="⚖️",
    layout="wide"
)

# -----------------------------
# IDENTIDADE VISUAL PRETO & DOURADO
# -----------------------------
st.markdown("""
<style>
.stApp {
    background-color: #0B0B0B;
    color: #FFFFFF;
}

.titulo-principal {
    color: #C6A54A;
    font-size: 46px;
    font-weight: 700;
    text-align: center;
    text-shadow: 0px 0px 18px rgba(198,165,74,0.7);
    letter-spacing: 2px;
}

.subtitulo {
    color: #FFFFFF;
    font-size: 18px;
    text-align: center;
    font-weight: 300;
}

.secao {
    max-width: 800px;
    margin: auto;
    text-align: center;
    font-size: 16px;
    line-height: 1.7;
}

hr {
    border: 1px solid #C6A54A;
}

a {
    color:#C6A54A;
    text-decoration:none;
    font-weight:600;
}

a:hover {
    color:#E0C26E;
}

.botao-acesso > button {
    background-color: #C6A54A;
    color: #0B0B0B;
    font-weight: 600;
    border-radius: 12px;
    padding: 10px 25px;
    border: none;
}

footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# CABEÇALHO
# -----------------------------
st.markdown(
    "<div class='titulo-principal'>ATLAS LEGISLATIVO<br>FRG CONSULTORIA POLÍTICA</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitulo'>Plataforma de Inteligência e Monitoramento Legislativo Federal</div>",
    unsafe_allow_html=True
)

st.markdown("<hr>", unsafe_allow_html=True)

# -----------------------------
# SOBRE
# -----------------------------
st.markdown("""
<div class='secao'>

A FRG Consultoria Política atua na interface estratégica entre o setor público e o setor privado,
oferecendo inteligência legislativa, análise regulatória e monitoramento institucional
no âmbito do Congresso Nacional.

<br><br>

O Atlas Legislativo é a plataforma proprietária da FRG Consultoria Política,
desenvolvida para acompanhamento legislativo estruturado, gestão de risco regulatório
e suporte estratégico à tomada de decisão institucional.

</div>
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# -----------------------------
# CONTATOS
# -----------------------------
st.markdown("""
<div class='secao'>
📩 <a href="mailto:contato@frgconsultoriapolitica.com.br">contato@frgconsultoriapolitica.com.br</a><br>
📱 <a href="https://wa.me/5561992518004" target="_blank">WhatsApp FRG</a><br>
📷 <a href="https://instagram.com/frgconsultoriapolitica" target="_blank">@frgconsultoriapolitica</a>
</div>
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# -----------------------------
# ACESSO RESTRITO
# -----------------------------
st.markdown("<hr>", unsafe_allow_html=True)

if st.button("Área Restrita - Clientes FRG"):
    st.warning("A plataforma completa é exclusiva para clientes da FRG Consultoria Política.")
    st.markdown("""
    <div class='secao'>
    Para solicitar acesso institucional, entre em contato pelos canais oficiais da FRG.
    </div>
    """, unsafe_allow_html=True)

# Bloqueio do sistema interno
st.stop()