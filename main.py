from boundary import rectangle
from entity import entity
from quadTree import quadTree
import pygame
import random

WIDTH = 600
HEIGHT = 600
def main():
    running = True
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    boundary = rectangle(200,200,100,100)
    
    qt = quadTree(rectangle(0, 0, WIDTH, HEIGHT), 8)
    for i in range(1000):
        qt.insert(entity(random.randint(0, WIDTH), random.randint(0, HEIGHT)))

    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        qt.draw(screen)
        boundary.x, boundary.y = pygame.mouse.get_pos()
        boundary.x -= boundary.get_width() / 2
        boundary.y -= boundary.get_height() / 2
        boundary.draw(screen, (255,255,255))
        entities = qt.query(boundary)
        for entt in entities:
            pygame.draw.circle(screen,(255,255,0),(entt.x, entt.y),4,1)
        pygame.display.flip()
        clock.tick()
        pygame.display.set_caption(str(clock.get_fps()))

if __name__ == '__main__':
    main()