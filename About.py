import streamlit as st

st.title("👩‍💻 About Me - DEBESMSCAT STUDENT")

col1, col2 = st.columns([1,2])

with col1:
    st.markdown("""
    <div style='text-align: center;'>
        <img src='https://via.placeholder.com/300x300/FF69B4/FFFFFF?text=👑' 
             style='border-radius: 50%; box-shadow: 0 15px 35px rgba(0,0,0,0.1);'>
        <h3>👑 QUENNIE</h3>
    </div>
    """, unsafe_allow_html=True)
    
with col2:
    st.markdown("""
    # 👑 QUENNIE VALENZUELA
    **BS COMPUTER SCIENCE-CCIT**
    **GIN LISTER / 3.0 GPA**
    **VICTORY PERO SA ML** 💅
    """)

st.subheader("🏅 Academic Achievements")
achievements = [
    "👑 **GIN LISTER** - Since first year college",
    "🦄 **MYTHICAL HONOR** - Highest rank 😂",
    "📊 **50% Thesis Progress** - 50% NOT SURE 🤷‍♀️",
    "📅 **Attendance** - 90% ABSENT 😎"
]

for achievement in achievements:
    st.success(achievement)

st.subheader("💭 My Mission")
st.markdown("""
> **"As a DEBESMSCAT student, I don't just code I create solution that make different using AI HAHAHA char"** 😂
""")

st.success("👈 **Just click the sidebar to view my nonsense life** 🎉")