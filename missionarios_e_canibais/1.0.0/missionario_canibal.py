import missionario_canibal as mc
import os


def Cabecalho(lado, plataformas):
    # Limpar a tela e demonstrar as regras e objetivos ao jogador
    os.system('cls')
    print(' ' * 84)
    print('\n +', '-' * 84, '+')
    print(' |', '{: ^84}'.format('MISSIONÁRIOS E CANIBAIS'), '|')
    print(' +', '-' * 84, '+')
    print(' |', ' ' * 84, '|')
    print(' |', '{: ^84}'.format('OBJETIVO:'), '|')
    print(
        ' |', '{: ^84}'.format(
            'AJUDAR A TRAVESSIA DOS MISSIONÁRIOS E DOS CANIBAIS ENTRE AS MARGENS DO RIO'
        ), '|')
    print(' |', ' ' * 84, '|')
    print(' |', '{: ^84}'.format('REGRAS:'), '|')
    print(' |',
          '{: ^84}'.format('1. NÃO É POSSÍVEL ATRAVESSAR COM A CANOA VAZIA'),
          '|')
    print(
        ' |', '{: ^84}'.format(
            '2. SOMENTE 2 PASSAGEIROS PODEM SUBIR NA CANOA POR VEZ'), '|')
    print(
        ' |', '{: ^84}'.format(
            '3. NÃO PODE DEIXAR MISSIONÁRIOS EM LOCAIS COM MAIS CANIBAIS'),
        '|')
    print(' |', ' ' * 84, '|')
    print(' +', '-' * 84, '+\n')
    # Apresenta o status do jogo e onde o jogador está
    print(' +', '-' * 20, '+', ' ' * 6, '+', '-' * 20, '+', ' ' * 6, '+',
          '-' * 20, '+')
    print(' |', '{: ^20}'.format('ESQUERDO'), '|', ' ' * 6, '|',
          '{: ^20}'.format('CANOA'), '|', ' ' * 6, '|',
          '{: ^20}'.format('DIREITO'), '|')
    print(' +', '-' * 20, '+', ' ' * 6, '+', '-' * 20, '+', ' ' * 6, '+',
          '-' * 20, '+')
    print(' |', ' ' * 20, '|', ' ' * 6, '|', ' ' * 20, '|', ' ' * 6, '|',
          ' ' * 20, '|')
    print(' |', '{: ^20}'.format('CANIBAIS: ' + str(plataformas['eC'])), '|',
          ' ' * 6, '|', '{: ^20}'.format('CANIBAIS: ' + str(plataformas['C'])),
          '|', ' ' * 6, '|',
          '{: ^20}'.format('CANIBAIS: ' + str(plataformas['dC'])), '|')
    print(' |', ' ' * 20, '|', ' ' * 6, '|', ' ' * 20, '|', ' ' * 6, '|',
          ' ' * 20, '|')
    print(' |', '{: ^20}'.format('MISSIONÁRIOS: ' + str(plataformas['eM'])),
          '|', ' ' * 6, '|',
          '{: ^20}'.format('MISSIONÁRIOS: ' + str(plataformas['M'])), '|',
          ' ' * 6, '|',
          '{: ^20}'.format('MISSIONÁRIOS: ' + str(plataformas['dM'])), '|')
    print(' |', ' ' * 20, '|', ' ' * 6, '|', ' ' * 20, '|', ' ' * 6, '|',
          ' ' * 20, '|')
    print(' +', '-' * 20, '+', ' ' * 6, '+', '-' * 20, '+', ' ' * 6, '+',
          '-' * 20, '+')
    if lado == 'd':
        print('{: >86}'.format('<<--( VOCÊ )-->>\n'))
    else:
        print('{: ^26}'.format('<<--( VOCÊ )-->>\n'))


def EntradaTexto(msg, valor, lado, plataformas):
    # Validar a entrada de teclas do usuário
    valido = False
    while valido == False:
        dig = input(msg).upper()
        mc.Cabecalho(lado, plataformas)
        for x in valor:
            if str(x) == dig:
                valido = True
                break
        if valido == False:
            print('O valor "' + dig + '" é invalido!! ')
    return dig


def EntradaNum(msg, lado, plataformas):
    # Receber um número do usuário
    while True:
        dig = input(msg)
        mc.Cabecalho(lado, plataformas)
        try:
            dig = int(dig)
            break
        except ValueError:
            print('O valor "' + dig + '" é invalido!! ', end="", flush=True)
    return dig


