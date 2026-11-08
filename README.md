# Simulador de Projeção Patrimonial & Juros Compostos

Aplicação web deselvida em **Python** e **Streamlit** para simulação interativa de crescimento patrimonial a longo prazo, considerando aportes recorrentes,juros compostos e o efeito da inflaçao (IPCA) sobre o poder de compra real.

---

## Live Demo
    **[Acesse a Aplicação Online no Streamlit Community Cloud](link)**

---

## Demonstração Visual

(fotos)

> * As imagens a cima ilustram a reatividade imediata dos gráficos e métricas conforme os parâmetros na barra lateral são ajustados.*

---

## Arquitetura do Código

O projeto segue o princío de **Separação de Responsabilidades (SoC)**:
* **'calculos.py'**: Módulo encapsulado com a inteligência e lógica matemática das projeções (taxa de Fisher, equivalência de juros composto mensais e deflecionamento patrimonial).
* **'app.py'**: Interace com o usuáriocriada em Streamlit, responsável por capturar inputs, invocar o motor de cálculo e renderizar métricas e gráficos dinâmicos com Plotly.

---

