import pygame
from objects import Alien, Hero, Generator, Rocket

class Game:
    screen = None
    rockets = []
    aliens = []
    lost = False
    score = 0

    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.name = pygame.display.set_caption('sZpejs inwejders.exe')
        done = False

        hero = Hero(self, width / 2, height - 20)
        generator = Generator(self)
        rocket = None


        while not done:



            self.display_score(Alien.score)

            if len(self.aliens) == 0:
                self.display_text("GG EZ, GET REKT")

            # for event in pygame.event.get():
            #     if event.type == pygame.QUIT:
            #         done = True

            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_LEFT]:
                hero.x -= 5 if hero.x > 20 else 0
            elif pressed[pygame.K_RIGHT]:
                hero.x += 5 if hero.x < width - 40 else 0
            elif pressed[pygame.K_UP]:
                hero.y -= 5 if hero.y > 20 else 0
            elif pressed[pygame.K_DOWN]:
                hero.y += 5 if hero.y < height - 20 else 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                    done = True

                if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                    done = True
                    Game(600, 400)
                    pygame.display.update()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not self.lost:
                    self.rockets.append(Rocket(self, hero.x + 10, hero.y))

            pygame.display.flip()
            self.clock.tick(60)
            self.screen.fill((0, 0, 0))

            for alien in self.aliens:

                alien.draw()
                alien.check_collision(self)

                if (alien.y > hero.y):
                    self.lost = True
                    self.display_text('YOU DIED')

            for rocket in self.rockets:
                rocket.draw()


            if not self.lost: hero.draw()



        # if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not self.lost:
        #     self.rockets.append(Rocket(self, hero.x, hero.y))


    def display_text(self, text):
        pygame.font.init()
        font = pygame.font.SysFont('bookmanoldstylepogrubiony', 45)
        textsurface = font.render(text, False, (204, 0, 0))
        self.screen.blit(textsurface, (110, 160))

    def display_score(self, score):
        pygame.font.init()
        font = pygame.font.SysFont('bookmanoldstylepogrubiony', 20)
        textsurface = font.render('Masz Scora: ' + str(score) , False, (255, 255, 255))
        self.screen.blit(textsurface, (0, 0))