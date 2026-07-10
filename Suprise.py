
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st
from wordcloud import WordCloud


# À PERSONNALISER : tes données


PRENOM = "Madame Rose" # <- son prénom

DEPUIS = "2024" # <- année où elle a commencé à t'encadrer

# Timeline des moments clés de votre
accompagnement : (date, événement)
TIMELINE = [
("2024-08-05", "Première séance ensemble"),

("2024-11-28", "Premier contrôle réussi grâce à ses conseils"),

("2025-06-16", "Un moment où elle t'a vraiment débloqué sur un chapitre"),


("2025-07-09", "Objectif atteint" ),

]
# Mots ou expressions qu'elle utilise souvent, ou qui résument ses conseils

MOTS_FREQUENTS = """
courage methode organisation revision
patience,
tu peux le faire concentration exercice
rigueur
progres confiance travail perseverance arrange ton ecriture
"""
# Statistiques de votre accompagnement — à remplir toi-même, même approximatif

STATS = {
"Séances de révision faites ensemble": 42,

"Exercices corrigés":999,
"Fois où elle a dit 'tu vas y arriver'":999,


"Fous rires pendant les pauses":999,
}
# Progression scolaire : (date, note obtenue) — remplace par tes vraies notes

PROGRESSION = [
("2024-09-01", 9.5),
("2024-11-01", 11.0),
("2025-01-15", 12.5),
("2025-03-01", 14.0),
("2025-06-01", 16.0),
]

# CONFIG PAGE

st.set_page_config(page_title=f"Wrapped de {PRENOM}", page_icon="🎓",
layout="centered")
st.markdown(
"""

<style>
.big-title { font-size: 42px; fontweight:800; text-align: center; }

.subtitle { font-size: 18px; textalign:center; color: #888; }

</style>
""",
unsafe_allow_html=True,
)

# INTRO — effet "chargement"

def intro():
    st.markdown(f'<p class="big-title"> 🎓 Ton Wrapped {DEPUIS}–2026</p>', unsafe_allow_html=True)
    
   
    st.markdown('<p class="subtitle">Chargement de notre  année de travail...</p>', unsafe_allow_html=True)
   
    
   
    progress = st.progress(0)
    for i in range(100):
        time.sleep(0.01)
        progress.progress(i + 1)
        st.balloons()

# SECTION 1 — Timeline

def section_timeline():
    st.header("📅 Les moments clés de nos séances")

    df = pd.DataFrame(TIMELINE,columns=["date", "evenement"])
    
    df["date"] =pd.to_datetime(df["date"])
    
    df = df.sort_values("date")
    fig = px.scatter(
    df, x="date", y=[1] * len(df),text="evenement",
    
    title="Chronologie de notre accompagnement",

    )
    fig.update_traces(textposition="top center", marker=dict(size=14,color="seagreen"))

    
    fig.update_yaxes(visible=False)
    st.plotly_chart(fig, use_container_width=True)

   
# SECTION 2 — Wordcloud

def section_wordcloud():
    st.header("☁️ Vos mots, vos conseils")

    wc = WordCloud(width=800,height=400, background_color="white",colormap="viridis").generate(MOTS_FREQUENTS)
    fig, ax = plt.subplots()
    ax.imshow(wc,interpolation="bilinear")
    ax.axis("off")
    st.pyplot(fig)
# SECTION 3 — Stats

def section_stats():
    st.header("📊 Notre année en chiffres")

    df =pd.DataFrame(list(STATS.items()),columns=["Stat", "Valeur"])
    fig = px.bar(df, x="Valeur", y="Stat", orientation="h",color="Valeur",color_continuous_scale="tealgrn")
    st.plotly_chart(fig, use_container_width=True)
   
    cols = st.columns(len(STATS))
    for col, (label, val) in zip(cols,STATS.items()):
    
        col.metric(label, val)

# SECTION 4 — Progression scolaire

def section_progression():
    st.header("📈 Ma progression grâce à vous")

    df = pd.DataFrame(PROGRESSION, columns=["date", "note"])
   
    df["date"] =pd.to_datetime(df["date"])
    
    df = df.sort_values("date")
    fig = px.line(df, x="date",y="note", markers=True,title="Évolution de mes notes")
    
    
    fig.update_traces(line_color="seagreen", line_width=3, marker=dict(size=10))
    
    fig.update_yaxes(title="Note /20", range=[0, 20])
   
    st.plotly_chart(fig, use_container_width=True)
   
    debut, fin = df["note"].iloc[0],df["note"].iloc[-1]
    
    st.success(f"De {debut}/20 à {fin}/20 — grâce à vous. 🎉")

# SECTION 5 — Le modèle "ML" (clin d'oeil)


def section_prediction():
    st.header("🤖 Modèle prédictif (certifié 100% pas sérieux)")

    st.write("Un modèle de régression a été entraîné sur mes progrès.")

    x = np.arange(0, 10)
    y = 2 * x + np.random.normal(0, 1, size=10) + 5
   
    fig, ax = plt.subplots()
    ax.scatter(x, y, label="Progrès observés")

    coeffs = np.polyfit(x, y, 1)
    ax.plot(x, coeffs[0] * x +coeffs[1], color="seagreen",label="Régression linéaire")
    
    
    ax.set_xlabel("Temps encadré par vous")
    ax.set_ylabel("Niveau de réussite")
    ax.legend()
    st.pyplot(fig)
    st.success("Conclusion du modèle : coefficient positif et statistiquement... mérité. 🎓")



# SECTION FINALE — message perso

def section_message():
    st.header("💌 Merci")
    st.write(
    """
    Madame,
    Vous allez parfois vous demander pourquoi senan vous appelle de cette manière.
    Et bien, c'est tout simplement parcequ'elle trouve en vous un modele important qu'il est bénefique pour elle de vous vouer cet respect.
    Il est vrai que votre mission initiale était de m'assister et de m,encadrer en Mathematiques
    
    """
    )
    
# MAIN
  
def main():
    intro()
    section_timeline()
    section_wordcloud()
    section_stats()
    section_progression()
    section_prediction()
    section_message()
if __name__ == "__main__":
    main()
