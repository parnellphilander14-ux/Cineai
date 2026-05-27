import streamlit as st

st.set_page_config(page_title="About – CineAI", page_icon="ℹ️", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Sans:wght@300;400;500;600&display=swap');
#MainMenu {visibility:hidden;} footer {visibility:hidden;} header {visibility:hidden;}
:root { --red:#E63946; --dark:#0D0D0D; --card:#161616; --border:#2a2a2a; --muted:#888; --white:#F5F0EB; }
html, body, .stApp { background-color:var(--dark) !important; color:var(--white) !important; font-family:'DM Sans',sans-serif !important; }
[data-testid="stSidebar"] { background-color:#111111 !important; border-right:1px solid var(--border) !important; }
[data-testid="stSidebar"] * { color:var(--white) !important; }
[data-testid="stSidebarNav"] a { color:var(--muted) !important; }
[data-testid="stSidebarNav"] a:hover { color:var(--white) !important; background-color:rgba(230,57,70,0.15) !important; }
hr { border-color:var(--border) !important; }
[data-testid="collapsedControl"] { display:block !important; color:white !important; }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("""
    <div style="padding:1.5rem 0 1rem 0; text-align:center;">
        <span style="font-family:'Bebas Neue',sans-serif; font-size:2rem; color:#E63946;">CINE</span>
        <span style="font-family:'Bebas Neue',sans-serif; font-size:2rem; color:#F5F0EB;">AI</span>
    </div><hr style="border-color:#2a2a2a;">
    """, unsafe_allow_html=True)

st.markdown("""
<h1 style='font-family:\"Bebas Neue\",sans-serif;font-size:2.8rem;color:#F5F0EB;letter-spacing:0.06em;margin-bottom:0;'>
    ABOUT <span style='color:#E63946;'>CINEAI</span>
</h1>
<p style='color:#888;margin-top:0.2rem;'>Final Project — Streamlit + API Integration</p>
<hr>""", unsafe_allow_html=True)

col1, col2 = st.columns([2,1], gap="large")

with col1:
    st.markdown("""
    <div style='background:#161616;border:1px solid #2a2a2a;border-radius:12px;padding:2rem;margin-bottom:1.5rem;'>
        <h3 style='font-family:\"Bebas Neue\",sans-serif;font-size:1.4rem;color:#F5F0EB;letter-spacing:0.06em;margin-top:0;'>ABOUT THIS APP</h3>
        <p style='color:#aaa;line-height:1.7;'>
            CineAI is an AI-powered movie discovery platform built with Streamlit.
            It uses Google Gemini to recommend movies based on your mood, genre, or any description —
            and lets you chat with an AI movie expert for anything cinema-related.
        </p>
    </div>

    <div style='background:#161616;border:1px solid #2a2a2a;border-radius:12px;padding:2rem;'>
        <h3 style='font-family:\"Bebas Neue\",sans-serif;font-size:1.4rem;color:#F5F0EB;letter-spacing:0.06em;margin-top:0;'>HOW TO USE</h3>
        <div style='color:#aaa;line-height:1.8;'>
            <p style='margin:0.4rem 0;'>
                <span style='color:#E63946;font-weight:600;'>Step 1</span> — Open the <b style='color:#F5F0EB;'>🎬 Movie Recommender</b> page
            </p>
            <p style='margin:0.4rem 0;'>
                <span style='color:#E63946;font-weight:600;'>Step 2</span> — Search by mood or title, or browse by genre and mood combo
            </p>
            <p style='margin:0.4rem 0;'>
                <span style='color:#E63946;font-weight:600;'>Step 3</span> — Open the <b style='color:#F5F0EB;'>🤖 Movie Chatbot</b> page
            </p>
            <p style='margin:0.4rem 0;'>
                <span style='color:#E63946;font-weight:600;'>Step 4</span> — Ask anything about movies, directors, actors, or get more recommendations
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style='background:#161616;border:1px solid #2a2a2a;border-radius:12px;padding:2rem;margin-bottom:1.5rem;'>
        <h3 style='font-family:\"Bebas Neue\",sans-serif;font-size:1.4rem;color:#F5F0EB;letter-spacing:0.06em;margin-top:0;'>TECH STACK</h3>
        <div style='color:#aaa;'>
            <p style='margin:0.6rem 0;'>🐍 <b style='color:#F5F0EB;'>Python</b></p>
            <p style='margin:0.6rem 0;'>🎈 <b style='color:#F5F0EB;'>Streamlit</b> — UI Framework</p>
            <p style='margin:0.6rem 0;'>🤖 <b style='color:#F5F0EB;'>Gemini API</b> — AI Recommender & Chatbot</p>
            <p style='margin:0.6rem 0;'>☁️ <b style='color:#F5F0EB;'>Streamlit Cloud</b> — Deployment</p>
        </div>
    </div>

    <div style='background:#161616;border:1px solid #2a2a2a;border-radius:12px;padding:2rem;'>
        <h3 style='font-family:\"Bebas Neue\",sans-serif;font-size:1.4rem;color:#F5F0EB;letter-spacing:0.06em;margin-top:0;'>FEATURES</h3>
        <div style='color:#aaa;'>
            <p style='margin:0.5rem 0;'>✅ Multi-page sidebar navigation</p>
            <p style='margin:0.5rem 0;'>✅ AI movie recommendations</p>
            <p style='margin:0.5rem 0;'>✅ Search by mood or title</p>
            <p style='margin:0.5rem 0;'>✅ Browse by genre & mood</p>
            <p style='margin:0.5rem 0;'>✅ AI movie chatbot</p>
            <p style='margin:0.5rem 0;'>✅ Chat history</p>
            <p style='margin:0.5rem 0;'>✅ Secure API key via secrets</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<p style='text-align:center; color:#444; font-size:0.8rem; margin-top:3rem;'>
    Built with ❤️ using Streamlit · Powered by Google Gemini
</p>""", unsafe_allow_html=True)
