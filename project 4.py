import pygame
import random

pygame.init()

screen_width, screen_height = 700, 500
movementspeed = 5
fontsize = 50

bgimage = pygame.transform.scale(pygame.image.load("bg2.jpg"), (screen_width, screen_height))

font = pygame.font.SysFont("Georgia", fontsize)


class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(
            pygame.Color("lavender"))
        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))
        self.rect = self.image.get_rect()

    def move(self, changeinx, changeiny):
        self.rect.x = max(
            min(self.rect.x + changeinx, screen_width - self.rect.width), 0)
        self.rect.y = max(
            min(self.rect.y + changeiny, screen_height - self.rect.height), 0)

# setup
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("colliders")
allsprite = pygame.sprite.Group()

# create sprites
sprite1 = Sprite(pygame.Color("maroon"), 30, 30)
sprite1.rect.x, sprite1.rect.y = random.randint(0, screen_width - sprite1.rect.width), random.randint(0, screen_height - sprite1.rect.height)
allsprite.add(sprite1)

sprite2 = Sprite(pygame.Color("yellow"), 30, 30)
sprite2.rect.x, sprite2.rect.y = random.randint(0, screen_width - sprite2.rect.width), random.randint(0, screen_height - sprite2.rect.height)
allsprite.add(sprite2)

# game loop variables:
running, won = True, False
clock = pygame.time.Clock()

# main game loop:
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_x):
            running = False

    if not won:
        keys = pygame.key.get_pressed()
        x_change = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * movementspeed
        y_change = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * movementspeed
        sprite1.move(x_change, y_change)

        if sprite1.rect.colliderect(sprite2.rect):
            allsprite.remove(sprite2)
            won = True

    # drawing
    screen.blit(bgimage, (0,0))
    allsprite.draw(screen)

    # display win message lols
    if won:
        wintext = font.render("yay!", True, pygame.Color("white"))
        screen.blit(wintext, ((screen_width - wintext.get_width())//2, (screen_height - wintext.get_height())//2))
    
    pygame.display.flip()
    clock.tick(90)

pygame.quit()