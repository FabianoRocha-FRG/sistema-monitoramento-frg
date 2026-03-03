import streamlit as st
import os

# -----------------------------
# CONFIGURAÇÃO DA PÁGINA
# -----------------------------
st.set_page_config(
    page_title="Atlas Legislativo – FRG Consultoria Política",
    page_icon="⚖️",
    layout="wide"
)

# -----------------------------
# CAMINHO DAS IMAGENS
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

logo_path = os.path.join(BASE_DIR, "assets", "logo_frg.png")
congresso_path = os.path.join(BASE_DIR, "assets", "imagem_congresso.jpg")
plenario_path = os.path.join(BASE_DIR, "assets", "imagem_plenario.jpg")

# -----------------------------
# IDENTIDADE VISUAL
# -----------------------------
st.markdown("""
<style>
.stApp { background-color: #0B0B0B; color: #FFFFFF; }

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

.secao {
    max-width: 900px;
    margin: auto;
    font-size: 16px;
    line-height: 1.8;
}

hr { border: 1px solid #C6A54A; }

a { color:#C6A54A; text-decoration:none; font-weight:600; }
a:hover { color:#E0C26E; }

footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# HEADER
# -----------------------------
st.image(logo_path, width=200)

st.markdown(
    "<div class='titulo-principal'>ATLAS LEGISLATIVO<br>FRG CONSULTORIA POLÍTICA</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitulo'>Inteligência Legislativa | Estratégia Política | Relações Governamentais</div>",
    unsafe_allow_html=True
)

st.markdown("<hr>", unsafe_allow_html=True)

# -----------------------------
# IMAGEM INSTITUCIONAL
# -----------------------------
st.image(congresso_path, use_container_width=True)

# -----------------------------
# QUEM SOMOS
# -----------------------------
st.markdown("## Quem Somos")

st.image(plenario_path, use_container_width=True)

st.markdown("""
<div class='secao'>

A FRG Consultoria Política atua na interface estratégica entre o setor público e o setor privado,
oferecendo inteligência legislativa, análise regulatória e monitoramento institucional
no âmbito do Congresso Nacional.

Combinamos tecnologia, expertise política e articulação institucional
para oferecer soluções estratégicas de alto impacto,
sempre alinhadas aos objetivos dos nossos clientes.

</div>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# -----------------------------
# SERVIÇOS
# -----------------------------
st.markdown("## Serviços Oferecidos")

st.markdown("""
<div class='secao'>

• Acompanhamento Legislativo Prioritário  
• Monitor Legislativo Completo  
• Reports Estratégicos e Newsletters  
• Informes em Tempo Real  
• Mapeamento de Stakeholders  
• Planejamento Estratégico  
• Análises de Cenário  
• Relacionamento Institucional  

</div>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# -----------------------------
# CASES
# -----------------------------
st.markdown("## Cases de Sucesso")

st.markdown("""
<div class='secao'>

✔ Manutenção de verbas indenizatórias extrateto  
✔ Inclusão de benefícios fiscais na Reforma Tributária  
✔ Aprovação de destaque no Senado Federal  
✔ Apresentação e aprovação de emendas parlamentares  
✔ Construção e aprovação de propostas normativas  

</div>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# -----------------------------
# CONTATO
# -----------------------------
st.markdown("## Contato")

st.markdown("""
<div class='secao'>

📍 SCN Quadra 04, Bloco B, Ed. Varig, Sala 702 – Brasília/DF  
📩 <a href="mailto:contato@frgconsultoriapolitica.com.br">contato@frgconsultoriapolitica.com.br</a>  
📱 <a href="https://wa.me/5561992518004" target="_blank">(61) 9 9251-8004</a>  
📷 <a href="https://instagram.com/frgconsultoriapolitica" target="_blank">@frgconsultoriapolitica</a>

</div>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# -----------------------------
# PLATAFORMA (BLOQUEADA)
# -----------------------------
st.markdown("## Plataforma Atlas Legislativo")

if st.button("Acessar Plataforma Completa"):
    st.warning("A Plataforma Atlas Legislativo é exclusiva para clientes da FRG Consultoria Política.")
    st.markdown("""
    <div class='secao'>
    Para solicitar acesso institucional, entre em contato pelos canais oficiais.
    </div>
    """, unsafe_allow_html=True)

st.stop()