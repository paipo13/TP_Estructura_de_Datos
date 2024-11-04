import pygame
import button
pygame.init()
p_ancho=600
p_alto=600
pantalla=pygame.display.set_mode((p_ancho,p_alto))
text_font = pygame.font.SysFont("Helvetica", 50)

#function for outputting text onto the screen
def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  pantalla.blit(img, (x, y))

wpp_img = pygame.image.load('App_con_pygame\wpp.jpg').convert_alpha()
wpp_button = button.Button(250, 250, wpp_img, 0.1)
player= pygame.Rect((250,250,40,40))
run = True
en_app=False
while run:
	if not en_app:
		pantalla.fill((255,255,255))
		if wpp_button.draw(pantalla):
			en_app=True
	if en_app:
		pantalla.fill((50,150,50))
		draw_text("Welcome to Whatsapp", text_font, (255, 255, 255), 100, 250)

	#event handler
	for event in pygame.event.get():
		#quit game
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()

pygame.quit()