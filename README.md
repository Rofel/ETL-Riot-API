# Dados da soloQ brasileira 
##  02/02/2024 - Dados referente a 3047 jogos criados.
#### O intuito do projeto é aprender a retirar os dados da soloQ através da API da RIOT Games, e após a extração, tratar os dados para armazenamento em um banco de dados mySQL para consulta e manipulação futura.

#### Para facilitar a apresentação, o projeto foi separado em 3 etapas: Extração de dados através da API da RIOT, Manipulação dos dados extraídos e Armazenamento dos dados finais no banco.
#### Cada etapa está associada a um notebook específico:
- #### [Extração](https://github.com/Rofel/ETL-Riot-API/blob/main/API%20data%20extracting.ipynb)
- #### [Manipulação](https://github.com/Rofel/ETL-Riot-API/blob/main/Manipulate%20JSON%20and%20prepare%20DF%20for%20DB%20insert.ipynb)
- #### [Armazenamento](https://github.com/Rofel/ETL-Riot-API/blob/main/Creating%20mySQL%20tables%20from%20csv.ipynb)

### Para realizar a extração é necessário ter uma conta de desenvolvedor da RIOT Games https://developer.riotgames.com/ e ter uma DEVELOPMENT API KEY 

![riotApiSite](https://github.com/Rofel/ETL-Riot-API/assets/13154589/abf3c506-e16a-4c98-bab2-cca83caefaa6)

#### O arquivo [methods.py](https://github.com/Rofel/ETL-Riot-API/blob/main/methods.py) contém todos os métodos utilizados para o projeto.

# Extração dos dados utilizando a API

#### A primeira parte do notebook é para apresentar os métodos de requisição da API. Como conseguir o Puuid a partir de um Summoner Name, a lista de matchs, e as informações de cada jogo. Tabém como conseguir as informações de filas específicas, como challenger, grandmaster, master, diamond, etc.

#### A segunda parte é a extração de partidas dos 20 primeiro jogadores da soloQ brasileira. Para isso são executados os seguintes passos:
-  Utilizando a função get_challengers_solo(), extrair os jogadores challengers da soloQ
-  Armazenar o 'summoner name' dos 20 jogadores com mais pontos em uma lista
-  A partir dessa lista, encontrar o puuid para cada jogador com a função ge_puuid(), com isso extrair o matchid dos últimos 20 jogos de cada jogador com a função get_ranked_matches()
-  Com a utilização do método ge_ranked_matches() teremos apenas jogos da soloQ.
-  Filtrar a lista de jogos, para retirar partidas repetidas com base no matchId, tendo uma lista de partidas únicas.
-  Começar a requisição dos dados das partidas únicas jogadas. Armazenando todas partidas em uma lista de match_info.
-  Por fim, exportar essa lista em um arquivo formato JSON.

#### Para uma base de dados mais robusta, mais jogadores e mais jogos são necessários. para usar como exemplo e agilizar o processo de extração, utilizei apenas os 20 primeiros jogadores. Criando assim um [challenger_matchs.json](https://github.com/Rofel/ETL-Riot-API/blob/main/challenger_matchs.json) com os dados das partidas.

# Manipulação dos dados
### OBS: As tabelas: Perks, Challenges, e Pings não foram implementadas até o momento.
#### Nessa etapa com os dados das partidas armazenado foram criados Dataframes específicos para armazenar os dados relevantes. Cada DF criado representa uma tabela diferente no modelo mySQL que será criado. 
#### A escolha das tabelas foi feita com base na análise do formato dos dados apresentados e está exposta [aqui](https://github.com/Rofel/ETL-Riot-API/blob/main/Tables%20for%20SQL%20DB.pdf)

#### Para concluir essa etapa foram executados os seguintes passos:
- Criação dos dataframes com base na lista de cada tabela
- Processamento dos dados já extraídos anteriormente para serem inseridos em seus respectivos dfs.
- Através de uma lista de dados estruturados de forma condizente com o modelo desejado, inserção dos dados nas tabelas desejadas.
- As tabelas criadas foram: 'player_stats', 'teams', 'bans', 'players' e 'matchs'
- Por fim cada tabela é exportada como um arquivo .csv de mesmo nome.
- Esses arquivos estão disponível dentro desse projeto.


# Criação do banco mySQL
#### A partir de um banco de dados criado em mySQL é feita uma conexão em python para a inserção das tabelas através do notebook com a biblioteca sqlalchemy
#### Os dados pessoais estão inseridos dentro de um arquivo .env para proteção. 

![mySQLleagueoflegendsdb](https://github.com/Rofel/ETL-Riot-API/assets/13154589/cd3a0bc2-26fb-4f85-8e08-61acc714b3a5)

#### Essa etapa é mais curta e consiste em:
- Criar uma conexão com a base de dados do banco mySQL
- Criar uma lista com os nomes das tabelas a serem criadas
- Importar os arquivos .csv criados para um dataframe
- Utilizando a função df.to_sql() criar a tabela no banco

## Select da tabela player_stats
![tables_mySQLleagueapi](https://github.com/Rofel/ETL-Riot-API/assets/13154589/93dc29fc-7235-4147-9b23-8d073cf15af2)


