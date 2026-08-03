from __future__ import annotations

import re
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
RAW_PATH = ROOT / "data" / "raw" / "vagas_dados_br.csv"
PROCESSED_DIR = ROOT / "data" / "processed"
PROCESSED_PATH = PROCESSED_DIR / "vagas_tratadas.csv"
SKILLS_PATH = PROCESSED_DIR / "vagas_skills.csv"

SKILLS = {
    "SQL": [r"\bsql\b", r"postgresql", r"postgres"],
    "Python": [r"\bpython\b"],
    "Pandas": [r"\bpandas\b"],
    "Power BI": [r"power\s*bi"],
    "Excel": [r"\bexcel\b"],
    "Google Sheets": [r"google\s*sheets", r"planilhas"],
    "Looker Studio": [r"looker\s*studio"],
    "DAX": [r"\bdax\b"],
    "APIs": [r"\bapis?\b"],
    "Estatistica": [r"estatistica"],
}


def normalize_text(value: str) -> str:
    return re.sub(r"\s+", " ", str(value).strip().lower())


def extract_skills(description: str) -> list[str]:
    text = normalize_text(description)
    found: list[str] = []

    for skill, patterns in SKILLS.items():
        if any(re.search(pattern, text, flags=re.IGNORECASE) for pattern in patterns):
            found.append(skill)

    return found


def transform() -> tuple[pd.DataFrame, pd.DataFrame]:
    df = pd.read_csv(RAW_PATH)

    df["salario_medio"] = df[["salario_min", "salario_max"]].mean(axis=1)
    df["titulo_normalizado"] = df["titulo"].str.lower().str.strip()
    df["descricao_normalizada"] = df["descricao"].map(normalize_text)
    df["skills"] = df["descricao"].map(extract_skills)
    df["qtd_skills"] = df["skills"].map(len)

    skills_df = (
        df[["id", "titulo", "nivel", "modalidade", "estado", "skills"]]
        .explode("skills")
        .dropna(subset=["skills"])
        .rename(columns={"skills": "skill"})
        .reset_index(drop=True)
    )

    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    df.to_csv(PROCESSED_PATH, index=False)
    skills_df.to_csv(SKILLS_PATH, index=False)

    return df, skills_df


if __name__ == "__main__":
    vagas, skills = transform()
    print(f"Vagas tratadas: {len(vagas)}")
    print(f"Relacoes vaga-skill: {len(skills)}")
