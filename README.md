O principal objetivo desse projeto é construir um pipeline completo de previsão de vendas, partindo de dados transacionais brutos até um modelo confiável, versionado e com deploy em Streamlit. Para isso foi criado tuda a estrutura essencial para construção dessa pipeline desde a quaidade dos dados passo muito importante e que norteia todo e qualquer projeto de data science , abordaremos conceitos de analise de dados, engenharia de dados e por fim ciência de dados.

O nosso Target principal (forecast) será a receita diária (SalesAmount) e o target secundário a quantidade vendida (OrderQuantity) pois a receita é o KPI mais relevante para negócio
e a quantidade ajuda a interpretar variações ,explicar picos e validar comportamento do modelo.


____________________________________________________________________________________________________________________________________
ETAPAS DO PROJETO:

Passo 1 — Auditoria  dos dados brutos

*  Existem duplicidades?
*  A frequência temporal é regular?
*  Existem buracos na série?
*  Existem valores anômalos?
*  Os dados são transacionais ou já agregados?
*  Verificar qual é a granularidade máxima possível 
*  Definição da série temporal correta
*  Série diária 
*  Definir Métricas corretas (receita e quantidade vendida)
*  Reconstrução da base final com frequência definida sem duplicatas
*  Pronta para análise de dados etapa seguinte onde foi feita uma analise


Passo 2 — EDA

*  Análise temporal da receita, quantidade vendida e ticket médio
*  Comparação entre granularidade diária e mensal
*  Identificação de tendência, sazonalidade e volatilidade
*  Decomposição clássica e STL
*  nálise de autocorrelação (ACF/PACF)
*  Compreender **tendência**
*  Identificar **sazonalidades**
*  Avaliar **estacionariedade**
*  Definir **insumos corretos para modelagem**
*  Criar **baselines simples** para comparação futura



ETAPA 3 - ENGENHARIA DE DADOS

Preparar a base de dados diária para modelagem:

*  Criação de variáveis dummies sazonais
*  Verificando sazonalidade semanal e anual
*  analiisando dependência temporal (lags)
*  Criação de lags da variável alvo
*  Criação de lags da quantidade (variável explicativa)
*  Efeitos de calendário
*  Dinâmica recente das vendas (rolling features)
*  Definindo target principal (receita_diaria) e target secundário (qtd_diaria)
*  Transformação da série  em log
*  Variáveis exógenas de calendário
*  Avaliação fora da amostra



ETAPA 4 - MODELAGEM

*  Definição dos parâmetros 
*  Avaliação fora da amostra
*  diagnóstico de resíduos
*  Baseline Naive
*  Variáveis exógenas
*  Definição do modelo SARIMAX
*  Ajuste do modelo
*  Diagnóstico dos resíduos
*  Previsão no espaço log
*  Avaliação do modelo
*  Comparação com baseline




__________________________________________________________________________________________________________________________________

DADOS

*  Base bruta: FactInternetSales_2011_2013.csv
Tipo: dados transacionais

*  Base filtrada : vendas_diarias.csv
Tipo: filtrada sem duplicidade

*  Base final : train_model.csv / test_model.csv
Tipo: tratada para modelagem

____________________________________________________________________________________________________________________________________

## Para visualizar a aplicação em Produção

**Acesse o app interativo (Streamlit):**  
https://SEU-LINK-DO-STREAMLIT.streamlit.app

No aplicativo é possível:
- Selecionar o horizonte de previsão
- Visualizar intervalos de confiança
- Analisar previsões futuras com variáveis exógenas


## Metodologia

###  Modelo
- SARIMAX (Seasonal ARIMA com variáveis exogenas)
- Ordem: *(exemplo)* `SARIMA(2,1,1)(0,1,0,7)`
- Frequência: diária

### Variáveis Exógenas
- Fim de semana
- Mês
- Dia da semana
- Dummies sazonais 

As exógenas futuras são tratadas automaticamente no deploy.



__________________________________________________________________________________________________________________________________
Ana Paula Vanderley

*  Cientista de Dados | Analista de Dados Pleno
*  Foco em séries temporais, previsão de vendas e modelagem estatística aplicada a negócios.
* LinkedIn  https://www.linkedin.com/in/apvanderley/
