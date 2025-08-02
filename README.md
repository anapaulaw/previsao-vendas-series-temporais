
# 📈 Previsão de Vendas com Séries Temporais

Projeto de ciência de dados com foco em previsão de vendas utilizando séries temporais. As etapas envolvem extração de dados de vendas, estruturação em banco relacional, análise exploratória, modelagem com SARIMA e machine learning, e visualizações interativas.

## 🗂️ Etapas

1. **Extração e Estruturação**: Leitura do CSV original, separação de tabelas (clientes, produtos, pedidos), criação de banco SQLite e unificação dos dados.
2. **Análise Exploratória**: Visualizações temporais, sazonalidade e análise de desempenho.
3. **Modelagem Preditiva**: Aplicação de modelos estatísticos (SARIMA, SARIMAX) e machine learning (XGBoost).
4. **Visualização e Métricas**: Comparação entre modelos com gráficos e métricas como RMSE e MAE.

## 📁 Estrutura de Pastas

- `data/`: arquivos `.csv` dos dados brutos e processados.
- `database/`: banco SQLite contendo as tabelas relacionais.
- `notebooks/`: notebooks Jupyter com cada etapa do projeto.
