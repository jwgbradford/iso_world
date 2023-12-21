from pygame import event, draw, display, Rect, quit, QUIT, KEYDOWN, K_ESCAPE
from sys import exit
from .world import World
from .settings import TILE_SIZE, WORLD_SIZE


class Game:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.width, self.height = self.screen.get_size()
        self.world = World(WORLD_SIZE)

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(60)
            self.events()
            self.update()
            self.draw()

    def events(self):
        for my_event in event.get():
            if my_event.type == QUIT:
                self.quit_game()
            if my_event.type == KEYDOWN:
                if my_event.key == K_ESCAPE:
                    self.quit_game()

    def quit_game(self):
        quit()
        exit()

    def update(self):
        pass

    def draw(self):
        self.screen.fill((0, 0, 0))
        for x in range(WORLD_SIZE[0]):
            for y in range(WORLD_SIZE[1]):
                sq = self.world.world[x][y]["cart_rect"]
                tile = Rect(sq[0][0], sq[0][1], TILE_SIZE, TILE_SIZE)
                draw.rect(self.screen, (0, 0, 255), tile, 1)
                p = self.world.world[x][y]["iso_poly"]
                p = [(x + self.width/2, y + self.height/4) for x, y in p]
                draw.polygon(self.screen, (255, 0, 0), p, 1)
        display.flip()