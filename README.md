Este projeto tem como objetivo prever o volume mensal de vendas a partir de dados históricos utilizando modelos estatísticos de séries temporais.
A abordagem combina técnicas clássicas de modelagem (SARIMA e SARIMAX) com transformações matemáticas (logarítmica) para estabilizar a variância e melhorar a precisão das previsões.

O estudo inclui análise exploratória, testes de estacionariedade, decomposição da série temporal e avaliação comparativa entre modelos, demonstrando a importância da transformação logarítmica na previsão de séries com tendência e sazonalidade.
______________________________________________________________________________________________________________________________________
1 - Objetivos

Analisar a série temporal de vendas e suas tendências sazonais e cíclicas.

Avaliar a estacionariedade da série com o teste ADF (Dickey-Fuller Aumentado).

Aplicar e comparar modelos SARIMA com e sem transformação logarítmica.

Calcular métricas de desempenho como RMSE e MAE.

Visualizar e interpretar as previsões em relação aos valores observados.

____________________________________________________________________________________________________________________________________
2 - Tecnologias Utilizadas

Python 3.10+

Pandas e NumPy → manipulação e transformação dos dados

Matplotlib e Seaborn → análise visual da série temporal

Statsmodels → modelagem SARIMA/SARIMAX e testes estatísticos

Scikit-learn → métricas de erro (RMSE, MAE)

Pmdarima → automação de parâmetros ARIMA

Jupyter Notebook → documentação e execução interativa
___________________________________________________________________________________________________________________________________
3 - Metodologia (Modelagem Estatística)
3.1 - Coleta e Tratamento de Dados

Leitura do dataset VendasMensais.csv.

Conversão da coluna de datas (Period) para o formato datetime.

Ordenação e limpeza de dados ausentes.

Limitação da série até o ano de 2020 para treinamento.

3.2 - Análise Exploratória

Visualização da série temporal e suas variações.

Decomposição em componentes tendência, sazonalidade e ruído com seasonal_decompose.

3.3 - Testes Estatísticos

Aplicação do Teste de Dickey-Fuller Aumentado (ADF) para verificar a estacionariedade da série.

Avaliação da necessidade de diferenciação para estabilizar a média.

3.4 - Modelagem e Previsão

Ajuste de modelos SARIMA(p,d,q)(P,D,Q,m).

Inclusão de variáveis exógenas simples (como mês, feriados e eventos comerciais) no SARIMAX.

Comparação entre modelos com e sem transformação logarítmica da variável de vendas.

3.5 - Avaliação de Desempenho

Cálculo de MAE (Erro Absoluto Médio) e RMSE (Raiz do Erro Quadrático Médio).

Comparação entre previsões reais e estimadas.

Gráficos de valores previstos vs. observados para avaliar a aderência.
__________________________________________________________________________________________________________________________________
4 - Resultados e Conclusões

A transformação logarítmica se mostrou eficaz para reduzir a variância e melhorar a estabilidade do modelo.

O modelo SARIMA com log-transformação apresentou menor RMSE e MAE em comparação ao modelo sem transformação.

A previsão apresentou boa aderência visual e estatística, capturando bem as flutuações sazonais.

Os resultados reforçam a importância de testar transformações matemáticas e variáveis exógenas simples para melhorar a acurácia em previsões de vendas.

____________________________________________________________________________________________________________________________________
Ana Paula Vanderley
*  Cientista de Dados | Analista de Dados Pleno
*  Foco em séries temporais, previsão de vendas e modelagem estatística aplicada a negócios.
* LinkedIn  https://www.linkedin.com/in/apvanderley/
