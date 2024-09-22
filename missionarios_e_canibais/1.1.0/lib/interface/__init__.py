from lib.interface.cores import *
from lib.interface.uteis import *


def menu(lista: list, 
            tamanho=0, 
            separador='▲▼', 
            titulo='MENU PRINCIPAL', 
            textoRodape='MySYS', 
            cor='original',
            linhaBaixo=True,
            linhaCima=True,
            linhaCentro=False,
            posicao=0,
            caract='•'
        ) -> int:
    """
    -> Print de menu de opcoes.
    :param lista: (obrigatorio) Lista com todas as opcoes do menu.
    :param separador: (opcional) Separador do titulo e rodape.
    :param tamanho: (opcional) Tamanho do titulo rodape e opcoes.
    :param cor: (opcional) Cor do titulo e rodape.
    :param linhaCima: (opcional) Se verdadeiro coloca o separador escolhido na parte de cima.
    :param linhaBaixo: (opcional) Se verdadeiro coloca o separador escolhido na parte de baixo.
    :param linhaCentro: (opcional) Se verdadeiro coloca uma linha no centro do titulo.
    :return: Numero inteiro da opção do menu.
    """
    if not tamanho:
        tamanho = len(titulo) + 4
    if not posicao:
        posicao = (len(lista) * 4)
    if posicao > 13:
        posicao = 13
    if posicao < 10:
        posicao += 5
    lista = lista[:7]
    centro = (round(tamanho * len(separador)) - len(titulo)) // 2
    opcoes = (sum([len(l) for l in lista]) / len(lista)) + 4
    if len(titulo) > opcoes:
        centro += round((len(titulo) - opcoes)) // 2
    cabecalho(titulo, 
                separador=separador, 
                tamanho=tamanho, 
                cor=cor, 
                linhaCima=linhaCima, 
                linhaBaixo=linhaBaixo,
                linhaCentro=linhaCentro
            )
    rodape(
            textoRodape, 
            separador=separador, 
            tamanho=tamanho, 
            cor=cor,
            linhaCima=linhaCima, 
            linhaBaixo=linhaBaixo,
            linhaCentro=linhaCentro,
            posicao=posicao
        )
    # Voltar as linhas no terminal.Nao funciona em todo terminal:
    retLinha(posicao)
    for op, item in enumerate(lista, 1):
        azul()
        sys.stdout.write(f'\r{" " * centro}{op} {caract} {item}\n')
        close()
    op = leiaInt(f'\r{" " * centro}\033[33m► Sua Opção: \033[m', lista, pulaLinha=3)
    return op


def card(*margem,
            texto=list(), 
            separador=' ', 
            tamanho=0, 
            corTitulo='amarelo', 
            corInfo='azul',
            info=list(),
            pulaLinha=1,
            alinhamento='^'
        ):
    """
    card personalizado
        -> Apresentar um card para uma tabela, formulario ou sistema (CLI)
        :param texto: (opcional) Lista com mensagens que o card contem.
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
    if corTitulo not in cores:
        cores[corTitulo] = corTitulo
    if corInfo not in cores:
        cores[corInfo] = corInfo
    if not tamanho:
        tamanho = len(texto) + 4
    cardTitulo(margem,
                texto=texto, 
                tamanho=tamanho, 
                cor=corTitulo, 
            )
    cardLinha(margem,
                coluna=len(texto), 
                tamanho=tamanho, 
                cor=corInfo, 
                pulaLinha=pulaLinha, 
                separador=separador
            )
    cardInfoDado(margem,
                    coluna=len(texto),
                    info=info,
                    tamanho=tamanho, 
                    cor=corInfo, 
                    pulaLinha=pulaLinha, 
                    separador=separador,
                    alinhamento=alinhamento
                )

def animacao(msg, quadros, vezes):
    i = 0
    while vezes:
        verde()
        print(f'\r{msg + quadros[i]:^80}', end='')
        if i < len(quadros) -1:
            i += 1
        else:
            i = 0
        sleep(.1)
        vezes -= 1
    print(f'\r{" ":^80}', end='')
    close()
    print()    