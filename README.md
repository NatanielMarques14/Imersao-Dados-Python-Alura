# Análise de Salários na Área de Dados

Este projeto é uma introdução completa à análise de dados com Python, desenvolvido durante a Imersão Alura. O objetivo é explorar um dataset de salários de profissionais da área de dados ao redor do mundo, realizar análises estatísticas e construir uma dashboard interativa para visualização dos resultados.

## Objetivos do Projeto

1. **Introdução à Análise de Dados**: Aprender os fundamentos da análise exploratória de dados (EDA) utilizando Python e bibliotecas como Pandas, Matplotlib, Seaborn e Plotly.

2. **Limpeza e Preparação de Dados**: Praticar técnicas de tratamento de dados, incluindo identificação e remoção de valores nulos, conversão de tipos de dados e padronização de informações.

3. **Visualização de Dados**: Criar diferentes tipos de gráficos e visualizações para comunicar insights de forma clara e eficaz.

4. **Dashboard Interativa**: Desenvolver uma aplicação web interativa usando Streamlit que permite aos usuários explorar os dados de forma dinâmica através de filtros e visualizações interativas.

## Estrutura do Projeto

```
.
├── analise_cargos_de_dados.ipynb  # Notebook com a análise completa dos dados
├── app.py                         # Dashboard interativa com Streamlit
├── dados-imersao-final.csv        # Dataset limpo e processado
├── requirements.txt               # Dependências do projeto
└── README.md                      # Este arquivo
```

## O que foi feito no Notebook (analise_cargos_de_dados.ipynb)

O notebook está dividido em três aulas principais:

### Aula 1: Exploração Inicial dos Dados

- **Carregamento dos dados**: Importação do dataset de salários via URL usando Pandas
- **Primeira visualização**: Análise das primeiras linhas e estrutura do dataset
- **Informações gerais**: 
  - Dataset com 133.349 registros e 11 colunas
  - Informações sobre salários, experiência, tipo de contrato, localização e tamanho da empresa
- **Tradução de colunas**: Renomeação das colunas de inglês para português para facilitar a compreensão
- **Análise de distribuições**: 
  - Distribuição de níveis de senioridade (Junior, Pleno, Senior, Executivo)
  - Distribuição de tipos de contrato (Tempo Integral, Contrato, Meio Período, Freelancer)
  - Distribuição de modalidades de trabalho (Presencial, Híbrido, Remoto Total)
- **Mapeamento de valores**: Conversão de códigos e siglas para nomes descritivos em português
- **Estatísticas descritivas**: Análise de medidas de tendência central e dispersão

### Aula 2: Limpeza e Preparação de Dados

- **Identificação de valores nulos**: Detecção de 10 linhas com valores faltantes na coluna 'ano' (menos de 0,01% do dataset)
- **Técnicas de tratamento de dados**:
  - Preenchimento com média e mediana (demonstração com exemplos)
  - Forward fill (ffill) e backward fill (bfill)
  - Preenchimento com valores constantes
- **Remoção de valores nulos**: Uso de `dropna()` para remover linhas incompletas
- **Conversão de tipos**: Transformação da coluna 'ano' de float64 para int64
- **Dataset final**: 133.339 registros limpos e prontos para análise

### Aula 3: Visualização de Dados

- **Gráficos com Matplotlib e Seaborn**:
  - Gráficos de barras para distribuição de senioridade e salários médios
  - Histogramas para distribuição de salários
  - Boxplots para análise de outliers e distribuições por senioridade
- **Visualizações interativas com Plotly**:
  - Gráficos de barras interativos com ordenação personalizada
  - Gráficos de pizza/rosca (donut) para proporções
  - Mapas coropléticos (choropleth) mostrando salários médios por país para diferentes cargos
- **Análises específicas**:
  - Média salarial por nível de senioridade
  - Distribuição geográfica de salários de Data Scientists
  - Identificação de outliers e padrões salariais

### Principais Resultados Encontrados

1. **Distribuição de Senioridade**: A maioria dos profissionais está no nível Senior, indicando um mercado maduro
2. **Hierarquia Salarial**: Executivos > Senior > Pleno > Junior (conforme esperado)
3. **Distribuição de Salários**: Assimetria positiva, com maioria concentrada em valores menores e alguns outliers muito altos
4. **Disparidades Geográficas**: Países desenvolvidos (EUA, Canadá, Japão) apresentam salários significativamente maiores
5. **Modalidade de Trabalho**: Trabalho presencial ainda predomina no mercado

## Dashboard Interativa (app.py)

