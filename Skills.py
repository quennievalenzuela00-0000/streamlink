import streamlit as st
import time

st.title("⭐ MY SKILLS")

st.subheader("💻 Programming Mastery")
skills = {
    "🐍 Python WITH AI": 100,
    "🐍 Python WITHOUT AI": 10,
    "⚡ JavaScript WITH AI": 100,
    "⚡ JavaScript WITHOUT AI": 0,
    "⚙️ C++ WITH AI": 100,
    "⚙️ C++ WITHOUT AI": 0
}

for skill, level in skills.items():
    bar = st.progress(level/100)
    st.write(f"**{skill}:** {level}% {'👑' if level == 100 else '😂'}")
    time.sleep(0.1)

st.subheader("🤖 ML Skills")
st.metric("ML SKILLS", "1000% 🔥", delta="QUEEN LEVEL")

st.subheader("🎮 Tech Stack Radar")
tech_stack = ["👑 KARINA", "🧝 FREYA", "😇 ANGELA", "🧙‍♀️ VEXANA", "🗡️ GUSION"]
for tech in tech_stack:
    col1, col2 = st.columns([3,1])
    with col1: st.write(tech)
    with col2: 
        if "KARINA" in tech or "FREYA" in tech or "ANGELA" in tech:
            st.success("✅ MASTERED")
        else:
            st.warning("⏳ STILL LEARNING")