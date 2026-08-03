from __future__ import annotations

from pathlib import Path

import pandas as pd
import streamlit as st


ROOT = Path(__file__).resolve().parents[1]
VAGAS_PATH = ROOT / "data" / "processed" / "vagas_tratadas.csv"
SKILLS_PATH = ROOT / "data" / "processed" / "vagas_skills.csv"


@st.cache_data
def load_data() -> tuple[pd.DataFrame, pd.DataFrame]:
    return pd.read_csv(VAGAS_PATH), pd.read_csv(SKILLS_PATH)


vagas, skills = load_data()

st.set_page_config(page_title="Analise de Vagas em Dados", page_icon=":bar_chart:", layout="wide")

st.title("Analise de Vagas de Dados para Iniciantes no Brasil")
st.caption("Projeto AI-assisted de Data Analytics com Python, Pandas, SQL e visualizacao.")

with st.sidebar:
    st.header("Filtros")
    niveis = st.multiselect("Nivel", sorted(vagas["nivel"].unique()), default=sorted(vagas["nivel"].unique()))
    modalidades = st.multiselect("Modalidade", sorted(vagas["modalidade"].unique()), default=sorted(vagas["modalidade"].unique()))
    estados = st.multiselect("Estado", sorted(vagas["estado"].unique()), default=sorted(vagas["estado"].unique()))

filtered = vagas[
    vagas["nivel"].isin(niveis)
    & vagas["modalidade"].isin(modalidades)
    & vagas["estado"].isin(estados)
]
filtered_skills = skills[skills["id"].isin(filtered["id"])]

col1, col2, col3, col4 = st.columns(4)
col1.metric("Vagas analisadas", len(filtered))
col2.metric("Salario medio", f"R$ {filtered['salario_medio'].mean():,.0f}".replace(",", "."))
col3.metric("Estados", filtered["estado"].nunique())
col4.metric("Skills mapeadas", filtered_skills["skill"].nunique())

left, right = st.columns(2)

with left:
    st.subheader("Skills mais citadas")
    st.bar_chart(filtered_skills["skill"].value_counts().sort_values(ascending=True))

with right:
    st.subheader("Vagas por modalidade")
    st.bar_chart(filtered["modalidade"].value_counts())

left, right = st.columns(2)

with left:
    st.subheader("Vagas por estado")
    st.bar_chart(filtered["estado"].value_counts())

with right:
    st.subheader("Salario medio por nivel")
    st.bar_chart(filtered.groupby("nivel")["salario_medio"].mean().sort_values())

st.subheader("Base filtrada")
st.dataframe(
    filtered[
        [
            "titulo",
            "empresa",
            "localidade",
            "estado",
            "modalidade",
            "nivel",
            "salario_min",
            "salario_max",
            "skills",
        ]
    ],
    use_container_width=True,
)