A dashboard foi construída usando **Streamlit**, uma biblioteca Python para criação de aplicações web interativas.

### Funcionalidades

1. **Filtros Interativos** (barra lateral):
   - Filtro por ano
   - Filtro por nível de senioridade
   - Filtro por tipo de contrato
   - Filtro por tamanho da empresa

2. **Métricas Gerais**:
   - Salário médio anual em USD
   - Salário máximo
   - Total de registros (após filtros)
   - Cargo mais frequente

3. **Visualizações Interativas**:
   - **Top 10 cargos por salário médio**: Gráfico de barras horizontal mostrando os cargos mais bem pagos
   - **Distribuição de salários anuais**: Histograma mostrando a distribuição dos salários
   - **Proporção dos tipos de trabalho**: Gráfico de rosca (donut) mostrando a distribuição entre Presencial, Híbrido e Remoto Total
   - **Mapas coropléticos por cargo**: Visualização geográfica dos salários médios para:
     - Cientista de Dados (Data Scientist)
     - Engenheiro de Dados (Data Engineer)
     - Analista de Dados (Data Analyst)

4. **Tabela de Dados Detalhados**: Exibição completa dos dados filtrados em formato tabular

### Tecnologias Utilizadas na Dashboard

- **Streamlit**: Framework para criação da interface web
- **Plotly Express**: Biblioteca para gráficos interativos
- **Pandas**: Manipulação e filtragem de dados

## Instalação e Uso

### Pré-requisitos

- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)

### Instalação

1. Clone ou baixe este repositório

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

### Executando a Dashboard

Para executar a dashboard interativa, use o comando:

```bash
streamlit run app.py
```

A aplicação será aberta automaticamente no seu navegador padrão, geralmente em `http://localhost:8501`

### Executando o Notebook

Para abrir e executar o notebook de análise:

```bash
jupyter notebook analise_cargos_de_dados.ipynb
```

Ou usando JupyterLab:

```bash
jupyter lab analise_cargos_de_dados.ipynb
```

## Dependências

As principais bibliotecas utilizadas no projeto são:

- `pandas==2.2.3`: Manipulação e análise de dados
- `streamlit==1.44.1`: Framework para dashboard web
- `plotly==5.24.1`: Gráficos interativos
- `matplotlib==3.8.0`: Visualizações estáticas
- `seaborn==0.13.2`: Visualizações estatísticas avançadas
- `nbformat>=4.2.0`: Suporte para notebooks Jupyter
- `ipython`: Ambiente interativo Python

## Sobre o Dataset

O dataset utilizado contém informações sobre salários de profissionais da área de dados coletados de diferentes fontes. As principais colunas incluem:

- **ano**: Ano da observação
- **senioridade**: Nível de experiência (Junior, Pleno, Senior, Executivo)
- **contrato**: Tipo de contrato (Tempo Integral, Contrato, Meio Período, Freelancer)
- **cargo**: Título do cargo
- **salario**: Salário na moeda original
- **moeda**: Moeda do salário
- **usd**: Salário convertido para USD
- **residencia**: País de residência do funcionário (código ISO2)
- **remoto**: Modalidade de trabalho (Presencial, Híbrido, Remoto Total)
- **empresa**: Localização da empresa (código ISO2)
- **tamanho_empresa**: Tamanho da empresa (Pequena, Média, Grande)

## Aprendizados

Este projeto demonstra:

1. **Ciclo completo de análise de dados**: Desde a exploração inicial até a criação de uma aplicação interativa
2. **Boas práticas de limpeza de dados**: Identificação e tratamento adequado de valores faltantes
3. **Visualização eficaz**: Escolha de gráficos apropriados para diferentes tipos de análises
4. **Desenvolvimento de aplicações interativas**: Criação de dashboards que permitem exploração dinâmica dos dados
5. **Comunicação de insights**: Apresentação clara e visualmente atraente dos resultados

## Próximos Passos

Possíveis melhorias e extensões do projeto:

- Adicionar mais filtros (por cargo, país, etc.)
- Implementar análises de tendências temporais
- Adicionar comparações entre diferentes variáveis
- Criar relatórios exportáveis (PDF, Excel)
- Implementar análises estatísticas mais avançadas (correlações, testes de hipóteses)
- Adicionar previsões usando machine learning

## Licença

Este projeto foi desenvolvido como parte da Imersão Alura e é destinado a fins educacionais.

## Contribuições

Este é um projeto educacional desenvolvido durante a Imersão Alura. Sinta-se à vontade para usar como referência e adaptar para suas próprias análises!

---

**Desenvolvido com ❤️ durante a Imersão Alura - Dados com Python**

