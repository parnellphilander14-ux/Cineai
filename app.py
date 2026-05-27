import streamlit as st

st.set_page_config(
    page_title="CineAI - Movie Recommender",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Global CSS
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Sans:wght@300;400;500;600&display=swap');

/* Hide default streamlit elements */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Root variables */
:root {
    --red: #E63946;
    --dark: #0D0D0D;
    --card: #161616;
    --border: #2a2a2a;
    --muted: #888;
    --white: #F5F0EB;
}

html, body, .stApp {
    background-color: var(--dark) !important;
    color: var(--white) !important;
    font-family: 'DM Sans', sans-serif !important;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #111111 !important;
    border-right: 1px solid var(--border) !important;
}
[data-testid="stSidebar"] * {
    color: var(--white) !important;
}

/* Sidebar nav links */
[data-testid="stSidebarNav"] a {
    color: var(--muted) !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 0.95rem !important;
    letter-spacing: 0.02em;
    padding: 0.5rem 1rem !important;
    border-radius: 6px;
    transition: all 0.2s;
}
[data-testid="stSidebarNav"] a:hover,
[data-testid="stSidebarNav"] a[aria-selected="true"] {
    color: var(--white) !important;
    background-color: rgba(230, 57, 70, 0.15) !important;
}

/* Buttons */
.stButton > button {
    background-color: var(--red) !important;
    color: white !important;
    border: none !important;
    border-radius: 6px !important;
    font-family: 'DM Sans', sans-serif !important;
    font-weight: 600 !important;
    letter-spacing: 0.04em !important;
    padding: 0.5rem 1.5rem !important;
    transition: opacity 0.2s !important;
}
.stButton > button:hover {
    opacity: 0.85 !important;
}

/* Inputs */
.stTextInput > div > div > input,
.stSelectbox > div > div,
.stTextArea textarea {
    background-color: var(--card) !important;
    border: 1px solid var(--border) !important;
    color: var(--white) !important;
    border-radius: 6px !important;
    font-family: 'DM Sans', sans-serif !important;
}

/* Metric cards */
[data-testid="stMetric"] {
    background-color: var(--card);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 1rem 1.5rem;
}

/* Divider */
hr {
    border-color: var(--border) !important;
}
[data-testid="collapsedControl"] { display:block !important; color:white !important; }
</style>
""", unsafe_allow_html=True)

# Sidebar branding
with st.sidebar:
    st.markdown("""
    <div style="padding: 1.5rem 0 1rem 0; text-align:center;">
        <span style="font-family:'Bebas Neue',sans-serif; font-size:2rem; color:#E63946; letter-spacing:0.1em;">CINE</span>
        <span style="font-family:'Bebas Neue',sans-serif; font-size:2rem; color:#F5F0EB; letter-spacing:0.1em;">AI</span>
        <p style="color:#888; font-size:0.75rem; margin-top:0.2rem; font-family:'DM Sans',sans-serif;">Your Cinema Intelligence</p>
    </div>
    <hr style="border-color:#2a2a2a;">
    """, unsafe_allow_html=True)

# Home page content
st.markdown("""
<div style="padding: 4rem 2rem 2rem 2rem; text-align:center;">
    <p style="color:#E63946; font-family:'DM Sans',sans-serif; font-size:0.85rem; letter-spacing:0.2em; text-transform:uppercase; margin-bottom:1rem;">Welcome to</p>
    <h1 style="font-family:'Bebas Neue',sans-serif; font-size:5rem; color:#F5F0EB; letter-spacing:0.08em; margin:0; line-height:1;">CINE<span style="color:#E63946;">AI</span></h1>
    <p style="color:#888; font-size:1.1rem; margin-top:1rem; max-width:500px; margin-left:auto; margin-right:auto; font-family:'DM Sans',sans-serif;">
        Discover movies you'll love. Chat with an AI that knows cinema inside-out.
    </p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("""
    <div style="background:#161616; border:1px solid #2a2a2a; border-radius:12px; padding:2rem; text-align:center; height:220px; display:flex; flex-direction:column; justify-content:center;">
        <div style="font-size:2.5rem; margin-bottom:1rem;">🎬</div>
        <h3 style="font-family:'Bebas Neue',sans-serif; font-size:1.5rem; color:#F5F0EB; letter-spacing:0.06em; margin:0 0 0.5rem 0;">MOVIE RECOMMENDER</h3>
        <p style="color:#888; font-size:0.9rem; margin:0;">Search by title, genre, or mood — get curated picks with full details.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="background:#161616; border:1px solid #2a2a2a; border-radius:12px; padding:2rem; text-align:center; height:220px; display:flex; flex-direction:column; justify-content:center;">
        <div style="font-size:2.5rem; margin-bottom:1rem;">🤖</div>
        <h3 style="font-family:'Bebas Neue',sans-serif; font-size:1.5rem; color:#F5F0EB; letter-spacing:0.06em; margin:0 0 0.5rem 0;">MOVIE CHATBOT</h3>
        <p style="color:#888; font-size:0.9rem; margin:0;">Ask anything about movies, directors, actors, and get AI-powered answers.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<p style="text-align:center; color:#555; font-size:0.8rem; margin-top:3rem;">
    Navigate using the sidebar → Use the pages to explore all features
</p>
""", unsafe_allow_html=True)
