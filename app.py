import streamlit as st
import pandas as pd
import plotly.express as px

#config da página
st.set_page_config(
    page_title="Dashboard de Salários na Área de Dados",
    page_icon="📶",
    layout="wide",
)

#carregando os dados já limpos
df = pd.read_csv("https://raw.githubusercontent.com/vqrca/dashboard_salarios_dados/refs/heads/main/dados-imersao-final.csv")
                 
#filtragem na barra lateral
st.sidebar.header("Filtros de Busca")

#na nossa dashboard irão aparecer como ícones a serem removidos por isso a diferença entre disponivel e selecionado

#filtro de ano
anos_disponiveis = sorted(df['ano'].unique())#unique pega os valores únicos da coluna ano e organiza com o sorted
anos_selecionados = st.sidebar.multiselect("Ano", anos_disponiveis, default=anos_disponiveis ) #multiselect a gente pode escolher os anos para o filtro

#filtro de senioridade
senioridades_disponiveis = sorted(df['senioridade'].unique())
senioridades_selecionadas = st.sidebar.multiselect("Senioridade", senioridades_disponiveis, default=senioridades_disponiveis)

#filtro do tipo de contrato
contratos_disponiveis = sorted(df['contrato'].unique())
contratos_selecionados = st.sidebar.multiselect("Tipo de Contrato", contratos_disponiveis, default=contratos_disponiveis)

#filtro do tamanho da empresa
tamanhos_disponiveis = sorted(df['tamanho_empresa'].unique())
tamanhos_selecionados = st.sidebar.multiselect("Tamanho da Empresa", tamanhos_disponiveis, default=tamanhos_disponiveis)

#filtragem do dataframe principal com base no que foi filtrado na sidebar que fizemos acima
df_filtrado = df[
    (df['ano'].isin(anos_selecionados))& #pega por exemplo os anos que o usuario selecionou e atualiza para aparecer na dashboard
    (df['senioridade'].isin(senioridades_selecionadas))&
    (df['contrato'].isin(contratos_selecionados))&
    (df['tamanho_empresa'].isin(tamanhos_selecionados))
]

#conteúdo principal da página
st.title("🎲 Dashboard de Análise de Salários na Área de Dados")
st.markdown("Explore os dados salariais na área de dados nos últimos anos. Utilize os filtros à esquerda para refinar sua análise.")#temos que deixar claro como o usuário deve utilizar a dashhboard

#métricas
st.subheader("Métricas gerais (Salário anual em USD)")

if not df_filtrado.empty:#pra garantir que o vazio apareça
    salario_medio = df_filtrado['usd'].mean()
    salario_maximo = df_filtrado['usd'].max()
    total_registros = df_filtrado.shape[0]
    cargo_mais_frequente = df_filtrado["cargo"].mode()[0]
else:
    salario_medio, salario_mediano, salario_maximo, total_registros, cargo_mais_comum = 0, 0, 0, ""

col1, col2, col3, col4 = st.columns(4) #podemos dividir nossa página em 4 colunas cada um representando uma info
col1.metric("Salário médio", f"${salario_medio:,.0f}")
col2.metric("Salário máximo", f"${salario_maximo:,.0f}")
col3.metric("Total de registros", f"{total_registros:,}")
col4.metric("Cargo mais frequente", cargo_mais_frequente)

st.markdown("---")

#análise visual dos gráficos com a biblioteca plotly

st.subheader("Gráficos")

col_graf1, col_graf2 = st.columns(2) #pra não ficar os 4 gráficos na mesma linha, vamos fazer em duas

