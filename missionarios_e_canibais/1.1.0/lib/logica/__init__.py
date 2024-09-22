from lib.logica.logicaGame import *

def game():
    perdeu = venceu = False
    lados = ('d', 'e')
    plataformas = {
                    'eM': 0,  # ESQUERDA: MISSIONARIOS
                    'M': 0,   # CANOA:    MISSIONARIOS
                    'dM': 3,  # DIREITA:  MISSIONARIOS
                    'eC': 0,  # ESQUERDA: CANIBAIS
                    'C': 0,   # CANOA:    CANIBAIS
                    'dC': 3   # DIREITA:  CANIBAIS
                }
    while not perdeu and not venceu:
        for lado in lados:
            if not perdeu and not venceu:
                sobePassageiro(lado, plataformas) 
                descePassageiro(lado, plataformas)
                perdeu = derrota(plataformas)
                venceu = vitoria(plataformas)
            else:
                break
    fim(plataformas)


def regras():
    retLinha(8)
    card(12, 0,
        texto=[''], 
        corInfo='\033[1;36m',
        tamanho=55, 
        pulaLinha=0,
        alinhamento='<',
        info=[
            ['► OBJETIVO: Atravessar todos os MISSIONÁRIOS e CANIBAIS.'],
            ['1. Não é possível atravessar com a canoa vazia.'],
            ['2. Só dois passageiros cabem na canoa.'],
            ['3. Não pode deixar MISSIONÁRIOS com mais CANIBAIS.'],
            [' ' * 90]
        ]
    )
    input()
