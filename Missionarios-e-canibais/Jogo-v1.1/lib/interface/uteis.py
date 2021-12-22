from lib.interface.cores import *
from os import system
import sys
import msvcrt
from time import sleep


cores = {
    'original': close(),
    'branco': branco(),
    'azul': azul(),
    'amarelo': amarelo(),
    'verde': verde(),
    'vermelho': vermelho(),
}


def cabecalho(texto='', 
                separador='▲▼', 
                tamanho=0, 
                cor='original', 
                linhaCima=True, 
                linhaBaixo=True,
                linhaCentro=False
            ):
    """
    entrada personalizado
        -> Apresentar um titulo para uma tabela, formulario ou sistema (CLI)
        :param texto: Mensagem que o titulo contem.
        :param separador: (opcional) Separador do titulo.
        :param tamanho: (opcional) Tamanho do titulo.
        :param cor: (opcional) Cor do titulo, pode ser o nome da cor ou o codigo.
        :param linhaCima: (opcional) Se verdadeiro coloca o separador escolhido na parte de cima.
        :param linhaBaixo: (opcional) Se verdadeiro coloca o separador escolhido na parte de baixo.
        :param linhaCentro: (opcional) Se verdadeiro coloca uma linha no centro do titulo.
        :return: Nao retorna valores
    """
    system('cls')
    close()
    if cor not in cores: 
        cores[cor] = cor
    if not tamanho: 
        tamanho = len(texto) + 4
    sys.stdout.write(cores[cor])
    if linhaCima: 
        sys.stdout.writelines(f'{separador*tamanho}\n')
    if linhaCentro and len(separador) == 1: 
        texto = f'{texto:{separador}^{tamanho // len(separador)}}'
    sys.stdout.writelines(f'{texto:^{tamanho * len(separador)}}\n')
    if linhaBaixo: 
        sys.stdout.writelines(f'{separador*tamanho}\n')
    close()


def rodape(texto='', 
            separador='▲▼', 
            tamanho=0, 
            cor='original', 
            linhaCima=True, 
            linhaBaixo=True,
            linhaCentro=False,
            posicao=10
        ):
    """
    saida personalizado
        -> Apresentar um fechamento para uma tabela, formulario ou sistema (CLI)
        :param texto: Mensagem que o rodape contem.
        :param separador: (opcional) Separador do rodape.
        :param tamanho: (opcional) Tamanho do rodape.
        :param cor: (opcional) Cor do rodape
        :param linhaCima: (opcional) Se verdadeiro coloca o separador escolhido na parte de cima.
        :param linhaBaixo: (opcional) Se verdadeiro coloca o separador escolhido na parte de baixo.
        :param linhaCentro: (opcional) Se verdadeiro coloca uma linha no centro do titulo.
        :param posicao: (opcional) Referencia para quantidade de linhas acima do rodape.
        :return: Nao retorna valores
    """
    if not tamanho: 
        tamanho = len(texto) + 4
    sys.stdout.write(cores[cor])
    sys.stdout.write('\n' * posicao)
    if linhaCima: 
        sys.stdout.write(f'{separador*tamanho}\n')
    if linhaCentro and len(separador) == 1: 
        texto = f'{texto:{separador}>{tamanho // len(separador)}}'
    sys.stdout.write(f'{texto:>{(tamanho * len(separador)) - 2}}\n')
    if linhaBaixo: 
        sys.stdout.write(f'{separador*tamanho}\n')
    close()


def leiaInt(msg: str, /, lista=list(), comeca=1, pulaLinha=0, cor='azul') -> int:
    """
    -> Ler a entrada de um numero inteiro.
    :param msg: (obrigatorio) Mensagem exibida ao usuario.
    :param lista: (opcional) Lista de itens que podem podem ser escolhidos.
    :return: Valor inteiro.
    """
    op = -1
    if cor not in cores:
        cores[cor] = cor
    sys.stdout.write(cores[cor])
    while True:
        try:
            sys.stdout.write('\r' + msg)
            if op == -1:
                limparEntrada(10)
                key = b'\x31'
                op = 0
            else:
                key = msvcrt.getch()
            if key != b'\r':
                if str(key.decode()).isnumeric():
                    sys.stdout.write(key.decode())
                op = int(key)
        except (ValueError, TypeError):
            if key == b'H' or key == b'M':
                if op < len(lista):
                    op += 1
                elif op >= len(lista):
                    op = comeca                  
                sys.stdout.write(f'{op:<20}')
            elif key == b'P' or key == b'K':
                if op > comeca:
                    op -= 1    
                elif op <= comeca:
                    op = len(lista)            
                sys.stdout.write(f'{op:<20}')
            continue
        else:
            if op in range(comeca, len(lista) + 1) and key == b'\r':
                sys.stdout.write('\n' * pulaLinha)
                close()
                return op


def leiaTexto(msg, lista=list()):
    # Validar a entrada de teclas do usuário
    op = -1
    while True:
        azul()
        sys.stdout.write('\r' + msg)
        if op == -1:
            limparEntrada(10)
            key = b'\x31'
            op = 0
        sys.stdout.write('\r' + msg)
        close()
        key = msvcrt.getch()
        if key not in [b'\xe0', b'\x86', b'\x85', b'\x1b', b'\r', b'\x87']:
            key = key.decode().upper()
            sys.stdout.write(key)
        if key in lista:
            op = key
        if key == b'\r' and op in lista:
            key = ''
            return op


