import pygame

class Missionario (pygame.sprite.Sprite):
    # classe de missionarios
    def __init__(self, startx, starty, width, heigth):
        pygame.sprite.Sprite.__init__(self)
        self.imgMissionario = pygame.image.load('imagem/missionario.png')
        self.imgMissionario = pygame.transform.scale(self.imgMissionario, (width, heigth))
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

class Canoa (pygame.sprite.Sprite):
    # classe canoa
    def __init__(self, startx, starty):
        pygame.sprite.Sprite.__init__(self)

        self.imgCanoa = pygame.image.load('imagem/canoa.png')
        self.image = self.imgCanoa

        self.rect = self.imgCanoa.get_rect()
        self.rect.topleft = startx, starty

def draw (self, screen):
    screen.blit(self.image, self.rect)



def main() :
    # Definições dos Objetos (variáveis)
    pygame.init() # inicialização da biblioteca Pygame

    # tamanho da tela
    infoObject = pygame.display.Info()

    ImagemFundo = pygame.image.load ('imagem/cenario.png')
    ImagemFundo = pygame.transform.scale(ImagemFundo, (infoObject.current_w, infoObject.current_h))

    tela = DISPLAYSURF = pygame.display.set_mode((infoObject.current_w, infoObject.current_h), pygame.FULLSCREEN) 
    

    corFundo = (255,255,255) # cor de fundo
    
    pygame.display.set_caption('Missionários e Canibais') # titulo da aba
    atualiza = pygame.time.Clock() # variavel que recebe o tempo de atualização  

    # intancia das classes de personagens
    missionario = Missionario(100, 100, 0, 0) 
    canibal = Canibal(200, 100)

    # instancia da classe canoa
    canoa = Canoa(200,300)

    # implementação do jogo
    while True:
        tela.fill(corFundo)
        tela.blit(ImagemFundo, (0, 0))
        atualiza.tick (27)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()                    
        draw(missionario, tela)
        draw(canibal, tela)
        draw(canoa, tela)
        pygame.display.update()


main()
