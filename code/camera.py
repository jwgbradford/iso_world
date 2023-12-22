from pygame import mouse, Vector2, key, K_RIGHT, K_LEFT, K_UP, K_DOWN
from .settings import WORLD_SIZE, TILE_SIZE

class Camera:

    def __init__(self, width, height):

        self.width = width
        self.height = height

        self.scroll = Vector2(
            (WORLD_SIZE[0] * TILE_SIZE * -1) + (width / 2), 
            (WORLD_SIZE[1] * TILE_SIZE * -0.5) + (height / 2)
            )
        self.dx = 0
        self.dy = 0
        self.speed = 25

    def update(self):
        self.dx = 0
        self.dy = 0
        self.mouse_move()
        self.key_move()
        # update camera scroll
        self.scroll.x += self.dx
        self.scroll.y += self.dy

    def mouse_move(self):
        mouse_pos = mouse.get_pos()
        # x movement
        if mouse_pos[0] > self.width * 0.97:
            self.dx = self.speed * -1
        elif mouse_pos[0] < self.width * 0.03:
            self.dx = self.speed
        # y movement
        if mouse_pos[1] > self.height * 0.96:
            self.dy = self.speed * -1
        elif mouse_pos[1] < self.height * 0.03:
            self.dy = self.speed

    def key_move(self):
        keys = key.get_pressed()
        if keys[K_RIGHT]:
            self.dx = self.speed * -1
        elif keys[K_LEFT]:
            self.dx = self.speed
        if keys[K_UP]: 
            self.dy = self.speed
        elif keys[K_DOWN]:
            self.dy = self.speed * -1
