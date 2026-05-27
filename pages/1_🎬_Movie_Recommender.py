import streamlit as st
import requests

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

# ─── LOAD API KEY FROM SECRETS ──────────────────────────────────────────────
try:
    tmdb_key = st.secrets["TMDB_API_KEY"]
except KeyError:
    st.error("⚠️ TMDB_API_KEY not found in secrets. Please configure it in Streamlit Cloud secrets.")
    st.stop()

TMDB_BASE = "https://api.themoviedb.org/3"
IMG_BASE  = "https://image.tmdb.org/t/p/w500"

def tmdb_get(endpoint, params, key):
    params["api_key"] = key
    r = requests.get(f"{TMDB_BASE}{endpoint}", params=params, timeout=10)
    r.raise_for_status()
    return r.json()

def star_rating(score):
    stars = round(score / 2)
    return "★" * stars + "☆" * (5 - stars)

def render_movie_grid(movies, key):
    cols = st.columns(4, gap="medium")
    for i, movie in enumerate(movies):
        with cols[i % 4]:
            poster = f"{IMG_BASE}{movie['poster_path']}" if movie.get("poster_path") else None
            title  = movie.get("title", "Unknown")
            year   = movie.get("release_date", "")[:4] or "—"
            rating = movie.get("vote_average", 0)

            if poster:
                st.image(poster, use_container_width=True)
            else:
                st.markdown("<div style='background:#1a1a1a;border:1px solid #2a2a2a;border-radius:6px;height:220px;display:flex;align-items:center;justify-content:center;'><span style='font-size:2.5rem;'>🎬</span></div>", unsafe_allow_html=True)

            st.markdown(f"""
            <div style='margin-top:0.4rem; margin-bottom:0.3rem;'>
                <p style='font-family:\"Bebas Neue\",sans-serif;font-size:0.95rem;color:#F5F0EB;margin:0;letter-spacing:0.04em;line-height:1.2;'>{title}</p>
                <p style='color:#888;font-size:0.75rem;margin:0.1rem 0 0 0;'>
                    {year} · <span style='color:#E63946;'>{star_rating(rating)}</span> <span style='color:#555;'>{rating:.1f}</span>
                </p>
            </div>""", unsafe_allow_html=True)

            with st.expander("ℹ️ Details"):
                try:
                    d = tmdb_get(f"/movie/{movie['id']}", {"language":"en-US","append_to_response":"credits"}, key)
                    overview  = d.get("overview","No description.")
                    runtime   = d.get("runtime", 0)
                    genres_l  = ", ".join(g["name"] for g in d.get("genres",[]))
                    cast      = ", ".join(c["name"] for c in d.get("credits",{}).get("cast",[])[:4]) or "N/A"
                    st.markdown(f"""
                    <p style='color:#bbb;font-size:0.82rem;line-height:1.5;'>{overview[:250]}{'…' if len(overview)>250 else ''}</p>
                    <p style='font-size:0.76rem;color:#888;margin-top:0.4rem;'>🕐 {runtime} min · 🎭 {genres_l}</p>
                    <p style='font-size:0.76rem;color:#888;'>👥 {cast}</p>
                    """, unsafe_allow_html=True)
                except Exception as ex:
                    st.caption(f"Could not load details: {ex}")

# ─── PAGE HEADER ────────────────────────────────────────────────────────────
st.markdown("""
<h1 style='font-family:\"Bebas Neue\",sans-serif;font-size:2.8rem;color:#F5F0EB;letter-spacing:0.06em;margin-bottom:0;'>
    MOVIE <span style='color:#E63946;'>RECOMMENDER</span>
</h1>
<p style='color:#888;margin-top:0.2rem;'>Search by title or browse by genre</p>
<hr>""", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["🔍  Search by Title", "🎭  Browse by Genre"])

with tab1:
    c1, c2 = st.columns([4,1])
    with c1:
        query = st.text_input("", placeholder="e.g. Inception, Parasite, The Dark Knight…", label_visibility="collapsed")
    with c2:
        st.markdown("<div style='margin-top:4px;'>", unsafe_allow_html=True)
        do_search = st.button("Search", use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    if do_search and query:
        with st.spinner("Searching…"):
            try:
                res = tmdb_get("/search/movie", {"query": query, "page":1, "include_adult":False}, tmdb_key)
                movies = res.get("results", [])
                if not movies:
                    st.warning("No movies found. Try a different title.")
                else:
                    st.markdown(f"<p style='color:#888;font-size:0.85rem;'>Found {res['total_results']} results — showing top 12</p>", unsafe_allow_html=True)
                    render_movie_grid(movies[:12], tmdb_key)
            except Exception as e:
                st.error(f"Error: {e}")

with tab2:
    try:
        genre_data = tmdb_get("/genre/movie/list", {"language":"en-US"}, tmdb_key)
        genres = {g["name"]: g["id"] for g in genre_data["genres"]}

        cg, cs, cb = st.columns([2,2,1])
        with cg:
            sel_genre = st.selectbox("Genre", list(genres.keys()))
        with cs:
            sort_map = {"Popularity":"popularity.desc","Top Rated":"vote_average.desc","Newest":"release_date.desc"}
            sort_lbl = st.selectbox("Sort by", list(sort_map.keys()))
        with cb:
            st.markdown("<div style='margin-top:28px;'>", unsafe_allow_html=True)
            do_browse = st.button("Browse", use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)

        if do_browse:
            with st.spinner("Loading…"):
                try:
                    res = tmdb_get("/discover/movie", {
                        "with_genres": genres[sel_genre],
                        "sort_by": sort_map[sort_lbl],
                        "page":1, "vote_count.gte":100
                    }, tmdb_key)
                    movies = res.get("results",[])
                    if movies:
                        render_movie_grid(movies[:12], tmdb_key)
                    else:
                        st.warning("No movies found.")
                except Exception as e:
                    st.error(f"Error: {e}")
    except Exception as e:
        st.error(f"Could not load genres. Check your secrets config. ({e})")
