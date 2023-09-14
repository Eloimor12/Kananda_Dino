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
        self.game_speed = 20
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
        self.game_speed = 20
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
        self.power_up_manager.uptade(self.score, self.game_speed, self.player)

    def upatade_score(self):
        self.score += 1 
        if self.score %100 == 0:
            self.game_speed += 5 # mais rápdo a cada 100 pontos

    def draw(self):
        self.clock.tick(FPS)
        self.screem.fill((255, 255, 255)) #representa o branco 
        self.draw_background()
        self.player.draw(self.screem)
        self.obstacle_manager.draw(self.screem)
        self.draw_score()
        self.draw_power_up_time()
        self.power_up_manager.draw(self.screem)
        pygame.display.uptade()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screem.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screem.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= image_width:
            self.screem.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
            self.x_pos_bg -= self.game_speed

    def draw_score(self):
        draw_message_component( # desenhando a pontuação, números atualizando 
            f"Score: {self.score}", 
            self.screem,
            pos_x_center = 1000,
            pos_y_center = 50
        )
    
    def draw_power_up_time(self): 
        if self.player.has_power_up: #escudo no jogo
            time_to_show = round((self.player.power_up_time - pygame.time.get_ticks()) / 1000, 2)
            if time_to_show >= 0:
                draw_message_component(
                    f"{self.player.type.capitalize()} dispinível por {time_to_show} segundos",
                    self.screem, 
                    font_size = 18, 
                    pos_x_center = 500, #posição da mensagem 
                    pos_y_center = 40 
                )
            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE

    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

            elif event.type == pygame.KEYDOWN:
                self.run()

    def show_manu(self):
            self.screem.fill((255, 255, 255))
            half_screem_height == SCREEN_HEIGHT // 2
            half_screem_width == SCREEN_WIDTH // 2
            if self.death_count == 0:
                draw_message_component("Pressione qualaquer tecla para iniciar", self.screem)
            else:
                draw_message_component("Pressione qualquer tecla para reinicar", self.screem, pos_y_center = half_screem_height + 140)
                draw_message_component(
                    f"Sua pontuação: {self.score}",
                    self.screem, 
                    pos_y_center = half_screem_height - 50
                )

                draw_message_component(
                    f"Contagem de vidas: {self.death_count}",
                    self.screem,
                    pos_y_center = half_screem_height - 100
                )

                self.screem.blit(ICON, (half_screem_width - 40, half_screem_hight - 30))
            
            pygame.display.flip()
            self.handle_events_on_menu
