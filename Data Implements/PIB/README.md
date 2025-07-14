# Projeto prático: Extração e processamento de dados do PIB
- **Objetivo:** Colocar em prática as habilidades adquiridas durante o curso *Python para Cientista de dados, IA e desenvolvedor*.
- **Tarefa:** extrair dados de um site usando webscraping e solicitar APIs para processá-los usando as bibliotecas Pandas e Numpy 

## Cenário do projeto
  Uma empresa internacional que deseja expandir seus negócios em diferentes países do mundo o recrutou.
  Você foi contratado como engenheiro de dados júnior e tem a tarefa de criar um script que possa extrair a lista das 10 maiores economias do mundo em ordem decrescente de seus PIBs em bilhões de dólares (arredondados para 2 casas decimais), conforme registrado pelo Fundo Monetário Internacional (FMI).
  Os dados necessários parecem estar disponíveis no URL mencionado abaixo: <br>
  URL: https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29e <br><br>
**Objetivos** <br>
  Ser capaz de:
  - Usar webscraping para extrair informações necessárias de um site
  - Use os pandas para carregar e processar os dados tabulares como um quadro de dados.
  - Use Numpy para manipular as informações contidas no quadro de dados.
  - Carregue o quadro de dados atualizado no arquivo CSV.

## Configurações
Para este laboratório, será necessário o uso das seguintes bibliotecas:
- Pandas: para gerenciar os dados
- NumPy: para operações matemáticas

`pip install pandas numpy` <br>
`pip install lxml # Analisador suportado pela biblioteca BeautifullSoup`
<br>

## Exercícios
### 1) Extraia os dados do PIB necessários da URL fornecida usando a raspagem da Web.
URL="https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29" <br>
  a) Extrair tabelas da página da web usando pandas. Retire a tabela número 3 como o DataFrame necessário.
  
  b) Substitua os cabeçalhos da coluna por números de coluna
  
  c) Retire colunas com índice 0 e 2 (nome do país e valor do PIB citado pelo FMI)
  
  d) Mantenha as linhas com o índice 1 a 10, indicando as 10 principais economias do mundo.
  
  e)  Atribua nomes de colunas como "país" e "PIB (milhões de dólares)"

### 2) Modifique a coluna do PIB do DataFrame, convertendo o valor disponível em milhões de dólares em bilhões de dólares. Use o método Round () da Biblioteca Numpy para arredondar o valor para 2 locais decimais. Modifique o cabeçalho do DataFrame para o PIB (bilhão de dólares).
  a) Altere o tipo de dados da coluna 'GDP (Million USD)' para inteiro.
  Use o método astype ().

  b) Converta o valor de GDP (Million USD) em bilhões de dólares

  c) Use o método Numpy.Round () para arredondar o valor para 2 decimais.

  d) Renomeie o cabeçalho da coluna de 'PIB (milhões de dólares)' para 'PIB (bilhão de dólares)'
