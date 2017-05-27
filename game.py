import chimera
import chimera.scenes
import pygame

def main():
    pygame.init()
    icon = pygame.image.load("resources/window_icon.png")
    pygame.display.set_icon(icon)

    screen = pygame.display.set_mode((1000,1000))
    pygame.display.set_caption("Chimera")
    pygame.display.flip()

    timer = pygame.time.Clock()
    running = True

    manager = chimera.scenes.SceneManager(chimera.scenes.SplashScene())

    while running:
        timer.tick(60)

        if pygame.event.get(pygame.QUIT):
            running = False
            pygame.display.quit()
            return

        manager.scene.handle_events(pygame.event.get())
        manager.scene.update()
        manager.scene.render(screen)

        pygame.display.flip()

if __name__ == "__main__":
    main()