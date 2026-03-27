import pygame 

pygame.init()
tela = pygame.display.set_mode((500,500))
run = True

while run:
s
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
        tela.fill((35,250,210))
        pygame.draw.rect(tela, ('#c0fcf8'), (235,235,30,30))
        pygame.display.update()
pygame.quit()