def cardTitulo(*margem,
                texto=list(), 
                tamanho=0, 
                cor='azul', 
                corFundo='original' 
            ):
    """
    Titulo de card personalizado
        -> Apresentar um titulo para card.
        :param texto: (opcional) Mensagens que o card contem no topo.
        :param tamanho: (opcional) Tamanho do card.
        :param cor: (opcional) Cor do card, pode ser o nome da cor ou o codigo.
        :param margem: (opcional) Define quantos espacos de margem o card tem.
        :return: Nao retorna valores
    """
    if not len(margem):
        margem = (3, 5, 5, 3)
    for i, item in enumerate(texto):
        sys.stdout.write(cores[corFundo])
        sys.stdout.write(' ' * int(margem[0][i]))           
        sys.stdout.write(cores[cor])
        sys.stdout.write(f'{item:^{tamanho}}')
    sys.stdout.write(cores[corFundo])
    sys.stdout.write(' ' * int(margem[0][len(margem) - 1]))     
    close()
    sys.stdout.write('\n')


def cardInfoDado(*margem,
                    coluna=1, 
                    separador=' ', 
                    tamanho=0, 
                    cor='azul',
                    corFundo='original',
                    info=list(),
                    pulaLinha=1,
                    alinhamento = '^'
                ):
    """
    Informacoes do card
        -> Apresentar as informacoes para card.
        :param coluna: (opcional) Numero de colunas do card
        :param separador: (opcional) Separador do card.
        :param tamanho: (opcional) Tamanho do card.
        :param cor: (opcional) Cor do card, pode ser o nome da cor ou o codigo.
        :param informacoes: (opcional) Lista com dados que o card possui.
        :param margem: (opcional) Define quantas espacos de margem o card tem.
        :param pulaLinha: (opcional) Define o numero de linhas que seram puladas.
        :alinhamento: (opcional) Define como o texto ficara alinhado no card.
        :return: Nao retorna valores
    """
    if not len(margem):
        margem = (3, 5, 5, 3)                
    for inf in info:
        col = coluna
        i = 0
        while col:
            sys.stdout.write(cores[corFundo])
            sys.stdout.write(' ' * int(margem[0][i]))
            sys.stdout.write(cores[cor])
            sys.stdout.write(f'{inf[i]:{alinhamento}{tamanho}}')
            sys.stdout.write(cores[corFundo])
            if i < len(inf):
                i += 1
            else:
                i = 0
            col -= 1
            close()
        sys.stdout.write(cores[corFundo])
        sys.stdout.write(' ' * int(margem[0][i]))
        sys.stdout.write('\n')
        cardLinha(coluna=coluna, 
                tamanho=tamanho, 
                cor=cor, 
                pulaLinha=pulaLinha, 
                *margem,
                separador=separador
            )


def cardLinha(*margem,
            coluna=1, 
            separador=' ', 
            tamanho=0, 
            cor='original',
            corFundo='original', 
            pulaLinha=1
        ):
    """
    Pular linha(s) para o card personalizado
        -> Apresentar uma linha sem conteudo para uma tabela, formulario ou sistema (CLI)
        :param coluna: (opcional) Numero de colunas que a linha possui.
        :param separador: (opcional) Caractere que forma a linha.
        :param tamanho: (opcional) Tamanho do card.
        :param cor: (opcional) Cor do card, pode ser o nome da cor ou o codigo.
        :param margem: (opcional) Define quantas espacos de margem o card tem.
        :param pulaLinha: (opcional) Quantas linhas voce quer pular.
        :return: Nao retorna valores
    """
    if not len(margem):
        margem = (3, 5, 5, 3)
    while pulaLinha:
        col = coluna
        i = 0
        while col:
            sys.stdout.write(cores[corFundo])
            sys.stdout.write(' ' * int(margem[0][i]))
            sys.stdout.write(cores[cor])
            sys.stdout.write(f'{"":{separador}^{tamanho}}')
            if i < coluna:
                i += 1
            else:
                i = 0
            col -= 1          
        pulaLinha -= 1
        sys.stdout.write(cores[corFundo])
        sys.stdout.write(' ' * int(margem[0][i]))
        close()
        sys.stdout.write('\n')    


def limparEntrada(qtd, tras=False):
    """
    -> Limpa a entrada de texto
    :param qtd: (obrigatorio) Numeros de caracteres que deseja limpar.
    :param tras: (opcional) Se verdadeiro apaga apenas do cursor para tras.
    :return: Nao retorna valores.
    """
    if not tras:
        sys.stdout.write(' ' * qtd)
    sys.stdout.write('\b' * qtd)


def retLinha(linha):
    """
    -> Voltar linhas no terminal (Nao funciona em todos os terminais)
    :param linha: Numero de linhas que voltara no terminal.
    :return: Nao retorna valores.
    """
    while linha:
        # \r = ENTER
        # \x1b = ESC
        # \x41 = A 
        sys.stdout.write(f'\r\x1b\x41\r')
        linha -= 1