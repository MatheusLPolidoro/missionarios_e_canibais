from lib.interface import *
from lib.logica import *
from time import sleep


while True:
    opcao = menu(['Iniciar partida', 'Regras do jogo', 'Score de jogos', 'Sair do jogo'], 
                    tamanho=40,
                    titulo='MISSIONARIOS E CANIBAIS',
                    textoRodape='CreateBy:MatheusLPolidoro',
                    cor='amarelo',
                )
    if opcao == 1:
        animacao('Iniciando Partida ', ['\\', '|', '/', '_'], 20)
        game()
    elif opcao == 2:
        regras()
    elif opcao == 3:
        input('Score de jogos')
    elif opcao == 4:
        verde()
        print(f'\r{"Saindo...":^80}', end='')
        sleep(2)
        break
