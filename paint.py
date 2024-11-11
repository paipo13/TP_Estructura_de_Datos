import pygame
class Paint:
    def __init__(self):
        self.nombre='Paint'
    def dibujar(self):
        """ Permite dibujar por pantalla."""
        pygame.init()
        p_ancho=600
        p_alto=600
        pantalla=pygame.display.set_mode((p_ancho,p_alto))
        negro=(0,0,0)
        blanco=(255,255,255)
        azul=(0,0,255)
        verde=(0,255,0)
        rojo=(255,0,0)
        morado=(150,0,150)
        a=14
        b=2
        color1=pygame.Rect((0,0,a,a))
        color2=pygame.Rect((a,0,a,a))
        color3=pygame.Rect((0,a,a,a))
        color4=pygame.Rect((a,a,a,a))
        color5=pygame.Rect((0,2*a,a,a))
        color6=pygame.Rect((a,2*a,a,a))
        borrador=pygame.Rect((0,600-a,a,a))
        clear=pygame.Rect((a,600-a,a,a))
        color_actual=negro
        pos=pygame.mouse.get_pos()
        x=pos[0]
        y=pos[1]
        dibujo=pygame.Rect((x,y,2,2))
        run = True
        pantalla.fill((255,255,255))
        while run:
            pos=pygame.mouse.get_pos()
            x=pos[0]
            y=pos[1]
            dibujo=pygame.Rect((x,y,b,b))
            pygame.draw.rect(pantalla,blanco,color1)
            pygame.draw.rect(pantalla,negro,color2)
            pygame.draw.rect(pantalla,azul,color3)
            pygame.draw.rect(pantalla,verde,color4)
            pygame.draw.rect(pantalla,rojo,color5)
            pygame.draw.rect(pantalla,morado,color6)
            pygame.draw.rect(pantalla,negro,borrador,width=2)
            pygame.draw.rect(pantalla,rojo,clear,width=2)
            if color1.collidepoint(pos):
                if pygame.mouse.get_pressed()[0]:
                    color_actual=blanco
                    b=2
            elif color2.collidepoint(pos):
                if pygame.mouse.get_pressed()[0]:
                    color_actual=negro
                    b=2
            elif color3.collidepoint(pos):
                if pygame.mouse.get_pressed()[0]:
                    color_actual=azul
                    b=2
            elif color4.collidepoint(pos):
                if pygame.mouse.get_pressed()[0]:
                    color_actual=verde
                    b=2
            elif color5.collidepoint(pos):
                if pygame.mouse.get_pressed()[0]:
                    color_actual=rojo
                    b=2
            elif color6.collidepoint(pos):
                if pygame.mouse.get_pressed()[0]:
                    color_actual=morado
                    b=2
            elif borrador.collidepoint(pos):
                if pygame.mouse.get_pressed()[0]:
                    color_actual=blanco
                    b=20
            elif clear.collidepoint(pos):
                if pygame.mouse.get_pressed()[0]:
                    pantalla.fill((255,255,255))
                    pygame.draw.rect(pantalla,blanco,color1)
                    pygame.draw.rect(pantalla,negro,color2)
                    pygame.draw.rect(pantalla,azul,color3)
                    pygame.draw.rect(pantalla,verde,color4)
                    pygame.draw.rect(pantalla,rojo,color5)
                    pygame.draw.rect(pantalla,negro,borrador,width=2)
                    pygame.draw.rect(pantalla,rojo,clear,width=2)
            else:
                if pygame.mouse.get_pressed()[0]:
                    pygame.draw.rect(pantalla,color_actual,dibujo) 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            pygame.display.update()
        pygame.quit()