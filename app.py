import streamlit as st
import time

st.set_page_config(
    page_title="Quennie Valenzuela Portfolio",
    page_icon="👑",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
html, body, [class*="css"]  { font-family: 'Poppins', sans-serif; }
.main-header {
    font-size: 4rem !important;
    background: linear-gradient(45deg, #FF69B4, #FF1493, #FF69B4, #FFB6C1);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-align: center;
    animation: glow 2s ease-in-out infinite alternate;
}
@keyframes glow { from { text-shadow: 0 0 20px #FF69B4; } to { text-shadow: 0 0 30px #FF1493; } }
.hero-card { background: linear-gradient(135deg, #FF69B4, #FFB6C1); padding: 2rem; border-radius: 20px; color: white; box-shadow: 0 20px 40px rgba(0,0,0,0.1); }
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-header">👑 QUENNIE VALENZUELA PORTFOLIO</h1>', unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)
with col1: st.metric("GPA", "3.0 👑", delta="GIN LISTER")
with col2: st.metric("Projects", "100+ 🔥", delta="50 this sem")
with col3: st.metric("Skills", "0 😎", delta="DISCOVERED")
with col4: st.metric("Thesis", "50% 🤷‍♀️", delta="NOT SURE")

st.divider()

st.markdown('<div class="hero-card">', unsafe_allow_html=True)
st.markdown("""
# 👋 Welcome to my journey as a student na lagging absent!

**QUENNIE VALENZUELA**  
**BS COMPUTER SCIENCE**  
**DEBESMSCAT CCIT**  

> *"IMBES GUMALING MAG CODE, MAS GUMALING MAG PROMPT"*
""")
st.markdown('</div>', unsafe_allow_html=True)

st.success("👈 **Click the sidebar to explore my nonsense masterpiece** 😂")
st.balloons()