### Requisitos

<<<<<<< HEAD
#### 1. Salvar dados dos jogadoeres e suas rodadas  
  1.1 Armazenar uma lista de dicionário chamado "players" onde terá dados de todos jogadores   
  
    Requisito: Salvar em arquivo JSON  

#### 2. Exibir painel de recordes
  Descrição: Capturar todos os dados salvos no arquivo JSON pegar as pontuações totais de cada jogador
  e inserir ela para exibição no painel de pontuação. 
   
         +---------------------------------+  
         |         PAINEL DE PLACARES       |  
         +----------------------------------+  

         1° LUGAR  
         Nome: Mister Bin  
         Pontuação: 40 pontos  

         2° LUGAR  
         Nome: Platonico  
         Pontuação: 50 pontos  

----

### Visualização de dados

##### Questões
    questions = [
        {
            "pergunta": "Quem foi o primeiro homem a pisar na Lua?",
            "opcoes": ["Neil Armstrong", "Buzz Aldrin", "Yuri Gagarin", "Alan Shepard"],
            "resposta": "Neil Armstrong"
        },
        ...
    ]

##### Info jogadores
    players = [
        {
            "nome": "Mister Bin",
            "rodadas": [
                {
                    "rodada" 1,
                    "player_res_list": ["a", "b", "c", "c", "a", "d", "a"...],
                    "computer_res_list": ["a", "a", "a", "c", "a", "b", "c"...],
                    "pts": 40
                },
                {
                    "rodada" 2,
                    "player_res_list": ["a", "b", "c", "c", "a", "d", "a"...],
                    "computer_res_list": ["a", "a", "a", "c", "a", "b", "c"...],
                    "pts": 20
                },
                ...
            ]
            "pts_totais": 60
            "recorde_rodada": 40
        }
    ]
=======
1. Salvar dados dos jogadoeres e suas rodadas
  1.1 Armazenar uma lista de dicionário chamado "players" onde terá dados de todos jogadores
      ex.:  players = [  
              {  
                "id": 1,                        - Código de identificação do jogador  
                "nome": Breno Mendes,           - Nome do jogador  
                "rodadas": 5,                   - Quantidade de rodadas que ele jogou  
                "pts_total": 30                 - Pontos totais de todas rodadas somadas  
                "pts_recorde_rodada": 8         - Mais pontuação em uma única rodada   
              },  
            ]    

    Requisito: Salvar em arquivo JSON

2. Exibir painel de recordes
  Descrição: Capturar todos os dados salvos no arquivo JSON pegar as pontuações totais de cada jogador
  e inserir ela para exibição no painel de pontuação.  
  ex.: +---------------------------------+  
      |         PAINEL DE PLACARES       |  
      +----------------------------------+  

      1° LUGAR  
        Nome: Breno Mendes  
        Pontuação: 45 pontos  

      2° LUGAR  
        Nome: Vitoria Oliveira  
        Pontuação: 44 pontos  
>>>>>>> origin/master
