### Requisitos

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
