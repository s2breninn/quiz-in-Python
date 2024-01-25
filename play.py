import json
import os

pts = 0
count_q = 0
rodada = 1
letters = ['a', 'b', 'c', 'd']
player_res_list = []
computer_res_list = []
player_dict = {}
new_round = {}

print('=============================')
print('Bem-vindo o jogo do quiz')
def main_print(pts, rodada):
    print('=============================')
    print(f'\nPontos: {pts}')
    print((f'Rodada: {rodada}'))
    print('Escolha se quer jogar ou não')
    print('0 - SIM | 1 - NÃO')

# Validação de entrada (0 ou 1)
def validation_in():
    while True:
        try:
            player_move = int(input())
            if player_move not in [0, 1]:
                raise ValueError('Erro inválido. Insira 0 ou 1')
            return player_move
        except Exception as e:
            print(f'Error: {e}')

# Validação de entrada para letra (a, b, c ou d)
def validation_letters():
    while True:
        try:
            player_response = input('Resposta: ')
            if player_response not in letters:
                raise ValueError('Entrada inválida! Insira a, b, c ou d')
            player_res_list.append(player_response)
            return player_response
        except Exception as e:
            print(f'Error: {e}')

#Visualização de questões, alternativas e respostas em JSON -> Dicionário em Py
def view_json():
    with open('questions.json') as file:
        data = json.load(file)
    return data

#Visualização de informações do jogador
def view_json_players():
    with open('players.json') as file:
        data_players = json.load(file)
    return data_players

# Startando o jogo
def play_quiz(player_move, data, letters):
    if player_move == 0:
        nome = input("Nome: ")
        for num_q, question in enumerate(data, start=1):
            show_question(num_q, question, letters)
        return nome
    elif player_move == 1:
        os.system('exit')
    else:
        ...

# Mostrar questões
def show_question(num_q, question, letters):
    print(f"\n{num_q}) {question['pergunta']}")
    for i, option in enumerate(question["opcoes"][:len(letters)], start=0):
        print(f"{letters[i]}) {option}")
    validation_letters()

# Checagem de resposta
def check_pts_res(pts, data, computer_res_list, player_res_list):
    # Iterando sobre cada pergunta
    for question in data:
        for i, (option, letter) in enumerate(zip(question['opcoes'], letters)):
            if question['resposta'] == option:
                computer_res_list.append(letter)
    # Comparando as listas e somando a pontuação
    for player_res_list, computer_res_list in zip(player_res_list, computer_res_list):
        if player_res_list == computer_res_list:
            pts += 10
    return pts

# Capturar informações sobre o jogador
def captura_info_player(data_players, nome, player_res_list, computer_res_list, pts, player_dict):
    new_round = {}

    # Armazenando dados da rodada
    new_round['rodada'] = rodada
    new_round['resposta_jogador'] = player_res_list
    new_round['resposta_computador'] = computer_res_list
    new_round['pontos'] = pts

    player_exists = False
    for player in data_players:
        if player['nome'] == nome:
            print('Já existe um jogador com esse nome.')
            player['rodadas'].append(new_round)
            player_exists = True
            break
    if not player_exists:
        print('Adicionando novo jogador.')
        new_player = {
            'nome': nome,
            'rodadas': [new_round]
        }
    data_players.append(new_player)

    for player in data_players:
        print(f'\n{player["nome"]}\nRodadas: {player["rodadas"]}')

    with open('players.json', 'w') as file:
        json.dump(data_players, file, indent=2)

again = 1
while again == 1:
    main_print(pts, rodada)
    player_move = validation_in()
    data = view_json()
    nome = play_quiz(player_move, data, letters)
    pts = check_pts_res(pts, data, computer_res_list, player_res_list)
    # Capturando dados do arquivo JSON
    data_players = view_json_players()
    # Capturando dados da jogada do jogador
    captura_info_player(data_players, nome, player_res_list, computer_res_list, pts, player_dict)

    print('\n==================')
    print(f'PLACAR: {pts} pontos')
    print('==================')

    while True:
        print('\nJogar novamente? 0 - SIM | 1 - NÃO')
        next = int(input())
        if next == 0:
            rodada += 1
            break
        elif next == 1:
            again = 0
            os.system('exit')
            break
    os.system('clear')