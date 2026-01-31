# ===================== IMPORTS =====================
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score, davies_bouldin_score

# ===================== PAGE CONFIG =====================
st.set_page_config(
    page_title="Amazon Music Clustering",
    page_icon="🎧",
    layout="wide"
)

# ===================== CUSTOM CSS (NO WHITE BAR) =====================
st.markdown("""
<style>

/* ---------- GLOBAL ---------- */
.stApp {
    background: radial-gradient(circle at top, #141625, #07080f);
    color: #e5e7eb;
}

/* REMOVE EMPTY / WHITE BARS */
div[data-testid="stVerticalBlock"]:has(> div:empty) {
    display: none !important;
}
.block-container {
    padding-top: 3.5rem !important;
}

/* ---------- SIDEBAR ---------- */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0f172a, #020617);
    padding: 1.2rem;
}
section[data-testid="stSidebar"] h1 {
    font-size: 20px;
}
section[data-testid="stSidebar"] label {
    font-size: 15px;
    padding: 8px 12px;
    margin: 4px 0;
    border-radius: 10px;
    color: #e5e7eb !important;
}
section[data-testid="stSidebar"] label:hover {
    background: rgba(255,255,255,0.08);
}
section[data-testid="stSidebar"] input:checked + div {
    background: linear-gradient(90deg, #6366f1, #8b5cf6);
    color: white !important;
    border-radius: 10px;
}

/* ---------- TITLE ---------- */
.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: 900;
    background: linear-gradient(90deg, #a78bfa, #f0abfc);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 4px;
}
.sub-title {
    text-align: center;
    font-size: 15px;
    color: #a1a1aa;
    margin-bottom: 28px;
}

/* ---------- CARDS ---------- */
.card {
    background: rgba(255,255,255,0.06);
    backdrop-filter: blur(18px);
    border-radius: 20px;
    padding: 26px;
    margin-bottom: 26px;
    border: 1px solid rgba(255,255,255,0.12);
    box-shadow: 0 10px 40px rgba(0,0,0,0.45);
}

/* ---------- FOOTER ---------- */
.footer {
    text-align: center;
    color: #9ca3af;
    font-size: 13px;
    margin-top: 40px;
}
.block-container {
    padding-top: 3.5rem !important;
}

.main-title {
    margin-top: 0.8rem;
}

div[data-testid="stVerticalBlock"]:has(> div:empty),
div[data-testid="stHorizontalBlock"]:has(> div:empty),
div[data-testid="stContainer"]:empty {
    display: none !important;
}

</style>
""", unsafe_allow_html=True)

# ===================== TITLE =====================
st.markdown("<div class='main-title'>🎧 Amazon Music Clustering Dashboard</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Unsupervised Learning • Music Analytics • K-Means</div>", unsafe_allow_html=True)

# ===================== LOAD DATA & MODELS =====================
df = pd.read_csv("amazon_music_clustered.csv")

features = [
    'danceability','energy','loudness','speechiness',
    'acousticness','instrumentalness','liveness',
    'valence','tempo','duration_ms'
]

kmeans = joblib.load("kmeans_model.pkl")
scaler = joblib.load("scaler.pkl")

# ===================== SIDEBAR NAV =====================
st.sidebar.markdown("## 🎛️ Navigation")
menu = st.sidebar.radio(
    "Go to",
    [
        "📊 Dataset Overview",
        "🎯 Cluster Evaluation",
        "📈 PCA Visualization",
        "🎼 Feature Analysis",
        "🎶 Mood Recommendation",
        "🎧 Predict New Song",
        "🧠 Final Insights"
    ]
)

