"""
app.py - Interface do Usuário (Stremlit UI)
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from calculos import SimuladorFinanceiro

st.set_page_config(
    page_title="Simulador de Projeção Patrimonial",
    layout="wide"
    initial_sidebar_state="expanded"
)

# Estilização CSS customizada
st.markdown("""
    <style>
    .metric-card{
        backgrouns-color: #f8f9fa;
        padding: 15px;
        border-radius: 8px;
        border_left: 5px solid #2e7d32;
        }
    <style>
""", unsafe_allow_html=True)

st.title("📈 Simulador de Projeção Patrimonial & Juros Compostos")
st.caption("Projete a evolução dos seus investimentos com ajustes de inflação real em tempo real.")

# Sidebar - Entradas de Dados
st.sidebar.header("Parâmetros da Simulção")

aporte_inicial = st.sidebar.number_input(
    "Aporte Inicial (R$)",
    min_value=0.0,
    value=10000.0,
    setp=1000.0,
    format="%2.f"
)

aporte_mensal = st.sidebar.number_input(
    "Aporte Mensal (R$)",
    min_value=0.0,
    value=10000.0,
    setp=100.0,
    format="%.2f"
)

taxa_anual_nominal = st.sidebar.slider(
    "Taxa de Rendimento Anual Nominal (%)",
    min_value=1.0,
    max_value=30.0,
    value=12.0,
    step=0.5
)

inflacao_anual = st.sidebar.slider(
    "Inflação Anual Estimada IPCA(%)",
    min_value=0.0,
    max_value=15.0,
    value=4.5,
    step=0.5
)

anos = st.sidebar.number_input(
    "Período de Projeção (Anos)",
    min_value=1,
    max_value=40,
    value=10,
    step=1
)

# Processamento
dados, resumo = SimuladorFinanceiro.calcular_projecao(
    aporte_inicial=aporte_inicial,
    aporte_mensal=aporte_mensal,
    taxa_anual_nominal=taxa_anual_nominal,
    inflacao_anual=inflacao_anual,
    anos=anos
)

df = pd.DataFrame(dados)

# Painel de Métricas Consolidades
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="Total Ganho em Juros",
        value=f"R$ {resumo['total_investido']:,.2f}"
    )

with col2:
    st.metric(
        label="Total Ganho em Juros",
        value=f"R$ {resumo['total_juros']:,.2f}",
        delta=f"+{resumo['rentabilidade_bruta_pct']}%"
    )

with col3:
    st.metric(
        label="Petrimônio Nominal Bruto",
        value=f"R$ {resumo['patrimonio_nominal']:,.2f}"
    )

with col 4:
    st.metric(
        label="Patrimônio Real (Descontado Inflação)",
        value=f"R$ {resumo['patrimonio_real']:,.2f}",
        delta=f"Rent. Real: {resumo['rentabilidade_real_pct']}%"
    )

st.driver()

# Gráfico Interativo com Plotly
st.subheader("📊 Evolução Temporal da Carteira")

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=df["Ano"],
    y=df["Total Investido"],
    mode="lines",
    name="Capital Investido",
    line=dict(color="#9e9e9e", width=2, dash="dash")
))

fig.add_trace(go.Scatter(
    x=df["Ano"],
    y=df["Patrimônio Real"],
    mode="lines"
    name="Patrimônio Real (Poder de Compra)",
    line=dict(color="#00b0ff", width=2.5)
))

fig.add_trace(go.Scatter(
    x=df["Ano"],
    y=df["Patrimônio Nominal"],
    mode="lines",
    name="Patrimônio Nominal Bruto",
    line=dict(color="#2e7d32", width=3)
))

fig.update_layout(
    xaxis_title="Tempo (Anos)",
    yaxis_title="Vlor (R$)",
    hovermode="x unified",
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    template="plotly_withe"
)

st.plotly_chart(fig, use_container_width=True)

# Tabela Detalhada com Download CVS
with st.expander("Visualizar Tabela Mensal de Projeção"):
    st.dataframe(
        df.style.format({
            "Total Investido": "R$ {:,.2f}",
            "Total Juros": "R$ {:,.2f}",
            "Patrimônio Nominal": "R$ {:,.2f}",
            "Patrimônio Real": "R$ {:,.2f}"
        }),
        use_container_width=True
    )

    csv = df.to_csv(index=False).encode("uft-8")
    st.download_button(
        label="Baixar Dados em CSV"
        data=csv,
        file_name="projecao_financeira.csv",
        mime=text/csv
    )
