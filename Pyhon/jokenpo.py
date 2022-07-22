"""Jokenpô"""
from random import randint


def start():
    while True:
        print(" " * 40)
        print("J    O    K    E    N    P    Ô")
        print(' ' * 40)
        game_mode = int(input("Digite 1 para JOGADOR VS COMPUTADOR\n"
                              "Digite 2 para JOGADOR VS JOGADOR\n"
                              "Escolha o modo de jogo: "))
        if game_mode == 0:
            break
        if game_mode > 2 or game_mode < 0:
            print('\33[31m Invalido, coloque o numero certo \33[m')
        elif game_mode == 1:
            machine()
        else:
            player_vs_player()


def machine():
    computador_pontos = jogador_pontos = 0
    while True:
        game_list = ['Papel', 'Pedra', 'Tesoura']
        print('*' * 40)
        jogador = int(input("Escolha:\n 0 para Papel\n 1 para Pedra\n 2 para Tesoura: "))
        computador = randint(0, 2)
        if jogador > 2 or jogador < 0:
            print("\33[31m Seleção incorreta \33[m")
        elif jogador == computador:
            print(f"Você jogou: {game_list[jogador]} X Computador jogou: {game_list[computador]}")
            print("\33[32m JOGADA EMPATADA \33[m")
        else:
            print(f"Você jogou: {game_list[jogador]} X Computador jogou: {game_list[computador]}")
            print('-' * 40)
            if computador == 2 and jogador == 0:
                print("\33[33m Computador ganhou a rodada \33[m!")
                print(' ' * 40)
                computador_pontos += 1
            else:
                if computador == 0 and jogador == 1:
                    print("\33[33m Computador ganhou a rodada! \33[m")
                    print(' ' * 40)
                    computador_pontos += 1
                else:
                    if computador == 1 and jogador == 2:
                        print("\33[33m Computador ganhou a rodada! \33[m")
                        print(' ' * 40)
                    else:
                        print("\33[32m Você ganhou a rodada!! \33[m")
                        print(' ' * 40)
                        jogador_pontos += 1
            if jogador_pontos == 2:
                print("\33[32m ****VOCÊ GANHOU O JOKENPÔ**** \33[m")
                computador_pontos += 1
                break
            if computador_pontos == 2:
                print("\33[33m ****COMPUTADOR GANHOU O JOKENPÔ**** \33[m")
                break


def player_vs_player():
    jogador1_pontos = jogador2_pontos = 0
    while True:
        print('*' * 40)
        game_list = ['Papel', 'Pedra', 'Tesoura']

        jogador1 = int(input("Jogador 1:\n 0 para Papel\n 1 para Pedra\n 2 para Tesoura: "))
        if jogador1 > 2 or jogador1 < 0:
            print('\33[31m Jogada inválida! Tente novamente.\33[m')

        jogador2 = int(input("Jogador 2:\n 0 para Papel\n 1 para Pedra\n 2 para Tesoura:  "))
        if jogador2 > 2 or jogador2 < 0:
            print('\33[31m Jogada inválida! Tenta novamente.\33[m')

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
