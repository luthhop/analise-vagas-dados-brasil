# Analise de Vagas de Dados para Iniciantes no Brasil

Projeto de Data Analytics desenvolvido com abordagem **AI-assisted**, com o objetivo de entender quais habilidades, ferramentas e condicoes aparecem com mais frequencia em vagas de entrada na area de dados no Brasil.

> Status: primeira versao funcional com base simulada. A proxima evolucao sera substituir ou complementar a base com dados reais coletados de fontes publicas ou exportacoes manuais.

## Problema

Quem busca o primeiro estagio ou vaga junior em dados costuma encontrar muitas listas de tecnologias: SQL, Python, Excel, Power BI, estatistica, cloud, machine learning e varias outras. Este projeto transforma esse problema em uma pergunta analitica:

**Quais habilidades aparecem com mais frequencia em vagas de dados para iniciantes no Brasil?**

## Perguntas de negocio

- Quais skills sao mais citadas nas vagas?
- Quais modalidades aparecem mais: remoto, hibrido ou presencial?
- Quais estados concentram mais oportunidades?
- Como a media salarial varia por nivel e modalidade?
- Quais ferramentas uma pessoa iniciante deveria priorizar?

## Tecnologias

- Python
- Pandas
- SQLite
- SQL
- Streamlit

## Estrutura

```text
data/
  raw/
  processed/
dashboard/
queries/
reports/
src/
```

## Como executar

Instale as dependencias:

```bash
pip install -r requirements.txt
```

Execute o pipeline:

```bash
python src/run_pipeline.py
```

Abra o dashboard:

```bash
streamlit run dashboard/app.py
```

## Resultados iniciais

Na base simulada desta primeira versao, as skills mais recorrentes sao SQL, Power BI, Python e Excel. Isso reforca uma priorizacao realista para quem busca entrada em dados:

1. SQL
2. Excel ou Google Sheets
3. Power BI
4. Python com Pandas
5. Estatistica descritiva

## Metodologia AI-assisted

Este projeto foi conduzido com IA generativa como parceira de desenvolvimento. A IA apoiou a criacao de codigo, estrutura do projeto, documentacao e sugestao de analises.

A conducao humana ficou responsavel por:

- definicao do problema;
- escolha da narrativa do projeto;
- revisao das perguntas analiticas;
- validacao dos resultados;
- decisao sobre proximos passos.
