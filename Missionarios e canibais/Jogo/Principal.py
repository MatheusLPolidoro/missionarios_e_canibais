import Jogo_2 as mc
def main():
    plataformas = {'dC': 3, 'dM': 3, 'eC': 0, 'eM': 0, 'C': 0, 'M': 0}
    lados = {'0': 'd', '1': 'e', '2': 'd'}
    comeu = False
    while plataformas['eC'] + plataformas['eM'] != 6:
        for lado in range(0,2):
            if comeu == False:
                mc.Cabecalho(lados[str(lado)],plataformas)
                mc.SobePassageiro(lados[str(lado)], plataformas)
                mc.DescePassageiro(lados[str(lado + 1)], plataformas)
                comeu = mc.ValidaStatus(plataformas,comeu)
            else:
                break
        if comeu == True:
            break
    mc.Final(comeu,lado, plataformas)

