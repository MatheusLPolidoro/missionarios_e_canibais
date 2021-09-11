import pygame

class Missionario (pygame.sprite.Sprite):
    # classe de missionarios
    def __init__(self, startx, starty):
        pygame.sprite.Sprite.__init__(self)
        self.imgMissionario = pygame.image.load('imagem/missionario.png')
        self.image = self.imgMissionario

        self.rect = self.imgMissionario.get_rect()
        self.rect.topleft = startx, starty


class Canibal (pygame.sprite.Sprite):
    # classe de canibal
    def __init__(self, startx, starty):
        pygame.sprite.Sprite.__init__(self)
        self.imgCanibal = pygame.image.load('imagem/canibal.png')
        self.image = self.imgCanibal

        self.rect = self.imgCanibal.get_rect()
        self.rect.topleft = startx, starty

def draw (self, screen):
    screen.blit(self.image, self.rect)

def main() :
    # Definições dos Objetos (variáveis)
    pygame.init() # inicialização da biblioteca Pygame

    altura = 800
    largura = 450

    ImagemFundo = pygame.image.load ('imagem/cenario.png')

    tela = pygame.display.set_mode([altura, largura]) # tamanho da tela

    corFundo = (255,255,255) # cor de fundo
    
    pygame.display.set_caption('Missionários e Canibais') # titulo da aba
    atualiza = pygame.time.Clock() # variavel que recebe o tempo de atualização  

    # intancia das classes de personagens
    missionario = Missionario(100, 100) 
    canibal = Canibal(200, 100)

    # implementação do jogo
    while True:
        tela.fill(corFundo)
        tela.blit(ImagemFundo, (0, 0))
        atualiza.tick (27)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        draw(missionario, tela)
        draw(canibal, tela)
        pygame.display.update()


main()
