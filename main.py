import pygame
import math
from game import Game

# definir une clock
clock = pygame.time.Clock()
FPS = 60

pygame.init()

# generer la fenetre de notre jeu
pygame.display.set_caption('Adam Game')
screen = pygame.display.set_mode((1080, 720))

# inporter et charger l'arrier plan de notre jeu
background = pygame.image.load('assets/bg.jpg')

# importer charger notre banniere
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)

# importer charger le boutton pour lancai la parti
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 2)

# charger notre jeu
game = Game()
running = True

# boucle tant que cette condition est vrai
while running:
    # appliquer l'arrier plan de notre jeu
    screen.blit(background, (0, -200))

    # je verifie si le jeu a commence
    if game.is_playing:
        # declencher les introduction de la partie
        game.update(screen)
    # verifier si notre jeu n'a pas commence
    else:
        # ajoute mon ecran de binvenue
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)


    # mettre a jour l'ecran
    pygame.display.flip()

    for event in pygame.event.get():

        # si l'evenement est fermer ont va fermer la fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # detecter si la touche espace est enclenchee pour lancai notre projectile
            if event.key == pygame.K_SPACE:
                 if game.is_playing:
                     game.player.launch_projectile()
                 else:
                     # mettre le jeu en mode "lancai"
                     game.start()
                     # jouer le son
                     game.sound_manager.play('click')


        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # verification pour savoir si la souri entre en collision avec le boutton jouer
            if play_button_rect.collidepoint(event.pos):
                # mettre le jeu en mode "lancai"
                game.start()
                # jouer le son
                game.sound_manager.play('click')
                # fixer le nombre fps sur ma clock
                clock.tick(FPS)

