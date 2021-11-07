import pygame
import random

import particle as p


def main():

    pygame.init()

    width = 640
    height = 640
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((width, height))

    bg = pygame.Surface([width, height])
    bg.fill((0, 0, 0))

    particle_group = pygame.sprite.Group()

    test = False
    # test = True

    # radius,pos_x,pos_y,color,velocity,force
    if test:
        a = p.Particle(5, 150, 150, (255, 255, 255), [0, 0], [0, 0])
        b = p.Particle(5, 140, 200, (255, 0, 255), [0, 0], [0, 0])
        c = p.Particle(5, 100, 300, (0, 0, 255), [0, 0], [0, 0])
        d = p.Particle(5, 350, 350, (0, 255, 255), [0, 0], [0, 0])
        e = p.Particle(5, 40, 20, (255, 255, 0), [0, 0], [0, 0])
        f = p.Particle(5, 100, 100, (255, 0, 0), [0, 0], [0, 0])

        particle_group.add(a)
        particle_group.add(b)
        particle_group.add(c)
        particle_group.add(d)
        particle_group.add(e)
        particle_group.add(f)

    else:
        for i in range(250):
            i = p.Particle(random.randrange(1, 3), random.randrange(width*0.05, width*0.95), random.randrange(height*0.05, height*0.95),
                           (random.randrange(0, 256), random.randrange(0, 256), random.randrange(0, 256)), [random.randrange(0, 1), random.randrange(0, 1)], [0, 0])
            particle_group.add(i)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update()
        screen.blit(bg, (0, 0))
        particle_group.draw(screen)
        particle_group.update()
        clock.tick(30)


if __name__ == "__main__":
    main()
