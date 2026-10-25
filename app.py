import streamlit as st
import pandas as pd
import plotly.express as px

# Konfigurasi halaman
st.set_page_config(page_title="Dashboard Netflix Originals", layout="wide")

# Injeksi CSS Tema Gelap ala Netflix & Logo di Tengah
st.markdown("""
<style>
    .stApp {
        background-color: #141414;
        color: #E5E5E5;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    h1, h2, h3 {
        color: #E50914 !important;
        font-weight: 700;
    }
    p, li, label {
        color: #FFFFFF !important;
        font-size: 15px;
    }
    .metric-card {
        background-color: #1f1f1f;
        padding: 15px;
        border-radius: 8px;
        border-left: 4px solid #E50914;
        text-align: center;
    }
    /* Logo Netflix di Tengah */
    .netflix-logo-center {
        color: #E50914;
        font-size: 55px;
        font-weight: 900;
        letter-spacing: 5px;
        text-align: center;
        margin: 0 0 10px 0;
        line-height: 1;
        text-shadow: 2px 2px 6px rgba(0,0,0,0.7);
    }
    /* Styling Kartu Poster Film */
    .movie-card {
        background-color: #1f1f1f;
        border-radius: 6px;
        overflow: hidden;
        text-align: center;
        padding-bottom: 10px;
        transition: transform 0.3s;
        height: 100%;
    }
    .movie-card:hover {
        transform: scale(1.05);
    }
    .movie-title {
        color: #ffffff;
        font-size: 13px;
        font-weight: bold;
        margin-top: 8px;
        padding: 0 5px;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
    }
    /* Styling Footer ala Netflix */
    .netflix-footer {
        background-color: #000000;
        color: #757575;
        padding: 40px 20px;
        margin-top: 50px;
        border-top: 1px solid #333333;
        font-size: 14px;
    }
    .netflix-footer a {
        color: #757575;
        text-decoration: none;
        margin-right: 20px;
        display: inline-block;
        margin-bottom: 10px;
    }
    .netflix-footer a:hover {
        text-decoration: underline;
        color: #ffffff;
    }
    .footer-title {
        color: #757575;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Memuat dan Membersihkan Data
# ---------------------------------------------------------
@st.cache_data
def load_and_clean_data():
    df = pd.read_csv("../data/netflix_clean.csv")
    df["Premiere"] = df["Premiere"].str.replace(r"(\d{1,2})\.\s*(\d{4})", r"\1, \2", regex=True)
    df["Premiere"] = pd.to_datetime(df["Premiere"], errors="coerce")
    df["Year"] = df["Premiere"].dt.year.astype(int)
    return df

df_clean = load_and_clean_data()

# ---------------------------------------------------------
# Header dengan Logo Netflix di Tengah & Judul Rata Kiri
# ---------------------------------------------------------
st.markdown('<p class="netflix-logo-center">NETFLIX</p>', unsafe_allow_html=True)

st.title("Dashboard Analisis Film Netflix Original")
st.write(
    "Dashboard ini menjawab pertanyaan seputar distribusi bahasa, performa skor IMDb, dan tren genre "
    "berdasarkan sumber data **Netflix Originals & IMDb Scores** yang telah melalui proses pembersihan data."
)
st.divider()

# ---------------------------------------------------------
# Bagian Film Sedang Tren
# ---------------------------------------------------------
st.subheader("🔥 Sedang Tren Sekarang (Top Trending Originals)")
st.write("Berikut adalah beberapa film unggulan dengan rating tertinggi yang sedang populer di platform:")

trending_films = df_clean.nlargest(5, "IMDB Score")

new_posters = [
    "https://picsum.photos/id/1011/400/600",
    "https://picsum.photos/id/1025/400/600",
    "https://picsum.photos/id/1069/400/600",
    "https://picsum.photos/id/1074/400/600",
    "https://picsum.photos/id/1084/400/600"
]

cols_poster = st.columns(5)
for idx, (_, row) in enumerate(trending_films.iterrows()):
    title = row["Title"]
    score = row["IMDB Score"]
    img_url = new_posters[idx % len(new_posters)]
    
    with cols_poster[idx]:
        st.markdown(f"""
        <div class="movie-card">
            <img src="{img_url}" width="100%" style="height: 240px; object-fit: cover; border-top-left-radius: 6px; border-top-right-radius: 6px;">
            <div class="movie-title" title="{title}">{title}</div>
            <p style="color: #46d369 !important; font-size: 13px; margin: 5px 0 0 0; font-weight: bold;">IMDb: {score}</p>
        </div>
        """, unsafe_allow_html=True)

st.divider()

# ---------------------------------------------------------
# Filter Dashboard (Sidebar)
# ---------------------------------------------------------
st.sidebar.header("🔍 Filter & Pencarian Dashboard")

search_query = st.sidebar.text_input("Cari Judul Film:", "", placeholder="Ketik judul film...")

selected_imdb = st.sidebar.slider(
    "Pilih Rentang Skor IMDb:",
    min_value=0.0,
    max_value=10.0,
    value=(0.0, 10.0),
    step=0.1
)

all_years = sorted(df_clean["Year"].dropna().unique().tolist(), reverse=True)
selected_years = st.sidebar.multiselect(
    "Pilih Tahun Film:",
    options=all_years,
    default=all_years
)

all_languages = sorted(df_clean["Language"].dropna().unique().tolist())
selected_languages = st.sidebar.multiselect(
    "Pilih Bahasa Film (Language):",
    options=all_languages,
    default=all_languages
)

all_genres = sorted(df_clean["Genre"].dropna().unique().tolist())
selected_genres = st.sidebar.multiselect(
    "Pilih Genre:",
    options=all_genres,
    default=all_genres
)

df_filtered = df_clean[
    (df_clean["IMDB Score"] >= selected_imdb[0]) & 
    (df_clean["IMDB Score"] <= selected_imdb[1]) &
    (df_clean["Year"].isin(selected_years)) &
    (df_clean["Language"].isin(selected_languages)) &
    (df_clean["Genre"].isin(selected_genres)) &
    (df_clean["Title"].str.contains(search_query, case=False, na=False))
]

# ---------------------------------------------------------
# Metrik Utama (KPI)
# ---------------------------------------------------------
st.subheader("📊 Ringkasan Metrik Utama (KPI)")
col_kpi1, col_kpi2, col_kpi3, col_kpi4 = st.columns(4)

total_film = len(df_filtered)
avg_imdb = round(df_filtered["IMDB Score"].mean(), 2) if total_film > 0 else 0
avg_runtime = round(df_filtered["Runtime"].mean(), 1) if total_film > 0 else 0
total_bahasa = df_filtered["Language"].nunique()

with col_kpi1:
    st.markdown(f"""<div class="metric-card"><h3>{total_film}</h3><p>Total Film</p></div>""", unsafe_allow_html=True)
with col_kpi2:
    st.markdown(f"""<div class="metric-card"><h3>{avg_imdb}</h3><p>Rata-rata Skor IMDb</p></div>""", unsafe_allow_html=True)
with col_kpi3:
    st.markdown(f"""<div class="metric-card"><h3>{avg_runtime} mnt</h3><p>Rata-rata Durasi</p></div>""", unsafe_allow_html=True)
with col_kpi4:
    st.markdown(f"""<div class="metric-card"><h3>{total_bahasa}</h3><p>Variasi Bahasa</p></div>""", unsafe_allow_html=True)

st.divider()

def apply_plotly_theme(fig, title, xaxis_title, yaxis_title):
    fig.update_layout(
        title=dict(text=title, font=dict(color='white', size=16)),
        paper_bgcolor='#141414',
        plot_bgcolor='#141414',
        font=dict(color='white'),
        xaxis=dict(title=xaxis_title, gridcolor='#333333'),
        yaxis=dict(title=yaxis_title, gridcolor='#333333'),
        margin=dict(t=50, b=30, l=30, r=30)
    )

if df_filtered.empty:
    st.warning("⚠️ Tidak ada data film yang cocok dengan pencarian atau kombinasi filter Anda.")
else:
    # ---------------------------------------------------------
    # Grafik Interaktif & Insight Berstruktur
    # ---------------------------------------------------------
    st.subheader("1. Analisis Bahasa Dominan dalam Konten")
    col_g1, col_i1 = st.columns([2, 1])

    bahasa_top = df_filtered["Language"].value_counts().head(10).reset_index()
    bahasa_top.columns = ['Language', 'Count']

    fig1 = px.bar(bahasa_top, x='Language', y='Count', text='Count', color_discrete_sequence=['#E50914'])
    apply_plotly_theme(fig1, "10 Bahasa Terbanyak pada Film Netflix Original", "Bahasa", "Jumlah Film")

    with col_g1:
        st.plotly_chart(fig1, use_container_width=True)
    with col_i1:
        st.markdown("### 💡 Insight & Rekomendasi")
        st.markdown("**Pertanyaan:** Bahasa apa yang paling mendominasi katalog Netflix Original?")
        st.markdown(f"**Temuan:** Berdasarkan filter terpilih, terdapat total **{total_film}** film yang masuk dalam kriteria.")
        st.markdown("**Bukti:** Grafik interaktif menunjukkan distribusi jumlah film berdasarkan bahasa.")
        st.markdown("**Rekomendasi:** Sesuaikan strategi distribusi konten berdasarkan preferensi bahasa audiens pada filter aktif.")

    st.divider()

    st.subheader("2. Analisis Konten dengan Kualitas Tertinggi")
    col_g2, col_i2 = st.columns([2, 1])

    film_imdb = df_filtered[df_filtered["IMDB Score"] >= 8.0].nlargest(10, "IMDB Score").sort_values("IMDB Score")

    fig2 = px.bar(film_imdb, x='IMDB Score', y='Title', orientation='h', text='IMDB Score', color_discrete_sequence=['#B3B3B3'])
    apply_plotly_theme(fig2, "10 Film dengan Skor IMDb Tertinggi (≥ 8.0)", "Skor IMDb", "Judul Film")
    if not film_imdb.empty:
        fig2.update_xaxes(range=[8.0, 10.0])

    with col_g2:
        if film_imdb.empty:
            st.info("Tidak ada film dengan skor IMDb ≥ 8.0 pada filter ini.")
        else:
            st.plotly_chart(fig2, use_container_width=True)
    with col_i2:
        st.markdown("### 💡 Insight & Rekomendasi")
        st.markdown("**Pertanyaan:** Film apa saja yang berhasil mencetak standar kualitas tertinggi (IMDb ≥ 8.0)?")
        st.markdown("**Temuan:** Menampilkan film pilihan terbaik yang lolos filter tahun, skor IMDb, bahasa, dan genre.")
        st.markdown("**Bukti:** Grafik horizontal menampilkan daftar judul spesifik beserta skor IMDb-nya.")
        st.markdown("**Rekomendasi:** Gunakan daftar film unggulan ini sebagai tolok ukur produksi masa depan.")

    st.divider()

    st.subheader("3. Analisis Tren Kategori Genre")
    col_g3, col_i3 = st.columns([2, 1])

    genre_top = df_filtered["Genre"].value_counts().head(10).reset_index()
    genre_top.columns = ['Genre', 'Count']
    genre_top = genre_top.sort_values('Count', ascending=True)

    fig3 = px.bar(genre_top, x='Count', y='Genre', orientation='h', text='Count', color_discrete_sequence=['#E50914'])
    apply_plotly_theme(fig3, "10 Genre Film Terbanyak Berdasarkan Filter", "Jumlah Film", "Genre")

    with col_g3:
        st.plotly_chart(fig3, use_container_width=True)
    with col_i3:
        st.markdown("### 💡 Insight & Rekomendasi")
        st.markdown("**Pertanyaan:** Genre apa yang paling menonjol pada filter yang diterapkan?")
        st.markdown("**Temuan:** Volume rilis terbanyak terkonsentrasi pada genre-genre tertentu sesuai pilihan filter.")
        st.markdown("**Bukti:** Grafik batang horizontal memperlihatkan perbandingan jumlah judul tiap genre.")
        st.markdown("**Rekomendasi:** Pertimbangkan alokasi sumber daya pada genre yang paling diminati dalam kategori filter ini.")

# ---------------------------------------------------------
# Footer ala Netflix
# ---------------------------------------------------------
st.markdown("""
<div class="netflix-footer">
    <div class="footer-title">Ada pertanyaan? Hubungi kelompok kami</div>
    <div style="display: flex; flex-wrap: wrap; justify-content: space-between; max-width: 900px;">
        <div style="flex: 1; min-width: 200px; margin-bottom: 20px;">
            <a href="#" target="_blank">Tanya Jawab (FAQ)</a><br>
            <a href="#" target="_blank">Pusat Bantuan</a><br>
        </div>
        <div style="flex: 1; min-width: 200px; margin-bottom: 20px;">
            <a href="#" target="_blank">Akun</a><br>
            <a href="#" target="_blank">Pusat Media</a><br>
        </div>
        <div style="flex: 1; min-width: 200px; margin-bottom: 20px;">
            <a href="#" target="_blank">Privasi</a><br>
            <a href="#" target="_blank">Hubungi Kami</a><br>
        </div>
    </div>
    <p style="color: #757575; font-size: 13px; margin-top: 20px;">Netflix Originals Analytics Dashboard &copy; 2026</p>
</div>
""", unsafe_allow_html=True)