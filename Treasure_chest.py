# activate the pygame library
import os

import pygame

FPS = 60

# set up window
DISPLAYSURF = pygame.display.set_mode( (400, 300), 0, 32 )
pygame.display.set_caption( 'Treasure_chest' )

chest_image = pygame.image.load( 'image/chest_set.png' )
pygame.image.load( os.path.join( 'image/chest_set.png' ) )
def get_surface():
    'image/chest_set.png'
chestx = 0
chesty = 32
DISPLAYSURF.blit(chest_image,(chestx, chesty))
pygame.display.update()



def get_init ():
        def get_surface():
            'image/chest_set.png.png'

def flip ():
    while True:
            # the main game loop
                DISPLAYSURF.fill( WHITE )


# game variables
# Gold_coin = 25
# silver_coin = 5
# loser = '>25'
# winner = '<25'
# current_draw = 'deal_coins'
# current_play = 'treasure_pot'

def computer_out_put(game_values, winner_vaules):
    if "player_score" != '25':
        return "Gold_coin_winner"

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                fpsClock.tick(FPS)
            pygame.display.update()