def SobePassageiro(lado, plataformas):
    # Realiza a manipulação dos valores de acordo com as opções selecionadas
    StrPas = {
        'C': ' CANIBAL',
        'M': ' MISSIONÁRIO',
        'C2': ' CANIBAIS ',
        'M2': ' MISSIONÁRIOS '
    }
    TrvPas = {'C': 'M', 'M': 'C'}
    while True:
        if plataformas['eC'] + plataformas['eM'] != 6:
            if plataformas['C'] + plataformas['M'] < 2 and plataformas[
                    lado + 'C'] + plataformas[lado + 'M'] > 0:
                pas = mc.EntradaTexto(
                    " -'C' para PEGAR (Canibais), 'M' (Missionários), 'N' (Nenhum): ",
                    ['M', 'C', 'N'], lado, plataformas)
                if pas in plataformas:
                    while plataformas[lado + pas] < 1:
                        mc.Cabecalho(lado, plataformas)
                        print('Sem' + StrPas[pas] + ' na margem...')
                        pas = mc.EntradaTexto(
                            " -'C' para PEGAR (Canibais), 'M' (Missionários): ",
                            ['M', 'C'], lado, plataformas)
                    if pas in plataformas and plataformas[lado + pas] > 0:
                        num = mc.EntradaNum(
                            'Quantidade de' + StrPas[pas + '2'] +
                            'que você quer COLOCAR na canoa:', lado,
                            plataformas)
                        while plataformas[
                                lado +
                                pas] < num or num < 0 or num > 2 or num + plataformas[
                                    'C'] + plataformas['M'] > 2:
                            mc.Cabecalho(lado, plataformas)
                            print('A quantidade "' + str(num) +
                                  '" é invalida!! ')
                            num = mc.EntradaNum(
                                'Quantidade de' + StrPas[pas + '2'] +
                                'que você quer COLOCAR na canoa:', lado,
                                plataformas)
                        plataformas[pas] = plataformas[pas] + num
                        plataformas[lado + pas] = plataformas[lado + pas] - num
                        if plataformas[lado + 'C'] + plataformas[
                                lado +
                                'M'] > 0 and plataformas['C'] + plataformas[
                                    'M'] < 2 and plataformas[lado +
                                                             TrvPas[pas]] != 0:
                            msg = ' -Ainda tem um espaço na canoa. Quer COLOCAR um' + StrPas[
                                TrvPas[pas]] + '? [S/N]:'
                            msg = mc.EntradaTexto(msg, ['S', 'N'], lado,
                                                  plataformas)
                            if msg == 'S':
                                plataformas[
                                    TrvPas[pas]] = plataformas[TrvPas[pas]] + 1
                                plataformas[lado + TrvPas[pas]] = plataformas[
                                    lado + TrvPas[pas]] - 1
                    elif pas == 'N':
                        print('Nenhum passageiro subiu...', end='', flush=True)
                        input()
                    else:
                        mc.Cabecalho(lado, plataformas)
                        print('Sem ' + StrPas[pas] + 'na margem...')
            if plataformas['C'] + plataformas['M'] > 0:
                break
            else:
                mc.Cabecalho(lado, plataformas)
                print('A canoa está vazia...')


def DescePassageiro(lado, plataformas):
    # Realiza a manipulação dos valores de acordo com as opções selecionadas
    StrPas = {
        'C': ' CANIBAL',
        'M': ' MISSIONÁRIO',
        'C2': ' CANIBAIS ',
        'M2': ' MISSIONÁRIOS '
    }
    StrLado = {'d': ' DIREITO ', 'e': ' ESQUERDO '}
    num = 0
    if plataformas['eC'] + plataformas['eM'] != 6:
        mc.Cabecalho(lado, plataformas)
        pas = mc.EntradaTexto(
            " -'C' para DEIXAR (Canibais), 'M' (Missionários), 'T' (todos) ou 'N' (Nenhum): ",
            ['C', 'M', 'T', 'N'], lado, plataformas)
        if pas != 'N' and pas != 'T' and plataformas['C'] + plataformas[
                'M'] != 0:
            while plataformas[pas] == 0:
                mc.Cabecalho(lado, plataformas)
                print('Sem' + StrPas[pas] +
                      ' na canoa!! Você deve selecionar novamente.')
                pas = mc.EntradaTexto(
                    " -'C' para deixar (Canibais), 'M' (Missionários), 'T' (todos) ou 'N' (Nenhum): ",
                    ['C', 'M', 'T', 'N'], lado, plataformas)
                if not pas in plataformas:
                    break
            if pas != 'N' and pas != 'T':
                if plataformas[pas] != 1:
                    num = mc.EntradaNum(
                        'Quantos' + StrPas[pas + '2'] + 'vão DESCER do lado' +
                        StrLado[lado] + ': ', lado, plataformas)
                    while num < 0 or num > plataformas[pas]:
                        mc.Cabecalho(lado, plataformas)
                        print(
                            'Quantidade invalida!! Você deve selecionar novamente.'
                        )
                        num = mc.EntradaNum(
                            'Quantos' + StrPas[pas + '2'] +
                            'vão DESCER do lado' + StrLado[lado] + ': ', lado,
                            plataformas)
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
        elif pas == 'N' and plataformas['C'] + plataformas['M'] != 0:
            print('Nenhum passageiro desceu...', end='', flush=True)
            input()
        else:
            print('A canoa esta VAZIA...', end='', flush=True)
            input()
        mc.Cabecalho(lado, plataformas)


def ValidaStatus(plataformas, comeu):
    if plataformas['dC'] > plataformas['dM'] + plataformas[
            'M'] and plataformas['dM'] > 0:
        comeu = True
    elif plataformas['eC'] > plataformas['eM'] + plataformas[
            'M'] and plataformas['eM'] > 0:
        comeu = True
    else:
        comeu = False
    return comeu


def Final(comeu, lado, plataformas):
    mc.Cabecalho(lado, plataformas)
    print(' +', '-' * 84, '+')
    if comeu == False:
        print(' |', '{: ^84}'.format('PARABÉNS VOCÊ VENCEU !!!'), '|')
    else:
        print(' |', '{: ^84}'.format('VOCÊ PERDEU !!!'), '|')
    print(' +', '-' * 84, '+')
    input()
