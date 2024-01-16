import json
import os

pts = 0
count_q = 0
rodada = 1
letters = ['a', 'b', 'c', 'd']
player_res_list = []
computer_res_list = []

print('=============================')
print('Bem-vindo o jogo do quiz')
def main_print(pts, rodada):
    print('=============================')
    print(f'\nPontos: {pts}')
    print((f'Rodada: {rodada}'))
    print('Escolha se quer jogar ou não')
    print('0 - SIM | 1 - NÃO')

def validation_in():
    while True:
        try:
            player_move = int(input())
            if player_move not in [0, 1]:
                raise ValueError('Erro inválido. Insira 0 ou 1')
            return player_move
        except Exception as e:
            print(f'Error: {e}')

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

def capturar_info_player():
    nome = input('Nome: ')

def view_json():
    with open('questions.json') as file:
        data = json.load(file)
    return data

def play_quiz(player_move, data, letters):
    if player_move == 0:
        for num_q, question in enumerate(data, start=1):
            show_question(num_q, question, letters)
    elif player_move == 1:
        os.system('exit')
    else:
        ...

def show_question(num_q, question, letters):
    print(f"\n{num_q}) {question['pergunta']}")
    for i, option in enumerate(question["opcoes"][:len(letters)], start=0):
        print(f"{letters[i]}) {option}")
    validation_letters()

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

again = 1
while again == 1:
    main_print(pts, rodada)
    player_move = validation_in()
    data = view_json()
    play_quiz(player_move, data, letters)
    pts = check_pts_res(pts, data, computer_res_list, player_res_list)

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
            break
    os.system('clear')