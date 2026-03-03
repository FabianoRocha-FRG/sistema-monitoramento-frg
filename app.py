import streamlit as st

# -----------------------------
# CONFIGURAÇÃO DA PÁGINA
# -----------------------------
st.set_page_config(
    page_title="Atlas Legislativo FRG",
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
    font-size: 48px;
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

.botao-premium > button {
    background-color: #C6A54A;
    color: #0B0B0B;
    font-weight: 600;
    border-radius: 12px;
    padding: 10px 25px;
    border: none;
}

.botao-premium > button:hover {
    background-color: #E0C26E;
}

.contato {
    text-align:center;
    font-size:16px;
    margin-top:30px;
}

a {
    color:#C6A54A;
    text-decoration:none;
    font-weight:600;
}

a:hover {
    color:#E0C26E;
}

footer {visibility: hidden;}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# PÁGINA INICIAL INSTITUCIONAL
# -----------------------------
st.markdown("<div class='titulo-principal'>ATLAS LEGISLATIVO FRG</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitulo'>Plataforma de Inteligência e Monitoramento Legislativo Federal</div>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div style='text-align:center; max-width:750px; margin:auto; font-size:16px; line-height:1.7;'>

A FRG Consultoria Política atua na interface estratégica entre o setor público e o setor privado,
oferecendo inteligência legislativa, análise regulatória e monitoramento institucional
no âmbito do Congresso Nacional.

<br><br>

O Atlas Legislativo FRG é uma plataforma proprietária desenvolvida para acompanhamento legislativo,
gestão de risco regulatório e suporte estratégico à tomada de decisão institucional.

<br><br>

O acesso completo à plataforma é exclusivo para clientes da FRG Consultoria Política.

</div>
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# -----------------------------
# CONTATOS INSTITUCIONAIS
# -----------------------------
st.markdown("""
<div class='contato'>
📩 <a href="mailto:contato@frgconsultoriapolitica.com.br">contato@frgconsultoriapolitica.com.br</a><br><br>
📱 <a href="https://wa.me/5561992518004" target="_blank">WhatsApp FRG</a><br><br>
📷 <a href="https://instagram.com/frgconsultoriapolitica" target="_blank">@frgconsultoriapolitica</a>
</div>
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# -----------------------------
# BLOQUEIO DE ACESSO
# -----------------------------
if st.button("Solicitar Acesso à Plataforma"):

    st.warning("O acesso completo ao Atlas Legislativo FRG é exclusivo para clientes.")

    st.markdown("""
    <div style='text-align:center; font-size:16px; margin-top:15px;'>

    Para solicitar acesso, entre em contato pelos canais oficiais da FRG:

    <br><br>

    📩 <a href="mailto:contato@frgconsultoriapolitica.com.br">Enviar E-mail</a><br><br>
    📱 <a href="https://wa.me/5500000000000" target="_blank">Falar via WhatsApp</a><br><br>
    📷 <a href="https://instagram.com/frgconsultoriapolitica" target="_blank">Instagram FRG</a>

    </div>
    """, unsafe_allow_html=True)

# Impede qualquer acesso ao sistema
st.stop()