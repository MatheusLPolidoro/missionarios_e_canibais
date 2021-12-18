def branco():
    """
    Cor branco para font no terminal
        => Modifica a cor para branco, cod (\\033[37m)
    """
    print('\033[37m', end='')
    return '\033[37m'  


def azul():
    """
    Cor azul para font no terminal
        => Modifica a cor para azul, cod (\\033[36m)
    """
    print('\033[36m', end='')
    return '\033[36m'


def azul2():
    """
    Cor azul para font no terminal
        => Modifica a cor para azul, cod (\\033[48;5;73m)
    """
    print('\033[48;5;73m', end='')
    return '\033[48;5;73m'


def amarelo():
    """
    Cor amarelo para font no terminal
        => Modifica a cor para amarelo, cod (\\033[33m)
    """
    print('\033[33m', end='')
    return '\033[33m'

def vermelho():
    """
    Cor vermelho para font no terminal
        => Modifica a cor para vermelho, cod (\\033[31m)
    """
    print('\033[31m', end='')
    return '\033[31m'

def verde():
    """
    Cor verde para font no terminal
        => Modifica a cor para verde, cod (\\033[32m)
    """
    print('\033[32m', end='')
    return '\033[32m'

def close():
    """
    fecha o estilo de font no terminal
        => cod (\\033[m)
    """
    print('\033[m', end='')
    return '\033[m'
