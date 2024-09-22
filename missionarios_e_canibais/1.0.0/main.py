import missionario_canibal as mc # Biblioteca criada com sub-procedimentos.

plataformas = {'dC': 3, 'dM': 3, 'eC': 0, 'eM': 0, 'C': 0, 'M': 0} # Dicionário para armazenar valores inteiros da quantidade.
lados = {'0': 'd', '1': 'e', '2': 'd'} # Dicionário para identificar qual lado da margem o jogador está.
comeu = False # Variável do tipo lógica (Boolean) para guardar resultado do jogo.

 # ENQUANTO a quantidade de Canibais e Missionários na esquerda for diferente de seis, REPITA.
while plataformas['eC'] + plataformas['eM'] != 6:
  # Variável (lado do tipo inteira) De 0 PARA 2, REPITA. (voltas com o valor 0 e com o valor 1 e depois sai do laço)
    for lado in range(0, 2):
      # SE variável (comeu do tipo lógica) for igual a FALSO E Missionários + Canibais do lado esquerdo for diferente de seis.
        if comeu == False and plataformas['eC'] + plataformas['eM'] != 6:
            mc.Cabecalho(lados[str(lado)], plataformas) # Sub-procedimento para montar cabecalho.
            mc.SobePassageiro(lados[str(lado)], plataformas) # Sub-procedimento para subir passageiro na canoa.
            mc.DescePassageiro(lados[str(lado + 1)], plataformas) # Sub-procedimento para descer passageiro da canoa.
            comeu = mc.ValidaStatus(plataformas, comeu) # Sub-procedimento para validar se os Canibais comeram os Missionários.
      # SE NÃO.
        else:
            break # Sair do laço de repetição PARA (FOR).
  # SE variável (comeu do tipo lógica) for igual a FALSO.
    if comeu == True:
        break # Sair do laço de repetição ENQUANTO (WHILE).

# Após sair do laço de repetição "ENQUANTO", apresentar a mensagem final ao jogador.
mc.Final(comeu, lado, plataformas)