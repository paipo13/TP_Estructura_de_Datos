import pygame
import random
pygame.init()
p_ancho=600
p_alto=600
pantalla=pygame.display.set_mode((p_ancho,p_alto))

player= pygame.Rect((250,250,40,40))
a=50
b=0
c=0
correr=True
while correr:
    pantalla.fill((a,b,b))
    pygame.draw.rect(pantalla,(a+50,b+50,c+50),player)
    key= pygame.key.get_pressed()
    if key[pygame.K_a]:
        player.move_ip(-1,0)
    if key[pygame.K_d]:
        player.move_ip(1,0)
    if key[pygame.K_w]:
        player.move_ip(0,-1)
    if key[pygame.K_s]:
        player.move_ip(0,1)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            correr=False
        if event.type == pygame.MOUSEBUTTONDOWN:
            a=random.randint(0,100)
            b=random.randint(0,100)
            c=random.randint(0,100)
        # if event.type == pygame.KEYDOWN:
        #         key= pygame.key.get_pressed()
        #         if key[pygame.K_a]:
        #             player.move_ip(-20,0)
        #         if key[pygame.K_d]:
        #             player.move_ip(20,0)
        #         if key[pygame.K_w]:
        #             player.move_ip(0,-20)
        #         if key[pygame.K_s]:
        #             player.move_ip(0,20)
    pygame.display.update()
pygame.quit()
