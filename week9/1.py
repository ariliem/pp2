import pygame
from datetime import datetime

pygame.init()

width, height = 800, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mickey Mouse Clock")

second_hand_image = pygame.image.load("leftarm.png")
minute_hand_image = pygame.image.load("rightarm.png")
mickey_image = pygame.image.load("mainclock.png")
mickey_rect = mickey_image.get_rect(center=(width // 2, height // 2))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    now = datetime.now()
    second_angle = now.second * 6
    minute_angle =60 + now.minute * 6  
    screen.fill((255, 255, 255))
    screen.blit(mickey_image, mickey_rect)
    rotated_second_hand = pygame.transform.rotate(second_hand_image, -second_angle)
    second_hand_rect = rotated_second_hand.get_rect(center=mickey_rect.center)
    screen.blit(rotated_second_hand, second_hand_rect)
    rotated_minute_hand = pygame.transform.rotate(minute_hand_image, -minute_angle)
    minute_hand_rect = rotated_minute_hand.get_rect(center=mickey_rect.center)
    screen.blit(rotated_minute_hand, minute_hand_rect)
    pygame.display.flip()
    pygame.time.Clock().tick(30)
