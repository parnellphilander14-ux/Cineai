import streamlit as st
from google import genai
from google.genai import types

st.set_page_config(page_title="Movie Chatbot – CineAI", page_icon="🤖", layout="wide")

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
[data-testid="stChatMessage"] { background-color:var(--card) !important; border:1px solid var(--border) !important; border-radius:10px !important; margin-bottom:0.5rem !important; }
[data-testid="stChatMessage"] p { color:var(--white) !important; font-family:'DM Sans',sans-serif !important; }
[data-testid="stChatInput"] { background-color:var(--card) !important; border:1px solid var(--border) !important; border-radius:8px !important; }
[data-testid="stChatInput"] textarea { color:var(--white) !important; background-color:transparent !important; font-family:'DM Sans',sans-serif !important; }
.stButton>button { background-color:var(--red) !important; color:white !important; border:none !important; border-radius:6px !important; font-family:'DM Sans',sans-serif !important; font-weight:600 !important; }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("""
    <div style="padding:1.5rem 0 1rem 0; text-align:center;">
        <span style="font-family:'Bebas Neue',sans-serif; font-size:2rem; color:#E63946;">CINE</span>
        <span style="font-family:'Bebas Neue',sans-serif; font-size:2rem; color:#F5F0EB;">AI</span>
    </div><hr style="border-color:#2a2a2a;">
    """, unsafe_allow_html=True)
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
    st.markdown("<hr style='border-color:#2a2a2a;'>", unsafe_allow_html=True)
    st.markdown("<p style='color:#555; font-size:0.75rem;'>💡 Try asking:</p>", unsafe_allow_html=True)
    for s in ["Recommend a thriller movie", "Who directed Inception?", "Best movies of 2024", "Movies similar to Parasite", "Top 5 Nolan films"]:
        st.markdown(f"<p style='color:#666;font-size:0.75rem;margin:0.2rem 0;'>• {s}</p>", unsafe_allow_html=True)

# ─── LOAD API KEY FROM SECRETS ──────────────────────────────────────────────
try:
    gemini_key = st.secrets["GEMINI_API_KEY"]
except KeyError:
    st.error("⚠️ GEMINI_API_KEY not found in secrets. Please configure it in Streamlit Cloud secrets.")
    st.stop()

# ─── GEMINI CLIENT (google-genai SDK) ───────────────────────────────────────
client = genai.Client(api_key=gemini_key)

SYSTEM_PROMPT = """You are CineAI, an enthusiastic and knowledgeable movie expert chatbot.
You ONLY discuss topics related to movies, cinema, directors, actors, film genres, movie history,
box office, film techniques, and recommendations.

If someone asks about something unrelated to movies or cinema, politely redirect them to movie topics.

When recommending movies:
- Always include the title, year, director, and a brief reason why they'd enjoy it
- Be specific and passionate about your recommendations
- Consider the user's preferences if they've mentioned any

Keep responses concise but informative. Use movie emojis occasionally. Be friendly and conversational."""

def ask_gemini(chat_history, user_msg):
    # Build contents list from history + new message
    contents = []
    for msg in chat_history:
        role = "user" if msg["role"] == "user" else "model"
        contents.append(types.Content(role=role, parts=[types.Part(text=msg["content"])]))
    contents.append(types.Content(role="user", parts=[types.Part(text=user_msg)]))

    response = client.models.generate_content(
        model="gemini-2.0-flash-lite",
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT,
            temperature=0.8,
            max_output_tokens=1024,
        ),
        contents=contents,
    )
    return response.text

# ─── CHAT STATE ─────────────────────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []

# ─── PAGE HEADER ────────────────────────────────────────────────────────────
st.markdown("""
<h1 style='font-family:\"Bebas Neue\",sans-serif;font-size:2.8rem;color:#F5F0EB;letter-spacing:0.06em;margin-bottom:0;'>
    MOVIE <span style='color:#E63946;'>CHATBOT</span>
</h1>
<p style='color:#888;margin-top:0.2rem;'>Powered by Gemini AI · Ask anything about cinema</p>
<hr>""", unsafe_allow_html=True)

if not st.session_state.messages:
    st.markdown("""
    <div style='background:#161616;border:1px solid #2a2a2a;border-radius:10px;padding:1.5rem;margin-bottom:1rem;text-align:center;'>
        <p style='font-size:2rem;margin:0;'>🎬</p>
        <p style='color:#F5F0EB;font-size:1rem;margin:0.5rem 0 0.2rem 0;font-weight:600;'>Hey! I'm CineAI</p>
        <p style='color:#888;font-size:0.85rem;margin:0;'>Your personal movie expert. Ask me about recommendations, directors, actors, or anything cinema!</p>
    </div>""", unsafe_allow_html=True)

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if user_input := st.chat_input("Ask about movies…"):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking…"):
            try:
                history_for_api = st.session_state.messages[:-1]
                response = ask_gemini(history_for_api, user_input)
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
            except Exception as e:
                st.error(f"❌ Error: {e}")
