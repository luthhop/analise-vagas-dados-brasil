from __future__ import annotations

from pathlib import Path

import altair as alt
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


def format_currency(value: float) -> str:
    if pd.isna(value):
        return "R$ 0"

    return f"R$ {value:,.0f}".replace(",", ".")


def bar_chart(data: pd.DataFrame, x: str, y: str, tooltip: list[str], height: int = 320) -> alt.Chart:
    return (
        alt.Chart(data)
        .mark_bar(color="#7cc4f8", cornerRadiusEnd=4)
        .encode(
            x=alt.X(f"{x}:Q", title=None),
            y=alt.Y(f"{y}:N", sort="-x", title=None),
            tooltip=tooltip,
        )
        .properties(height=height)
    )

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
col2.metric("Salario medio", format_currency(filtered["salario_medio"].mean()))
col3.metric("Estados", filtered["estado"].nunique())
col4.metric("Skills mapeadas", filtered_skills["skill"].nunique())

if filtered.empty:
    st.warning("Nenhuma vaga encontrada com os filtros selecionados.")
    st.stop()

left, right = st.columns(2)

with left:
    st.subheader("Skills mais citadas")
    top_skills = (
        filtered_skills["skill"]
        .value_counts()
        .rename_axis("skill")
        .reset_index(name="mencoes")
        .sort_values("mencoes", ascending=False)
    )
    st.altair_chart(bar_chart(top_skills, "mencoes", "skill", ["skill", "mencoes"]), width="stretch")

with right:
    st.subheader("Vagas por modalidade")
    modality_data = (
        filtered["modalidade"]
        .value_counts()
        .rename_axis("modalidade")
        .reset_index(name="vagas")
        .sort_values("vagas", ascending=False)
    )
    st.altair_chart(bar_chart(modality_data, "vagas", "modalidade", ["modalidade", "vagas"]), width="stretch")

left, right = st.columns(2)

with left:
    st.subheader("Vagas por estado")
    state_data = (
        filtered["estado"]
        .value_counts()
        .rename_axis("estado")
        .reset_index(name="vagas")
        .sort_values("vagas", ascending=False)
    )
    st.altair_chart(bar_chart(state_data, "vagas", "estado", ["estado", "vagas"]), width="stretch")

with right:
    st.subheader("Salario medio por nivel")
    salary_data = (
        filtered.groupby("nivel", as_index=False)["salario_medio"]
        .mean()
        .sort_values("salario_medio", ascending=False)
    )
    salary_chart = bar_chart(salary_data, "salario_medio", "nivel", ["nivel", "salario_medio"])
    st.altair_chart(salary_chart, width="stretch")

st.subheader("Base filtrada")
table_data = filtered.copy()
table_data["skills"] = table_data["skills"].str.replace("[", "", regex=False).str.replace("]", "", regex=False)

st.dataframe(
    table_data[
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
    width="stretch",
    hide_index=True,
)
