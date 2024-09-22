from lib.interface import *
from time import sleep


nome = {
    'C': ' CANIBAL',
    'M': ' MISSIONÁRIO',
    'C2': ' CANIBAIS ',
    'M2': ' MISSIONÁRIOS '
}

passageiro = {'C': 'M', 'M': 'C'}


def frame(lado, plataformas, esquerda=6, direita=6):
    missionarioKey = ('eM', 'M', 'dM')
    canibalKey = ('eC', 'C', 'dC')
    missionario = ['Missionarios ' + str(plataformas[k]) for k in missionarioKey]
    canibal = ['canibais ' + str(plataformas[k]) for k in canibalKey]
    di = es = 1
    d = direita
    e = esquerda
    while True:
        sleep(.05)
        retLinha(8)
        es = e
        di = d
        card(4, es, di, 4,
                texto=['Esquerda', 'Canoa', 'Direita'], 
                corTitulo='\033[48;5;130m',
                corInfo='\033[0;94;103m',
                tamanho=20, 
                info=[missionario, canibal], 
            )
        print('\n')
        if lado == 'd' and e < 11:
            e += 1
            d -= 1
        elif lado == 'e' and d < 11:
            d += 1
            e -= 1
        else:
            break
        

def entradaNum(msg):
    return leiaInt(msg, [0, 1], comeca=0, cor='azul')


def canoaParada(lado):
    if lado == 'd':
        return (11, 1)
    elif lado == 'e':
        return (1, 11)

def sobePassageiro(lado, plataformas):
    while True:
        if not vitoria(plataformas):
            if plataformas['C'] + plataformas['M'] < 2 and plataformas[
                    lado + 'C'] + plataformas[lado + 'M'] > 0:
                margem = canoaParada(lado)
                frame(lado, plataformas, esquerda=margem[0], direita=margem[1])
                pas = leiaTexto(
                    " ► 'C' para PEGAR Canibais, 'M' Missionários, 'N' Nenhum: ",
                    ['M', 'C', 'N'])

                if pas in plataformas:
                    while plataformas[lado + pas] < 1:
                        pas = leiaTexto(
                            " ► 'C' para PEGAR (Canibais), 'M' (Missionários): ",
                            ['M', 'C'])

                    if pas in plataformas and plataformas[lado + pas] > 0:
                        num = entradaNum(
                            ' ►Quantidade de' + nome[pas + '2'] +
                            'que você quer COLOCAR na canoa:')

                        while plataformas[lado +
                                pas] < num or num < 0 or num > 2 or num + plataformas[
                                    'C'] + plataformas['M'] > 2:
                            num = entradaNum(
                                ' ►Quantidade de' + nome[pas + '2'] +
                                'que você quer COLOCAR na canoa:')
                        plataformas[pas] = plataformas[pas] + num
                        plataformas[lado + pas] = plataformas[lado + pas] - num

                        if plataformas[lado + 'C'] + plataformas[
                                lado +
                                'M'] > 0 and plataformas['C'] + plataformas[
                                    'M'] < 2 and plataformas[lado +
                                                             passageiro[pas]] != 0:
                            msg = ' ►Ainda tem um espaço na canoa. Quer COLOCAR um' + nome[
                                passageiro[pas]] + '? [S/N]:'
                            msg = leiaTexto(msg, ['S', 'N'])
                            if msg == 'S':
                                plataformas[
                                    passageiro[pas]] = plataformas[passageiro[pas]] + 1
                                plataformas[lado + passageiro[pas]] = plataformas[
                                    lado + passageiro[pas]] - 1

            if plataformas['C'] + plataformas['M'] > 0:
                break




def descePassageiro(lado, plataformas):
    lado = 'e' if lado == 'd' else 'd'
    frame(lado, plataformas)
    ladoTexto = {'d': ' DIREITO ', 'e': ' ESQUERDO '}
    num = 0
    if not vitoria(plataformas):
        pas = leiaTexto(
            " ► 'C' para DEIXAR Canibais, 'M' Missionários, 'T' ou 'N': ",
            ['C', 'M', 'T', 'N'])
        if pas != 'N' and pas != 'T' and plataformas['C'] + plataformas[
                'M'] != 0:
            while plataformas[pas] == 0:
                print('\rSem' + nome[pas] +
                      ' na canoa!! Você deve selecionar novamente.', end='')
                pas = leiaTexto(
                    " ► 'C' para DEIXAR Canibais, 'M' Missionários, 'T' ou 'N': ",
                    ['C', 'M', 'T', 'N'])
                if not pas in plataformas:
                    break
            if pas != 'N' and pas != 'T':
                if plataformas[pas] != 1:
                    num = entradaNum(
                        ' ► Quantos' + nome[pas + '2'] + 'vão DESCER do lado' +
                        ladoTexto[lado] + ': ')
                    while num < 0 or num > plataformas[pas]:
                        num = entradaNum(
                            ' ► Quantos' + nome[pas + '2'] +
                            'vão DESCER do lado' + ladoTexto[lado] + ': ')
                else:
                    num = 1
                plataformas[pas] = plataformas[pas] - num
                plataformas[lado + pas] = plataformas[lado + pas] + num
        elif pas == 'T' and plataformas['C'] + plataformas['M'] != 0:
            plataformas[lado +
                        'C'] = plataformas[lado + 'C'] + plataformas['C']
            plataformas[lado +
                        'M'] = plataformas[lado + 'M'] + plataformas['M']
            plataformas['C'] = 0
            plataformas['M'] = 0



def derrota(plataformas):
    if plataformas['dC'] > plataformas['dM'] + plataformas['M'] and plataformas['dM'] > 0:
        return True
    elif plataformas['eC'] > plataformas['eM'] + plataformas['M'] and plataformas['eM'] > 0:
        return True
    return False


def vitoria(plataformas):
    if plataformas['eC'] + plataformas['eM'] == 6:
        return True
    return False

def fim(plataformas):
    sleep(.2)
    if derrota(plataformas):
        print('\r' + ' ' * 90, end='')
        retLinha(11)
        card(30, 30,
            texto=[''], 
            corInfo='\033[1;31m',
            tamanho=20, 
            pulaLinha=4,
            info=[['DERROTA...']]
        )
    elif vitoria(plataformas):
        print('\r' + ' ' * 90, end='')
        retLinha(11)
        card(30, 30,
            texto=[''], 
            corInfo='\033[1;32m',
            tamanho=20, 
            pulaLinha=4,
            info=[['VITÓRIA!']]
        )
    input()
