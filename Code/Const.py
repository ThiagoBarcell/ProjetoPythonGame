import pygame

# C
COLOR_YELLOW = (253, 255, 47)
COLOR_WHITE = (255,255,255)
COLOR_BLACK = (0,0,0)
COLOR_RED = (255,0,0)
COLOR_BLUE =(33,0,255)

# D
DAMAGE_GLOBAL ={
      'Level/car_1_01': 100,
      'Level/car_2_01': 20,
      'Level/car_3_01': 100,
      'Level/Road_00': 100,
      'Level/Road_01': 100,
      'Level/Road_02': 100 }

# E
ENTITY_SPEED ={
    'Level1Bg0':0,
    'Level1Bg1':1,
    'Level1Bg2':2,
    'Level1Bg3':3,
    'Level1Bg4':4,
    'Level1Bg5':5,
    'Level1Bg6':6,
}
ENTITY_SPEED_FIXO = 10

EVENT_ENEMY = pygame.USEREVENT + 1

EVENT_CRASH = pygame.USEREVENT + 2

# p
PLAYER_KEY_UP = { 'Level/car_1_01': pygame.K_UP,
                  'Level/car_3_01': pygame.K_w}
PLAYER_KEY_DOWN = { 'Level/car_1_01': pygame.K_DOWN,
                  'Level/car_3_01': pygame.K_s}
PLAYER_KEY_LEFT = { 'Level/car_1_01': pygame.K_LEFT,
                  'Level/car_3_01': pygame.K_a}
PLAYER_KEY_RIGHT = { 'Level/car_1_01': pygame.K_RIGHT,
                  'Level/car_3_01': pygame.K_d}
PLAYER_FAROL = 0

# G
GAME_VOLUME = 0.1

# H
HEALTH_GLOBAL ={
      'Level/car_1_01': 101,
      'Level/car_2_01': 100,
      'Level/car_3_01': 101,
      'Level/Road_00': 100,
      'Level/Road_01': 100,
      'Level/Road_02': 100 }

# M
MENU_OPTION = ( 'NEW GAME 1P',
                'NEW GAME 2P - COOPERATIVE',
                'NEW GAME 2P - COMPETITIVE',
                'SCORE',
                'EXIT')

# S
SPAWN_TIME = 1000

# W
WIN_WIDTH = 510
WIN_HEIGHT = 324