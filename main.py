# File created by: Diego Avila
# Agenda:
# gIT GITHUB    
# Build file and folder structures
# Create libraries
# testing github changes
# I changed something - I changed something else tooooo!

# This file was created by: Diego Avila
# Sources: http://kidscancode.org/blog/2016/08/pygame_1-1_getting-started/
# Sources: https://kidscancode.org/blog/2016/08/pygame_shmup_part_3/
# Sources: https://kidscancode.org/blog/2016/08/pygame_shmup_part_4/

'''
Game structure:
GOALS; RULES; FEEDBACK; FREEDOM
My goal is:

Slime mob
Player gets bounced away when colliding

Score
Everytime the player collides with mob score goes down 1

Reach goal:
use images and animated sprites...

Rules:
Avoid the mobs and earn the least possible score

Feedback:
Can change the starting position of the player and mobs
Can add a creative background and use images for mobs and player
Can keep the player from leaving the screen or make the player come back when they leave the screen

Freedom:
can keep playing for an unlimited amount of time

'''

# import libs
import pygame as pg
import os
# import settings 
from settings import *
from sprites import *
from os import path
# from pg.sprite import Sprite

# set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "images")

# create game class in order to pass properties to the sprites file
class Game:
    def __init__(self):
        # init game window etc.
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("my game")
        self.clock = pg.time.Clock()
        self.running = True
        print(self.screen)
    # loads image of Mr Game & Watch
    def load_data(self):
        self.player_img = pg.image.load(path.join(img_folder, "Game-Watch.png")).convert()
    def new(self):
        # starting a new game
        self.score = 0
        self.load_data()
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.player = Player(self)
        self.plat1 = Platform(WIDTH, 50, 0, HEIGHT-50, (150,150,150), "normal")
        # self.plat1 = Platform(WIDTH, 50, 0, HEIGHT-50, (150,150,150), "normal")
        self.all_sprites.add(self.plat1)

        self.platforms.add(self.plat1)
        
        self.all_sprites.add(self.player)
        # adds platforms
        for plat in PLATFORM_LIST:
            p = Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)
        for i in range(0,10):
            m = Mob(20,20,(0,255,0))
            self.all_sprites.add(m)
            self.enemies.add(m)
        self.run()
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
    
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                # spacebar is to jump
                if event.key == pg.K_SPACE:
                    self.player.jump()
    def update(self):
        self.all_sprites.update()
        # when player collides with enemies they will receive a -1
        mhits = pg.sprite.spritecollide(self.player, self.enemies, False)
        if mhits:
            if abs(self.player.vel.x) > abs(self.player.vel.y):
                self.player.vel.x *= -1
            else:
                self.player.vel.y *= -1
            self.score -= 1

        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                if hits[0].variant == "disappearing":
                    hits[0].kill()
                elif hits[0].variant == "bouncey":
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = -PLAYER_JUMP
                else:
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = 0
    # draw/render
    def draw(self):
        self.screen.fill(BLUE)
        self.all_sprites.draw(self.screen)
        self.draw_text(str(self.score), 24, WHITE, WIDTH/2, HEIGHT/2)
        # is this a method or a function?
        pg.display.flip()
    # draws text at midtop
    def draw_text (self, text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface, text_rect)
    def get_mouse_now(self):
        x,y = pg.mouse.get_pos()
        return (x,y)

# instantiate the game class...
g = Game()

# kick off the game loop
while g.running:
    g.new()

pg.quit()