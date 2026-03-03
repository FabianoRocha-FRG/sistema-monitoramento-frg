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
st.markdown("<div class='titulo-principal'>ATLAS LEGISLATIVO<br>FRG CONSULTORIA POLÍTICA</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitulo'>Inteligência Legislativa | Estratégia Política | Relações Governamentais</div>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# -----------------------------
# QUEM SOMOS
# -----------------------------
st.markdown("## Quem Somos")

st.markdown("""
<div class='secao'>

A FRG é uma empresa de assessoria e consultoria em Relações Institucionais e Governamentais.
Nosso diferencial está na combinação de tecnologia, expertise política e atuação assertiva,
com foco em informações realmente relevantes.

Contamos com parcerias estratégicas junto a diversos atores políticos, o que nos permite
antecipar tendências e assegurar alto índice de sucesso em setores como energia,
tecnologia, infraestrutura e saúde.

Entregamos soluções personalizadas e de alto impacto, sempre alinhadas aos objetivos dos nossos clientes.

</div>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# -----------------------------
# SÓCIO-FUNDADOR
# -----------------------------
st.markdown("## Sócio-Fundador")

st.markdown("""
<div class='secao'>

Fabiano Rocha Guimarães possui mais de duas décadas de atuação no setor público federal.

Entre 2019 e 2025, foi Coordenador de Plenário da Liderança do Governo na Câmara dos Deputados,
atuando nos governos Bolsonaro e Lula, coordenando articulação política,
negociação de votações e análise de pautas estratégicas.

Mantém diálogo constante com parlamentares, equipes ministeriais e setor privado,
sendo reconhecido pela leitura estratégica do ambiente político e construção de consensos.

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
• Elaboração de Reports e Newsletters Semanais  
• Monitor Legislativo Completo  
• Agenda Legislativa e Resultados Semanais  
• Leitura Direcionada do Diário Oficial  
• Informes Estratégicos em Tempo Real  

• Mapeamento de Proposições e Stakeholders  
• Planejamento Estratégico  
• Análises de Cenário  
• Informações de Bastidores  
• Relacionamento com o Congresso Nacional  

</div>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# -----------------------------
# CASES DE SUCESSO
# -----------------------------
st.markdown("## Cases de Sucesso")

st.markdown("""
<div class='secao'>

✔ Manutenção de verbas indenizatórias extrateto  
✔ Inclusão de benefícios fiscais na Reforma Tributária  
✔ Aprovação de destaque no Estatuto da Segurança Privada  
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
# ÁREA RESTRITA
# -----------------------------
st.markdown("## Área Restrita")

if st.button("Acessar Plataforma Completa"):
    st.warning("A plataforma completa é exclusiva para clientes da FRG Consultoria Política.")
    st.markdown("""
    <div class='secao'>
    Para solicitar acesso institucional, entre em contato pelos canais oficiais.
    </div>
    """, unsafe_allow_html=True)

# Bloqueia qualquer sistema interno
st.stop()