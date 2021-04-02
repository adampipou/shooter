import pygame
import random
# creer une classe pour gerer cette comete
from monster import Mummy, Alien


class Comet(pygame.sprite.Sprite):

    def __init__(self, comet_event):
        super().__init__()
        # definire une image associer a cette comet
        self.image = pygame.image.load('assets/comet.png')
        self.rect = self.image.get_rect()
        self.velocity = random.randint(2, 4)
        self.rect.x = random.randint(20, 800)
        self.rect.y = -  random.randint(0, 800)
        self.comet_event = comet_event

    def remove(self):
        self.comet_event.all_comets.remove(self)
        # jouer le son
        self.comet_event.game.sound_manager.play('meteorite')

        # verifier si le nombre de commete est de 0
        if len(self.comet_event.all_comets) == 0:
            # remmetre la barre a 0
            self.comet_event.reset_percent()
            # apparetre les deux premier monstre
            self.comet_event.game.spawn_monster(Mummy(self.comet_event.game))
            self.comet_event.game.spawn_monster(Mummy(self.comet_event.game))
            self.comet_event.game.spawn_monster(Alien(self.comet_event.game))

    def fall(self):
        self.rect.y += self.velocity

        # ne tombe pas sur le sol
        if self.rect.y >= 500:
            print("sol")
            # retirer la boule de feu
            self.remove()
        # verifier si la boule de feu touche le joueur
        if self.comet_event.game.check_collision(
            self, self.comet_event.game.all_players
        ):
            print("Joueur touche !")
            # retirer la boule de feu
            self.remove()

            # si il n y a plus de boule de feu
            if len(self.comet_event.all_comets) == 0:
                print("l'evenement est fini")
                # remmetre la jauge au depart
                self.comet_event.reset_percent()
                self.comet_event.fall_mode = False

            # subire 20 point de degat
            self.comet_event.game.player.damage(20)