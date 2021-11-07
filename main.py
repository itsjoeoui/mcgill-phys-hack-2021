import pygame
import math
import random
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler()
    ]
)

class Particle(pygame.sprite.Sprite):

    def __init__(self,radius,pos_x,pos_y,color,velocity,force):
        super().__init__()
        
        # Initial properties
        self.radius = radius
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color
        self.velocity = velocity
        self.mass = radius
        self.force = force
        
        # Image rendering
        self.image = pygame.Surface([2*self.radius,2*self.radius])
        self.image.set_colorkey((0, 0, 0))
        self.rect = pygame.draw.circle(self.image, self.color, (self.radius, self.radius), self.radius)

    def get_color(self):
        pass
    
    def get_x(self):
        return self.pos_x
        
    def get_y(self):
        return self.pos_y
    
    def get_mass(self):
        return self.mass
    
    def update(self):
        self.rect.center = (self.pos_x,self.pos_y)
        self.velocity[0] += self.force[0]/self.mass
        self.velocity[1] += self.force[1]/self.mass
        self.pos_x += self.velocity[0]
        self.pos_y -= self.velocity[1]
        self.force = [0,0]

        for i in self.groups():
            for s in i.sprites():

                # Skip itself
                if s == self:
                    continue

                dist_x = abs(s.get_x()-self.get_x())
                dist_y = abs(self.get_y()-s.get_y())
                dist = math.hypot(dist_x, dist_y)

                if dist < (self.radius + s.radius) and self.radius >= s.radius:
                    self.combine(s)
                    logging.info("Combined!")
                    
                if dist_x == 0:
                    f_x = 0
                    f_y = self.mass * s.mass / (dist_x**2+ dist_y**2)
                else:
                    angle = math.atan(dist_y/dist_x)
                    f = self.mass * s.mass / (dist_x**2+ dist_y**2)
                    f_x = math.cos(angle)*f * 0.8
                    f_y = math.sin(angle)*f * 0.8

                if self.get_x() > s.get_x():
                    self.force[0] -= f_x
                else:
                    self.force[0] += f_x

                if self.get_y() > s.get_y():
                    self.force[1] += f_y
                else:
                    self.force[1] -= f_y
            
        # logging.info("Velocity", self.velocity)
        # logging.info("Force:",self.force)
        # logging.info(self.pos_x,self.pos_y)
    
    def combine(self, other):
        new_mass = self.mass+other.mass
        self.radius += other.radius

        self.velocity[0] = (self.mass*self.velocity[0]+other.mass*other.velocity[0])/new_mass
        self.velocity[1] = (self.mass*self.velocity[1]+other.mass*other.velocity[1])/new_mass
        other.kill()

        self.mass = new_mass

        self.image = pygame.Surface([2*self.radius,2*self.radius])
        self.rect = pygame.draw.circle(self.image, self.color, (self.radius, self.radius), self.radius)
        self.rect.center = (self.pos_x,self.pos_y)
        
def main():

    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((500,500))

    bg = pygame.Surface([500,500])
    bg.fill((0,0,0))

    test_group = pygame.sprite.Group()

    # for i in range(30):
    #   i= Particle(random.randrange(1,10), random.randrange(0,500), random.randrange(0,500), (random.randrange(0,256),random.randrange(0,256),random.randrange(0,256)), [random.randrange(0,5),random.randrange(0,5)], [0,0])
    #   test_group.add(i)
    # radius,pos_x,pos_y,color,velocity,force

    a = Particle(5,150,150,(255,255,255),[0,0],[0,0])
    b = Particle(5,140,200,(255,0,255),[0,0],[0,0])
    c = Particle(5,100,300,(0,0,255),[0,0],[0,0])
    d = Particle(5,350,350,(0,255,255),[0,0],[0,0])
    e = Particle(5,40,20,(255,255,0),[0,0],[0,0])
    f = Particle(5,100,100,(255,0,0),[0,0],[0,0])
    
    test_group.add(a)
    test_group.add(b)
    test_group.add(c)
    test_group.add(d)
    test_group.add(e)
    test_group.add(f)
        
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update()
        screen.blit(bg,(0,0))
        test_group.draw(screen)
        test_group.update()
        clock.tick(30)

if __name__ == "__main__":
    main()
