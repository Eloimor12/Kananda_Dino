import pygame
from pygame.transform import scale
import os

# Global Constants
TITLE = "Megaman"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")
SOUND_DIR = os.path.join(os.path.dirname(__file__), "..", "assets","Sounds")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "WallpaperMagaman.png"))

RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Run00.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Run01.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Run02.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Run03.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Run04.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Run05.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Run06.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Run07.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Run08.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Run09.png")),

]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/RunShield00.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/RunShield01.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/RunShield02.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/RunShield03.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/RunShield04.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/RunShield05.png")),    
    pygame.image.load(os.path.join(IMG_DIR, "Dino/RunShield06.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/RunShield07.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/RunShield08.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/RunShield09.png")),
    
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/Jump00.png"))
JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/Jump01.png"))
JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/Jump02.png"))
JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Dino/JumpShield00.png"))
JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Dino/JumpShield01.png"))
JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Dino/JumpShield02.png"))
JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpHammer.png"))

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Duck00.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Duck01.png")),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DuckShield00.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DuckShield01.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Duck00.png")),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/CactusSmall00.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/CactusSmall01.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/CactusSmall02.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/CactusLarge00.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/CactusLarge01.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/CactusLarge02.png")),
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird00.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird01.png")),
]

DEATH_SOUND = pygame.mixer.Sound(os.path.join(SOUND_DIR, '11 - MMX - X Die.wav'))
JUMP_SOUND = pygame.mixer.Sound(os.path.join(SOUND_DIR, '08 - MMX - X Jump.wav'))
SCORE_SOUND = pygame.mixer.Sound(os.path.join(SOUND_DIR, '00 - MMX _X Score.wav'))
DUCK_SOUND = pygame.mixer.Sound(os.path.join(SOUND_DIR, '07 - MMX - X Duck.wav'))
POWER_UP_SOUND = pygame.mixer.Sound(os.path.join(SOUND_DIR, '13 - MMX - X Shield.wav'))
BACKGROUND_SOUND = pygame.mixer.Sound(os.path.join(IMG_DIR, '02 Intro Stage'))
CLOUD =pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud00.png'))
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png'))


BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/chao3.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"
