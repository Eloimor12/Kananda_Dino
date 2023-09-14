import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE
from dino_runner.components.dinossaur import Dinossaur
from dino_runner.components.obstacles import Obstacle_Manager
from dino_runner.components.powerups.power_up_manager import PowerManager

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screem = pygame.display.set_mode((SCREEN_HEIGHT,SCREEN_WIDTH))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.score = 0
        self.death_count = 0
        self.gamr_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 300
        self.player = Dinossaur()
        self.obstacle_manager = Obstacle_Manager()
        self.power_up_manager = PowerManager()

    def execute(self):
        self.running = True #primeiro corre
        while self.running: 
            if not self.running:
                self.show_menu()

        pygame.display.quit()
        pygame.quit()

    def run(self):
        self.playing = True #jogador está vivo
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups()
        self.gamr_speed = 20
        self.score = 0
        while self.playing:
            self.events() #abaixar , pular ..
            self.uptade() # novos
            self.draw() 

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def uptade(self):
        user_input = pygame.key.get_pressed()
        self.player.uptade(user_input)
        self.obstacle_manager.uptade(self)
        self.uptade_score()
        self.power_up_manager.uptade()
        self.power_up_manager.uptade(self.score, self.gamr_speed, self.player)