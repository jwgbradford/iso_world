from pygame import event, draw, display, Rect, quit, QUIT, KEYDOWN, K_ESCAPE
from sys import exit
from .world import World
from .settings import TILE_SIZE, WORLD_SIZE
from .utils import draw_text
from .camera import Camera

class Game:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.width, self.height = self.screen.get_size()
        self.world = World(WORLD_SIZE)
        self.camera = Camera(self.width, self.height)

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
        self.camera.update()

    def draw(self):
        scroll_x = self.camera.scroll.x
        scroll_y = self.camera.scroll.y
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.world.world_base, (scroll_x, scroll_y))
        for x in range(WORLD_SIZE[0]):
            for y in range(WORLD_SIZE[1]):
                render_pos =  self.world.world_map[x][y]["render_pos"]
                tile = self.world.world_map[x][y]["tile"]
                if tile != "":
                    self.screen.blit(
                        self.world.tiles[tile],
                        (
                            render_pos[0] + self.world.world_base.get_width() / 2 + scroll_x,
                            render_pos[1] + (self.world.tiles[tile].get_height() - TILE_SIZE) + scroll_y
                        )
                    )
        draw_text(
            self.screen,
            'fps={}'.format(round(self.clock.get_fps())),
            25,
            (255, 255, 255),
            (10, 10)
        )
        display.flip()