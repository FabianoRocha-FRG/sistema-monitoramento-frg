import streamlit as st

# -----------------------------
# CONFIGURAÇÃO
# -----------------------------
st.set_page_config(
    page_title="Atlas Legislativo - FRG Consultoria Política",
    page_icon="⚖️",
    layout="wide"
)

# -----------------------------
# IDENTIDADE VISUAL
# -----------------------------
st.markdown("""
<style>
.stApp { background-color: #0B0B0B; color: #FFFFFF; }

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
# MENU SUPERIOR
# -----------------------------
menu = st.radio(
    "",
    ["Home", "Quem Somos", "Serviços", "Cases", "Contato", "Plataforma"],
    horizontal=True
)

st.markdown("<hr>", unsafe_allow_html=True)

# -----------------------------
# HOME
# -----------------------------
if menu == "Home":

    st.markdown("<div class='titulo-principal'>ATLAS LEGISLATIVO<br>FRG CONSULTORIA POLÍTICA</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitulo'>Inteligência Legislativa | Estratégia Política | Relações Governamentais</div>", unsafe_allow_html=True)

    st.image("https://upload.wikimedia.org/wikipedia/commons/3/3f/Congresso_Nacional_-_Bras%C3%ADlia_-_DF.jpg", use_container_width=True)

    st.markdown("""
    <div class='secao'>
    O Atlas Legislativo é a plataforma proprietária da FRG Consultoria Política,
    desenvolvida para monitoramento estratégico do Congresso Nacional,
    análise regulatória e articulação institucional de alto nível.
    </div>
    """, unsafe_allow_html=True)

# -----------------------------
# QUEM SOMOS
# -----------------------------
elif menu == "Quem Somos":

    st.markdown("## Quem Somos")

    st.image("https://upload.wikimedia.org/wikipedia/commons/9/95/Congresso_Nacional_plen%C3%A1rio.jpg", use_container_width=True)

    st.markdown("""
    <div class='secao'>
    A FRG é uma empresa especializada em Relações Institucionais e Governamentais.
    Atuamos com inteligência legislativa, monitoramento estratégico e articulação política.

    Nosso diferencial está na combinação entre tecnologia, expertise política
    e atuação assertiva, com foco em informações realmente relevantes.
    </div>
    """, unsafe_allow_html=True)

# -----------------------------
# SERVIÇOS
# -----------------------------
elif menu == "Serviços":

    st.markdown("## Serviços Oferecidos")

    st.markdown("""
    <div class='secao'>

    • Acompanhamento Legislativo Prioritário  
    • Monitor Legislativo Completo  
    • Elaboração de Reports e Newsletters  
    • Agenda Legislativa e Informes em Tempo Real  
    • Mapeamento de Stakeholders  
    • Planejamento Estratégico  
    • Análises de Cenário  
    • Relacionamento Institucional  

    </div>
    """, unsafe_allow_html=True)

# -----------------------------
# CASES
# -----------------------------
elif menu == "Cases":

    st.markdown("## Cases de Sucesso")

    st.markdown("""
    <div class='secao'>

    ✔ Manutenção de verbas indenizatórias extrateto  
    ✔ Inclusão de benefícios fiscais na Reforma Tributária  
    ✔ Aprovação de destaque no Senado Federal  
    ✔ Apresentação e aprovação de emendas  
    ✔ Construção e aprovação de propostas normativas  

    </div>
    """, unsafe_allow_html=True)

# -----------------------------
# CONTATO
# -----------------------------
elif menu == "Contato":

    st.markdown("## Contato Institucional")

    st.markdown("""
    <div class='secao'>

    📍 SCN Quadra 04, Bloco B, Ed. Varig, Sala 702 – Brasília/DF  
    📩 <a href="mailto:contato@frgconsultoriapolitica.com.br">contato@frgconsultoriapolitica.com.br</a>  
    📱 <a href="https://wa.me/5561992518004" target="_blank">(61) 9 9251-8004</a>  
    📷 <a href="https://instagram.com/frgconsultoriapolitica" target="_blank">@frgconsultoriapolitica</a>

    </div>
    """, unsafe_allow_html=True)

# -----------------------------
# PLATAFORMA (BLOQUEADA)
# -----------------------------
elif menu == "Plataforma":

    st.warning("A Plataforma Atlas Legislativo é exclusiva para clientes da FRG Consultoria Política.")
    st.markdown("""
    <div class='secao'>
    Para solicitar acesso institucional, entre em contato pelos canais oficiais.
    </div>
    """, unsafe_allow_html=True)

    st.stop()