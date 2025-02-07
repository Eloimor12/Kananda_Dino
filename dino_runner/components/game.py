import pygame 
import pygame.mixer
pygame.init()  # iniciar pygame # 
pygame.mixer.init()
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, SCORE_SOUND, BACKGROUND_SOUND, CLOUD, GAME_OVER
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager #importando todos os obtaculos
from dino_runner.utils.text_utils import draw_message_component
from dino_runner.components.powerups.power_up_manager import PowerUpManager #importando o poder

class Game:
    def __init__(self): # costrutor classe game
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.score = 0
        self.record = 0
        self.death_count = 0  #contagem de vidas
        self.game_speed = 20 #velocidade
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.x_pos_cloud = 0 #posição nuvem 
        self.y_pos_cloud = 30  
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        self.score_sound = SCORE_SOUND # som do score
        self.score_sound.set_volume(0.5) 
        self.background_sound = BACKGROUND_SOUND # som da tela de fundo
          
    def execute(self): #jogador corre, o jogo continua rodando, se não, ele reseta
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()

        pygame.display.quit()
        pygame.quit()
    
    def run(self): #
        self.playing = True
        self.obstacle_manager.reset_obstacles() #reset dos obstaculos
        self.power_up_manager.reset_power_up() #reset dos power ups
        self.game_speed = 20 
        self.score = 0
        self.background_sound.play(1)

        while self.playing:
            self.events()
            self.update()
            self.draw ()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.ruinning = False
            
    def update(self): #atualizando 
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.update_score()
        self.power_up_manager.update(self.score, self.game_speed, self.player)


    def update_score(self):  #a cada 100 pontos a velocidade aumenta
        self.score += 1
        if self.score % 100 == 0:
            self.game_speed +=  5
            self.score_sound.play() #play som score
        if self.score >= self.record: #adicionei score
            self.record = self.score

    def draw(self): # tela do jogo , com tudo que vai aparecer na tela
        self.clock.tick(FPS)  
        self.screen.fill((173, 234, 234))
        self.draw_blackground()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.draw_cloud()
        self.draw_score()
        self.draw_power_up_time()
        self.power_up_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()
        
    def draw_blackground(self): #construindo a tela
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= - image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed #aleteração para o chao se mover

    def draw_score(self): #pontuação no jogo 
        draw_message_component(
            f"Score: {self.score}",
            self.screen,
            pos_x_center = 1000, #posião no jogo 
            pos_y_center = 50
        )
        draw_message_component(
            f"Record: {self.score}",
            self.screen,
            pos_x_center = 1000, #posião no jogo 
            pos_y_center = 75
        )

    def draw_power_up_time(self): #mostrar o tempo
        if self.player.has_power_up:
            time_to_Show = round((self.player.power_up_timing - pygame.time.get_ticks()) / 1000, 2) # mostra a contagem 
            if time_to_Show >= 0:
                draw_message_component(
                    f"{self.player.type.capitalize()} disponível por  {time_to_Show} segundos",
                    self.screen,
                    font_size = 20, #tamanho da fonte
                    pos_x_center = 500, #posição no jogo
                    pos_y_center = 40
                )
            else:
                    self.player.has_power_up = False
                    self.player.type = DEFAULT_TYPE 
    
    def draw_cloud(self):
        image_width = CLOUD.get_width()
        self.screen.blit(CLOUD, (image_width + self.x_pos_cloud, self.y_pos_cloud))
        if self.x_pos_cloud <= - image_width:
            self.screen.blit(CLOUD, (image_width + self.x_pos_cloud, self.y_pos_cloud))
            self.x_pos_cloud = 1000

        self.x_pos_cloud -= self.game_speed #ultrapassar toda a tela(1000) para surgir a nova nuvem
    
    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.run()

    def show_menu(self): #começo e o final do jogo
        self.screen.fill((50, 153, 204))
        half_screen_height = SCREEN_HEIGHT // 2
        hals_screen_width = SCREEN_WIDTH // 2 
        if self.death_count == 0:
            draw_message_component("Pressione qualquer tecla para iniciar", self.screen)
        else:
            draw_message_component("Pressione qualquer tecla para reiniciar", self.screen, pos_y_center = half_screen_height + 140)
            draw_message_component(
                f"Sua pontuaçao: {self.score}",
                self.screen,
                pos_y_center = half_screen_height - 50
            )
            self.background_sound.stop()

            draw_message_component(
                f"Contagem de vidas: {self.death_count} ",
                self.screen,
                pos_y_center = half_screen_height - 100
            )
            draw_message_component(
                f"Record: {self.record} ",
                self.screen,
                pos_y_center = half_screen_height + 100
            )
            self.screen.blit(ICON, (hals_screen_width - 40, half_screen_height - 30))
            self.screen.blit(GAME_OVER, (hals_screen_width - 200, half_screen_height - 190)) #aparecer game over no final

        pygame.display.flip()
        self.handle_events_on_menu()