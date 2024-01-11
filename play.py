import json

pts = 0
letters = ['a', 'b', 'c', 'd']
response_list = []

print('=============================')
print('Bem-vindo o jogo do QUIZ')
def main_print(pts):
    print('=============================')
    print(f'\nPontos: {pts}')
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
            response_list.append(player_response)
            return player_response
        except Exception as e:
            print(f'Error: {e}')

def view_json():
    with open('questions.json') as file:
        data = json.load(file)

    return data

def play_quiz(player_move, data, letters):
    if player_move == 0:
        for num_q, question in enumerate(data, start=1):
            show_question(num_q, question, letters)
    else:
        ...

def show_question(num_q, question, letters):
    print(f"\n{num_q}) {question['pergunta']}")
    for i, option in enumerate(question["opcoes"][:len(letters)], start=0):
        print(f"{letters[i]}) {option}")
    validation_letters()
    print(response_list)

def check_res():
    ...

again = 1
while again == 1:
    main_print(pts)
    player_move = validation_in()
    data = view_JSON()
    play_quiz = play_quiz(player_move, data, letters)
