# Guia de coleta manual de vagas

Este guia define um processo simples para complementar a base simulada do projeto com vagas reais de entrada na area de dados.

## Objetivo

Coletar vagas reais de estagio, assistente, entrada ou junior em dados para analisar quais habilidades aparecem com mais frequencia no mercado brasileiro.

## Fontes sugeridas

Use fontes publicas ou plataformas em que voce esteja navegando manualmente:

- LinkedIn
- Gupy
- Indeed
- Glassdoor
- Programathor
- Sites de empresas
- Paginas de carreira de startups

Evite scraping automatico nesta etapa. A ideia e fazer uma coleta pequena, controlada e bem documentada.

## Quantidade inicial

Para a primeira versao realista, busque entre **30 e 50 vagas**.

Essa quantidade ja permite observar padroes iniciais sem transformar a coleta em uma tarefa pesada.

## Criterios de inclusao

Inclua vagas que tenham pelo menos uma destas caracteristicas:

- estagio em dados;
- analista de dados junior;
- estagiario de BI;
- assistente de BI;
- assistente de dados;
- analytics intern;
- data analyst intern;
- business intelligence junior.

## Criterios de exclusao

Evite vagas que sejam claramente:

- pleno;
- senior;
- coordenacao;
- gerencia;
- engenharia de dados avancada;
- ciencia de dados com foco pesado em machine learning;
- vagas fora do Brasil, caso o objetivo da analise continue sendo mercado brasileiro.

## Campos para preencher

Use o arquivo `data/raw/modelo_coleta_vagas.csv` como base.

Campos principais:

- `id`: identificador sequencial da vaga.
- `data_coleta`: data em que a vaga foi registrada.
- `fonte`: plataforma ou site onde a vaga foi encontrada.
- `url`: link da vaga.
- `titulo`: titulo da vaga.
- `empresa`: nome da empresa.
- `localidade`: cidade, estado ou texto informado na vaga.
- `estado`: sigla do estado quando identificavel.
- `modalidade`: remoto, hibrido, presencial ou nao informado.
- `nivel`: estagio, entrada, junior ou nao informado.
- `salario_min`: salario minimo quando informado.
- `salario_max`: salario maximo quando informado.
- `descricao`: resumo ou trecho da descricao com requisitos e atividades.

## Boas praticas

- Copie apenas informacoes necessarias para analise.
- Registre a URL para rastreabilidade.
- Se o salario nao for informado, deixe vazio.
- Se a modalidade nao estiver clara, use `Nao informado`.
- Padronize estados com siglas, como `SP`, `RJ`, `MG`.
- Nao inclua dados pessoais de recrutadores ou candidatos.

## Proximo passo tecnico

Depois da coleta, o pipeline podera ser ajustado para usar uma base real, mantendo a base simulada apenas como exemplo ou fallback.
