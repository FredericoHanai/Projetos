"""Jokenpô"""
from random import randint


def start():
    print(" " * 40)
    print("J    O    K    E    N    P    Ô")
    print(' ' * 40)
    game_mode = int(input("Escolha o modo de jogo\nDigite 1 para JOGADOR VS COMPUTADOR\n"
                          "Digite 2 para JOGADOR VS JOGADOR"))
    if game_mode == 1:
        return machine()
    return player_vs_player()


def machine():
    computador_pontos = jogador_pontos = 0
    while True:
        game_list = ['Papel', 'Pedra', 'Tesoura']
        print('*' * 40)
        jogador = int(input("Escolha 0 -> Papel, 1 -> Pedra e 2 -> Tesoura: "))
        computador = randint(0, 2)
        if jogador > 2 or jogador < 0:
            print("Seleção incorreta")
        elif jogador == computador:
            print(f"Você jogou: {game_list[jogador]} X Computador jogou: {game_list[computador]}")
            print("JOGADA EMPATADA")
        else:
            print(f"Você jogou: {game_list[jogador]} X Computador jogou: {game_list[computador]}")
            print('-' * 40)
            if computador == 2 and jogador == 0:
                print("Computador ganhou a rodada!")
                print(' ' * 40)
                computador_pontos += 1
            else:
                if computador == 0 and jogador == 1:
                    print("Computador ganhou a rodada!")
                    print(' ' * 40)
                    computador_pontos += 1
                else:
                    if computador == 1 and jogador == 2:
                        print("Computador ganhou a rodada!")
                        print(' ' * 40)
                    else:
                        print("Você ganhou a rodada!!")
                        print(' ' * 40)
                        jogador_pontos += 1
            if jogador_pontos == 2:
                print("****VOCÊ GANHOU O JOKENPÔ****")
                computador_pontos += 1
                break
            if computador_pontos == 2:
                print("****COMPUTADOR GANHOU O JOKENPÔ****")
                break


def player_vs_player():
    jogador1_pontos = jogador2_pontos = 0
    while True:
        game_list = ['Papel', 'Pedra', 'Tesoura']
        print('*' * 40)
        jogador1 = int(input("Digite 0 -> Papel, 1 -> Pedra e 2 -> Tesoura: "))
        jogador2 = int(input("Digite 0 -> Papel, 1 -> Pedra e 2 -> Tesoura: "))
        if jogador1 > 2 or jogador1 < 0:
            print("Seleção incorreta")
        elif jogador1 == jogador2:
            print(f"Jogador 1 jogou: {game_list[jogador1]} X Jogador 2 jogou: {game_list[jogador2]}")
            print("JOGADA EMPATADA")
        else:
            print(f"Jogador 1 jogou: {game_list[jogador1]} X Jogador 2 jogou: {game_list[jogador2]}")
            print('-' * 40)
            if jogador2 == 2 and jogador1 == 0:
                print("Jogador 2 ganhou a rodada!")
                print(' ' * 40)
                jogador2_pontos += 1
            else:
                if jogador2 == 0 and jogador1 == 1:
                    print("Jogador 2 ganhou a rodada!")
                    print(' ' * 40)
                    jogador2_pontos += 1
                else:
                    if jogador2 == 1 and jogador1 == 2:
                        print("Jogador 2 ganhou a rodada!")
                        print(' ' * 40)
                        jogador2_pontos += 1
                    else:
                        print("Jogador 1 ganhou a rodada!!")
                        print(' ' * 40)
                        jogador1_pontos += 1
            if jogador2_pontos == 2:
                print("****JOGADOR 1 GANHOU O JOKENPÔ****")
                break
            if jogador1_pontos == 2:
                print("****JOGADOR 2 GANHOU O JOKENPÔ****")
                break


if __name__ == "__main__":
    start()