# ===================== 1. DATASET OVERVIEW =====================
if menu == "📊 Dataset Overview":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<h2 style='color:white;'>📊 Dataset Overview</h2>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    col1.metric("🎵 Total Songs", f"{df.shape[0]:,}")
    col2.metric("🎚️ Features Used", len(features))
    col3.metric("🧩 Clusters", df['Cluster'].nunique())

    st.markdown("### 🔍 Sample Data")
    st.dataframe(df.head(8), use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ===================== 2. CLUSTER EVALUATION =====================
elif menu == "🎯 Cluster Evaluation":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<h2 style='color:white;'>🎯 Cluster Evaluation</h2>", unsafe_allow_html=True)

    X = df[features]
    sil = silhouette_score(X, df['Cluster'])
    dbi = davies_bouldin_score(X, df['Cluster'])

    col1, col2 = st.columns(2)
    col1.metric("Silhouette Score", f"{sil:.3f}")
    col2.metric("Davies–Bouldin Index", f"{dbi:.3f}")

    st.info("✔ Higher Silhouette & lower Davies–Bouldin = better clustering")
    st.markdown("</div>", unsafe_allow_html=True)

# ===================== 3. PCA VISUALIZATION =====================
elif menu == "📈 PCA Visualization":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<h2 style='color:white;'>📈 PCA Visualization</h2>", unsafe_allow_html=True)

    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(df[features])

    fig, ax = plt.subplots(figsize=(9,6))
    sc = ax.scatter(X_pca[:,0], X_pca[:,1], c=df['Cluster'], cmap='plasma', alpha=0.6)
    ax.set_facecolor("#0e0e16")
    fig.patch.set_facecolor("#0e0e16")
    ax.set_title("Clusters in PCA Space", color="white")
    ax.set_xlabel("PC1", color="white")
    ax.set_ylabel("PC2", color="white")
    ax.tick_params(colors="white")
    plt.colorbar(sc)

    st.pyplot(fig)
    st.markdown("</div>", unsafe_allow_html=True)

# ===================== 4. FEATURE ANALYSIS =====================
elif menu == "🎼 Feature Analysis":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<h2 style='color:white;'>🎼 Feature Analysis</h2>", unsafe_allow_html=True)

    feature = st.selectbox("Select Feature", features)
    fig, ax = plt.subplots(figsize=(8,5))
    sns.boxplot(x='Cluster', y=feature, data=df, palette='viridis', ax=ax)
    ax.set_title(f"{feature.capitalize()} Distribution Across Clusters")
    st.pyplot(fig)

    st.caption("Outliers represent unique or rare musical styles.")
    st.markdown("</div>", unsafe_allow_html=True)

# ===================== 5. MOOD RECOMMENDATION =====================
elif menu == "🎶 Mood Recommendation":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<h2 style='color:white;'>🎶 Mood Recommendation</h2>", unsafe_allow_html=True)

    mood = st.selectbox(
        "Choose your mood",
        ["😊 Happy / Party", "😌 Chill / Relax", "🔥 Energetic"]
    )

    if mood == "😊 Happy / Party":
        cluster = 1
    elif mood == "😌 Chill / Relax":
        cluster = 0
    else:
        cluster = 2

    st.success(f"🎵 Recommended Cluster: {cluster}")
    st.dataframe(df[df['Cluster'] == cluster].head(5), use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ===================== 6. PREDICT NEW SONG =====================
elif menu == "🎧 Predict New Song":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<h2 style='color:white;'>🎧 Predict New Song</h2>", unsafe_allow_html=True)

    inputs = [
        st.slider("Danceability", 0.0, 1.0, 0.5),
        st.slider("Energy", 0.0, 1.0, 0.5),
        st.slider("Loudness", -60.0, 0.0, -20.0),
        st.slider("Speechiness", 0.0, 1.0, 0.1),
        st.slider("Acousticness", 0.0, 1.0, 0.5),
        st.slider("Instrumentalness", 0.0, 1.0, 0.0),
        st.slider("Liveness", 0.0, 1.0, 0.2),
        st.slider("Valence", 0.0, 1.0, 0.5),
        st.slider("Tempo", 50.0, 200.0, 120.0),
        st.slider("Duration (ms)", 60000, 400000, 200000)
    ]

    if st.button("🎯 Predict Cluster"):
        scaled = scaler.transform([inputs])
        pred = kmeans.predict(scaled)[0]
        st.success(f"🎵 This song belongs to Cluster {pred}")

    st.markdown("</div>", unsafe_allow_html=True)

# ===================== 7. FINAL INSIGHTS =====================
elif menu == "🧠 Final Insights":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<h2 style='color:white;'>🧠 Final Insights</h2>", unsafe_allow_html=True)

    profile = df.groupby("Cluster")[features].mean()
    st.dataframe(profile.style.background_gradient(cmap="plasma"), use_container_width=True)

    st.success("""
    🔹 Cluster 0 → Chill / Acoustic / Low Energy  
    🔹 Cluster 1 → Party / High Energy / Fast Tempo  
    🔹 Cluster 2 → Rap / Live / Speech Dominant  
    """)

    st.markdown("</div>", unsafe_allow_html=True)

# ===================== FOOTER =====================
st.markdown("<div class='footer'>🚀 Built with Streamlit | Amazon Music Clustering Project</div>", unsafe_allow_html=True)
