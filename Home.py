import streamlit as st

st.title("🏠 Home - My College Story")

st.subheader("🎯 My College Journey")
timeline = {
    "1st Sem": "2.85 👑 gin lister",
    "2nd Sem": "3.0 😂 absent lister", 
    "Current": "3.0 😎 just living",
    "Goal": "to still graduate and become your boss 💅"
}

for period, story in timeline.items():
    with st.expander(f"📅 {period}", expanded=False):
        st.info(f"**{story}**")

st.subheader("📊 Current GPA: 50/50")
st.metric("GPA", "3.0", delta="gin lister material yey! 🎉")

st.subheader("📈 My Semester Progress")
progress = st.progress(0)
st.info("0% - incomplete 😭")
st.caption("**Just living my best absent life** 😂")