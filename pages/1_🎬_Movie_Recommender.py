import streamlit as st
from google import genai
from google.genai import types
import json

st.set_page_config(page_title="Movie Recommender – CineAI", page_icon="🎬", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Sans:wght@300;400;500;600&display=swap');
#MainMenu {visibility:hidden;} footer {visibility:hidden;} header {visibility:hidden;}
:root { --red:#E63946; --dark:#0D0D0D; --card:#161616; --border:#2a2a2a; --muted:#888; --white:#F5F0EB; }
html, body, .stApp { background-color:var(--dark) !important; color:var(--white) !important; font-family:'DM Sans',sans-serif !important; }
[data-testid="stSidebar"] { background-color:#111111 !important; border-right:1px solid var(--border) !important; }
[data-testid="stSidebar"] * { color:var(--white) !important; }
.stButton>button { background-color:var(--red) !important; color:white !important; border:none !important; border-radius:6px !important; font-family:'DM Sans',sans-serif !important; font-weight:600 !important; }
.stButton>button:hover { opacity:0.85 !important; }
.stTextInput>div>div>input, .stSelectbox>div>div { background-color:var(--card) !important; border:1px solid var(--border) !important; color:var(--white) !important; border-radius:6px !important; font-family:'DM Sans',sans-serif !important; }
hr { border-color:var(--border) !important; }
[data-testid="collapsedControl"] { display:block !important; color:white !important; }
[data-testid="stSidebarNav"] a { color:var(--muted) !important; }
[data-testid="stSidebarNav"] a:hover { color:var(--white) !important; background-color:rgba(230,57,70,0.15) !important; }
div[data-testid="stExpander"] { background-color:var(--card) !important; border:1px solid var(--border) !important; border-radius:8px !important; }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("""
    <div style="padding:1.5rem 0 1rem 0; text-align:center;">
        <span style="font-family:'Bebas Neue',sans-serif; font-size:2rem; color:#E63946;">CINE</span>
        <span style="font-family:'Bebas Neue',sans-serif; font-size:2rem; color:#F5F0EB;">AI</span>
    </div><hr style="border-color:#2a2a2a;">
    """, unsafe_allow_html=True)
    st.markdown("<p style='color:#555; font-size:0.75rem;'>💡 Try searching:</p>", unsafe_allow_html=True)
    for s in ["sci-fi movies like Interstellar", "romantic comedies", "horror movies 2023", "best Nolan films", "action movies for kids"]:
        st.markdown(f"<p style='color:#666;font-size:0.75rem;margin:0.2rem 0;'>• {s}</p>", unsafe_allow_html=True)

# ─── LOAD API KEY FROM SECRETS ──────────────────────────────────────────────
try:
    gemini_key = st.secrets["GEMINI_API_KEY"]
except KeyError:
    st.error("⚠️ GEMINI_API_KEY not found in secrets.")
    st.stop()

client = genai.Client(api_key=gemini_key)

def get_recommendations(query):
    prompt = f"""You are a movie expert. The user is looking for: "{query}"
    
Recommend exactly 8 movies. Respond ONLY with a valid JSON array, no extra text, no markdown, no backticks.

Format:
[
  {{
    "title": "Movie Title",
    "year": "2010",
    "director": "Director Name",
    "genre": "Action, Thriller",
    "rating": "8.5/10",
    "description": "A 2-sentence description of the movie and why someone would enjoy it.",
    "why": "One sentence on why this matches the user's request."
  }}
]"""

    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        config=types.GenerateContentConfig(temperature=0.7, max_output_tokens=2048),
        contents=prompt
    )
    
    text = response.text.strip()
    # Strip any accidental markdown fences
    text = text.replace("```json", "").replace("```", "").strip()
    return json.loads(text)

def star_rating(rating_str):
    try:
        score = float(rating_str.replace("/10", "").strip())
        stars = round(score / 2)
        return "★" * stars + "☆" * (5 - stars)
    except:
        return "★★★★☆"

# ─── PAGE HEADER ────────────────────────────────────────────────────────────
st.markdown("""
<h1 style='font-family:\"Bebas Neue\",sans-serif;font-size:2.8rem;color:#F5F0EB;letter-spacing:0.06em;margin-bottom:0;'>
    MOVIE <span style='color:#E63946;'>RECOMMENDER</span>
</h1>
<p style='color:#888;margin-top:0.2rem;'>Powered by Gemini AI · Describe what you want to watch</p>
<hr>""", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["🔍  Search by Mood / Title", "🎭  Browse by Genre"])

# ─── TAB 1: SEARCH ──────────────────────────────────────────────────────────
with tab1:
    c1, c2 = st.columns([4, 1])
    with c1:
        query = st.text_input("", placeholder="e.g. mind-bending sci-fi, movies like Parasite, sad romance…", label_visibility="collapsed")
    with c2:
        st.markdown("<div style='margin-top:4px;'>", unsafe_allow_html=True)
        do_search = st.button("Search", use_container_width=True, key="search_btn")
        st.markdown("</div>", unsafe_allow_html=True)

    if do_search and query:
        with st.spinner("Finding movies for you…"):
            try:
                movies = get_recommendations(query)
                st.markdown(f"<p style='color:#888;font-size:0.85rem;'>Here are 8 picks for <b style='color:#E63946;'>\"{query}\"</b></p>", unsafe_allow_html=True)
                cols = st.columns(4, gap="medium")
                for i, movie in enumerate(movies):
                    with cols[i % 4]:
                        st.markdown(f"""
                        <div style='background:#161616;border:1px solid #2a2a2a;border-radius:10px;padding:1rem;margin-bottom:0.5rem;height:100%;'>
                            <div style='background:#1a1a1a;border-radius:6px;height:160px;display:flex;align-items:center;justify-content:center;margin-bottom:0.8rem;'>
                                <span style='font-size:3rem;'>🎬</span>
                            </div>
                            <p style='font-family:\"Bebas Neue\",sans-serif;font-size:1rem;color:#F5F0EB;margin:0;letter-spacing:0.04em;line-height:1.2;'>{movie.get('title','')}</p>
                            <p style='color:#888;font-size:0.75rem;margin:0.2rem 0;'>{movie.get('year','')} · <span style='color:#E63946;'>{star_rating(movie.get('rating','8/10'))}</span> {movie.get('rating','')}</p>
                            <p style='color:#666;font-size:0.72rem;margin:0;'>🎭 {movie.get('genre','')}</p>
                            <p style='color:#777;font-size:0.72rem;margin:0.1rem 0;'>🎬 {movie.get('director','')}</p>
                        </div>
                        """, unsafe_allow_html=True)
                        with st.expander("ℹ️ Why watch?"):
                            st.markdown(f"<p style='color:#bbb;font-size:0.82rem;line-height:1.5;'>{movie.get('description','')}</p>", unsafe_allow_html=True)
                            st.markdown(f"<p style='color:#E63946;font-size:0.78rem;font-style:italic;'>✨ {movie.get('why','')}</p>", unsafe_allow_html=True)
            except json.JSONDecodeError:
                st.error("Couldn't parse recommendations. Try again!")
            except Exception as e:
                st.error(f"Error: {e}")

# ─── TAB 2: BROWSE BY GENRE ─────────────────────────────────────────────────
with tab2:
    genres = ["Action", "Comedy", "Drama", "Horror", "Sci-Fi", "Romance", "Thriller", "Animation", "Documentary", "Fantasy"]
    moods  = ["Feel-good", "Mind-bending", "Tear-jerker", "Adrenaline rush", "Thought-provoking", "Family-friendly"]

    cg, cm, cb = st.columns([2, 2, 1])
    with cg:
        sel_genre = st.selectbox("Genre", genres)
    with cm:
        sel_mood = st.selectbox("Mood", moods)
    with cb:
        st.markdown("<div style='margin-top:28px;'>", unsafe_allow_html=True)
        do_browse = st.button("Browse", use_container_width=True, key="browse_btn")
        st.markdown("</div>", unsafe_allow_html=True)

    if do_browse:
        with st.spinner("Finding movies…"):
            try:
                browse_query = f"{sel_mood} {sel_genre} movies"
                movies = get_recommendations(browse_query)
                st.markdown(f"<p style='color:#888;font-size:0.85rem;'>Top picks for <b style='color:#E63946;'>{sel_mood} {sel_genre}</b></p>", unsafe_allow_html=True)
                cols = st.columns(4, gap="medium")
                for i, movie in enumerate(movies):
                    with cols[i % 4]:
                        st.markdown(f"""
                        <div style='background:#161616;border:1px solid #2a2a2a;border-radius:10px;padding:1rem;margin-bottom:0.5rem;'>
                            <div style='background:#1a1a1a;border-radius:6px;height:160px;display:flex;align-items:center;justify-content:center;margin-bottom:0.8rem;'>
                                <span style='font-size:3rem;'>🎬</span>
                            </div>
                            <p style='font-family:\"Bebas Neue\",sans-serif;font-size:1rem;color:#F5F0EB;margin:0;letter-spacing:0.04em;line-height:1.2;'>{movie.get('title','')}</p>
                            <p style='color:#888;font-size:0.75rem;margin:0.2rem 0;'>{movie.get('year','')} · <span style='color:#E63946;'>{star_rating(movie.get('rating','8/10'))}</span> {movie.get('rating','')}</p>
                            <p style='color:#666;font-size:0.72rem;margin:0;'>🎭 {movie.get('genre','')}</p>
                            <p style='color:#777;font-size:0.72rem;margin:0.1rem 0;'>🎬 {movie.get('director','')}</p>
                        </div>
                        """, unsafe_allow_html=True)
                        with st.expander("ℹ️ Why watch?"):
                            st.markdown(f"<p style='color:#bbb;font-size:0.82rem;line-height:1.5;'>{movie.get('description','')}</p>", unsafe_allow_html=True)
                            st.markdown(f"<p style='color:#E63946;font-size:0.78rem;font-style:italic;'>✨ {movie.get('why','')}</p>", unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Error: {e}")
