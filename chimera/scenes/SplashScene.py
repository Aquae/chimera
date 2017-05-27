import pygame
from .MainMenuScene import MainMenuScene

class SplashScene(object):

    def __init__(self):
        super(SplashScene, self).__init__()
        self.font = pygame.font.SysFont('Arial', 56)
        self.sfont = pygame.font.SysFont('Arial', 32)

    def render(self, screen):
        screen.fill((0, 200, 0))
        heading = self.font.render('Chimera', True, (255, 255, 255))
        subheading = self.sfont.render('> press space to start <', True, (255, 255, 255))
        screen.blit(heading, (200, 50))
        screen.blit(subheading, (200, 350))

    def update(self):
        pass

    def handle_events(self, events):
        for e in events:
            if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
                self.manager.go_to(MainMenuScene())
