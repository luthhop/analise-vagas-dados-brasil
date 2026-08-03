from __future__ import annotations

import sqlite3
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DB_PATH = ROOT / "data" / "processed" / "vagas_dados.db"
VAGAS_PATH = ROOT / "data" / "processed" / "vagas_tratadas.csv"
SKILLS_PATH = ROOT / "data" / "processed" / "vagas_skills.csv"


def load_sqlite() -> Path:
    vagas = pd.read_csv(VAGAS_PATH)
    skills = pd.read_csv(SKILLS_PATH)

    with sqlite3.connect(DB_PATH) as conn:
        vagas.to_sql("vagas", conn, if_exists="replace", index=False)
        skills.to_sql("vagas_skills", conn, if_exists="replace", index=False)

    return DB_PATH


if __name__ == "__main__":
    print(f"Banco SQLite criado em: {load_sqlite()}")
