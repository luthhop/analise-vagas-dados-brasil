from __future__ import annotations

from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
VAGAS_PATH = ROOT / "data" / "processed" / "vagas_tratadas.csv"
SKILLS_PATH = ROOT / "data" / "processed" / "vagas_skills.csv"
REPORT_PATH = ROOT / "reports" / "resumo_executivo.md"


def format_currency(value: float) -> str:
    return f"R$ {value:,.0f}".replace(",", ".")


def markdown_table(series: pd.Series, value_name: str) -> str:
    table = series.reset_index()
    table.columns = [table.columns[0], value_name]
    first_col, second_col = table.columns
    rows = [f"| {first_col} | {second_col} |", "| --- | ---: |"]

    for _, row in table.iterrows():
        rows.append(f"| {row[first_col]} | {row[second_col]} |")

    return "\n".join(rows)


def build_report() -> str:
    vagas = pd.read_csv(VAGAS_PATH)
    skills = pd.read_csv(SKILLS_PATH)

    top_skills = skills["skill"].value_counts().head(10)
    modalidades = vagas["modalidade"].value_counts()
    estados = vagas["estado"].value_counts().head(10)
    salario_nivel = vagas.groupby("nivel")["salario_medio"].mean().sort_values(ascending=False)

    insights = [
        "SQL aparece como a habilidade mais recorrente e deve ser prioridade para entrada em dados.",
        "Power BI, Python e Excel formam um conjunto forte para vagas de estagio e junior.",
        "Vagas hibridas e remotas aparecem com peso relevante na amostra.",
        "A diferenca salarial entre estagio, entrada e junior reforca a importancia de evoluir portfolio e SQL.",
    ]

    return f"""# Resumo executivo

## Visao geral

- Vagas analisadas: {len(vagas)}
- Empresas na base: {vagas["empresa"].nunique()}
- Estados representados: {vagas["estado"].nunique()}
- Salario medio geral: {format_currency(vagas["salario_medio"].mean())}

## Top skills

{markdown_table(top_skills, "total_mencoes")}

## Vagas por modalidade

{markdown_table(modalidades, "total_vagas")}

## Vagas por estado

{markdown_table(estados, "total_vagas")}

## Salario medio por nivel

{markdown_table(salario_nivel.map(format_currency), "salario_medio")}

## Insights iniciais

{chr(10).join(f"- {insight}" for insight in insights)}

## Recomendacao de estudo

Para uma pessoa iniciante buscando estagio ou primeira vaga em dados, a ordem sugerida pela analise e:

1. SQL
2. Excel ou Google Sheets
3. Power BI
4. Python com Pandas
5. Estatistica descritiva
"""


def main() -> None:
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(build_report(), encoding="utf-8")
    print(f"Relatorio gerado em: {REPORT_PATH}")


if __name__ == "__main__":
    main()
