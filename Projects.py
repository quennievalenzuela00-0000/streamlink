# SAME AS BEFORE - DON'T CHANGE 🔥
import streamlit as st

st.title("🚀 CS3 PROJECT MASTERPIECES")

projects = {
    "🎓 AI-Powered Grading System": {
        "desc": "Thesis project using ML to auto-grade programming assignments",
        "tech": "Python, TensorFlow, Flask, MySQL",
        "grade": "95% (Ongoing)",
        "demo": "LIVE DEMO ⏰ Coming Soon"
    },
    "🏢 DEBESMSCAT Student Portal": {
        "desc": "Full-stack web app for enrollment, grades, and clearance",
        "tech": "React, Node.js, MongoDB, JWT Auth",
        "grade": "1.25 🥇",
        "demo": "Deployed on Vercel"
    },
    "🔍 Smart Library Management": {
        "desc": "RFID + Face Recognition for DEBESMSCAT Library",
        "tech": "Python, OpenCV, Arduino, SQLite",
        "grade": "1.50 🥈",
        "demo": "Video Presentation Available"
    },
    "📊 CS3 Capstone Dashboard": {
        "desc": "Interactive analytics dashboard for all CS3 projects",
        "tech": "Streamlit, Plotly, Pandas, PostgreSQL",
        "grade": "1.00 🥇",
        "demo": "LIVE on Streamlit Cloud"
    }
}

for project, details in projects.items():
    st.markdown("---")
    col1, col2 = st.columns([2,1])
    
    with col1:
        st.markdown(f"### 🔥 **{project}**")
        st.info(details["desc"])
        st.caption(f"**Tech Stack:** {details['tech']}")
    
    with col2:
        st.metric("📉 Grade", details["grade"])
        if st.button(details["demo"], key=project):
            st.success(f"🎉 **{project}** demo accessed!")

st.subheader("🔍 Filter My CS3 Works")
tech_filter = st.multiselect("Tech Stack", 
                           ["Python", "React", "ML/AI", "Database", "Web", "IoT"])
st.success("**💡 All projects include:** Source Code + Documentation + Presentation")

st.markdown("""
<div style='text-align: center; padding: 2rem;'>
    <h3>🎓 Built for DEBESMSCAT CS3 Excellence</h3>
</div>
""", unsafe_allow_html=True)