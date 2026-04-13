import streamlit as st
import time

st.title("📞 Connect With Me")

st.markdown("""
<div style='background: linear-gradient(135deg, #FF69B4, #FFB6C1); 
           color: white; padding: 2rem; border-radius: 15px; text-align: center;'>
<h2>🤝 FOR COLLABORATION IN ML AND SPONSORS OF SKIN</h2>
<p><strong>Open for:</strong> swapping lane/open for trashtalking joke hehe 😂</p>
</div>
""", unsafe_allow_html=True)

st.subheader("✉️ Direct Message Form")
col1, col2 = st.columns(2)

with col1:
    name = st.text_input("👤 Name")
    email = st.text_input("📧 Email")
    role = st.selectbox("🎮 MLBB Role", ["ML Collaborator", "Skin Sponsor", "Trash Talker", "Thesis Helper"])

with col2:
    subject = st.selectbox("📂 Subject", 
                          ["ML COLLABORATION", "ML SWAP", "GIVE ME A SKIN OF ANGELA", "BUY A DIAS AND SEND TO QUEEN"])
    urgency = st.slider("⏰ Urgency", 1, 5, 5)

message = st.text_area("💬 Message", 
                      "Hi Quennie! Can you...")

if st.button("🚀 SEND TO QUEEN", type="primary", use_container_width=True):
    if name and email and message:
        with st.spinner("📤 Sending to QUEEN..."):
            time.sleep(1.5)
        st.success("✅ **MESSAGE SENT TO QUEEN!** 👑")
        st.balloons()
        st.snow()
    else:
        st.error("❌ Complete all fields! 😂")

st.subheader("🔗 Connect")
social = {
    "👑 MLBB ID": "QUEEN#1234",
    "💻 GitHub": "github.com/quenniequeen",
    "📱 Facebook": "fb.com/quenniequeen",
    "🎮 Discord": "quennie#6969",
    "💅 Instagram": "@queen_valenzuela"
}

cols = st.columns(2)
for i, (platform, link) in enumerate(social.items()):
    with cols[i%2]:
        st.markdown(f"**{platform}:** `{link}`")