with col_graf1:
    if not df_filtrado.empty:
        top_cargos = df_filtrado.groupby('cargo')['usd'].mean().nlargest(10).sort_values(ascending=True).reset_index() #agrupamento dos cargos com os 10 maiores salarios
        grafico_cargos = px.bar( #gráfico de barra
            top_cargos,
            x='usd',
            y='cargo',
            orientation='h', #horizontal
            title="Top 10 cargos por salário médio",
            labels={'usd': 'Média salarial anual (USD)', 'cargo': ''}
        )
        grafico_cargos.update_layout(title_x=0.1, yaxis={'categoryorder':'total ascending'}) #mover o título pra ficar bonito
        st.plotly_chart(grafico_cargos, use_container_width=True)#conseguir exibir o gráfico na dash
    else:
        st.warning("Nenhum dado para exibir no gráfico de cargos.")

with col_graf2:
    if not df_filtrado.empty:
        grafico_hist = px.histogram( #um historgrama com a distribuição dos salários
            df_filtrado,
            x='usd',
            nbins=30,
            title="Distribuição de salários anuais",
            labels={'usd': 'Faixa salarial (USD)', 'count': ''}
        )
        grafico_hist.update_layout(title_x=0.1)
        st.plotly_chart(grafico_hist, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir no gráfico de distribuição.")

col_graf3, col_graf4 = st.columns(2)

with col_graf3:
    if not df_filtrado.empty:
        remoto_contagem = df_filtrado['remoto'].value_counts().reset_index()
        remoto_contagem.columns = ['tipo_trabalho', 'quantidade']
        grafico_remoto = px.pie( #gráfico de pizza com os tipos de trabalho
            remoto_contagem,
            names='tipo_trabalho',
            values='quantidade',
            title='Proporção dos tipos de trabalho',
            hole=0.5
        )
        grafico_remoto.update_traces(textinfo='percent+label')
        grafico_remoto.update_layout(title_x=0.1)
        st.plotly_chart(grafico_remoto, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir no gráfico dos tipos de trabalho.")

with col_graf4:
    if not df_filtrado.empty:
        df_ds = df_filtrado[df_filtrado['cargo'] == 'Data Scientist']
        media_ds_pais = df_ds.groupby('residencia_iso3')['usd'].mean().reset_index()
        grafico_paises = px.choropleth(media_ds_pais,
            locations='residencia_iso3',
            color='usd',
            color_continuous_scale='rdylgn',
            title='Salário médio de Cientista de Dados por país',
            labels={'usd': 'Salário médio (USD)', 'residencia_iso3': 'País'})
        grafico_paises.update_layout(title_x=0.1)
        st.plotly_chart(grafico_paises, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir no gráfico de países.")

col_graf5, col_graf6 = st.columns(2)

with col_graf5:
    if not df_filtrado.empty:
        df_de = df_filtrado[df_filtrado['cargo'] == 'Data Engineer']
        media_de_pais = df_de.groupby('residencia_iso3')['usd'].mean().reset_index()

        grafico_paises = px.choropleth(
            media_de_pais,
            locations='residencia_iso3',
            color='usd',
            color_continuous_scale='rdylgn',
            title='Salário médio de Engenheiro de Dados por país',
            labels={'usd': 'Salário médio (USD)', 'residencia_iso3': 'País'}
        )

        grafico_paises.update_layout(title_x=0.1)
        st.plotly_chart(grafico_paises, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir no gráfico de países.")

with col_graf6:
    if not df_filtrado.empty:
        df_da = df_filtrado[df_filtrado['cargo'] == 'Data Analyst']
        media_da_pais = df_da.groupby('residencia_iso3')['usd'].mean().reset_index()

        grafico_paises = px.choropleth(
            media_da_pais,
            locations='residencia_iso3',
            color='usd',
            color_continuous_scale='rdylgn',
            title='Salário médio de Analista de Dados por país',
            labels={'usd': 'Salário médio (USD)', 'residencia_iso3': 'País'}
        )

        grafico_paises.update_layout(title_x=0.1)
        st.plotly_chart(grafico_paises, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir no gráfico de países.")

#dados detalhados
st.subheader("Dados Detalhados")
st.dataframe(df_filtrado)