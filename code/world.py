from .settings import TILE_SIZE
from pygame import image, Surface
from random import randint

class World:
    def __init__(self, size, width, height):
        self.grass_tiles = Surface((width, height))
        self.tiles = self.load_images()
        self.world_map = self.create_world(size, width, height)

    def create_world(self, size, width, height):
        c, r = size
        world = []
        for col in range(c):
            world.append([])
            for row in range(r):
                world_tile = self.grid_to_world(col, row)
                world[col].append(world_tile)
                render_pos = world_tile["render_pos"]
                self.grass_tiles.blit(self.tiles["block"], (render_pos[0] + width/2, render_pos[1] + height/4))
        return world

    def grid_to_world(self, col, row):
        tile = [
            (col * TILE_SIZE, row * TILE_SIZE),
            (col * TILE_SIZE + TILE_SIZE, row * TILE_SIZE),
            (col * TILE_SIZE + TILE_SIZE, row * TILE_SIZE + TILE_SIZE),
            (col * TILE_SIZE, row * TILE_SIZE + TILE_SIZE)
        ]
        iso_poly = [self.cart_to_iso(x, y) for x, y in tile]
        minx = min([x for x, y in iso_poly])
        miny = min([y for x, y in iso_poly])

        r = randint(1, 100)

        if r <= 5:
            tile = "tree"
        elif r <= 10:
            tile = "rock"
        else:
            tile = ""        
        out = {
            "grid": [col, row],
            "cart_rect": tile,
            "iso_poly": iso_poly,
            "render_pos": [minx, miny],
            "tile": tile        
        }
        return out

    def cart_to_iso(self, x, y):
        iso_x = x - y
        iso_y = (x + y)/2
        return iso_x, iso_y
    
    def load_images(self):
        block = image.load("assets/graphics/block.png")
        tree = image.load("assets/graphics/tree.png")
        rock = image.load("assets/graphics/rock.png")
        return {"block": block, "tree": tree, "rock": rock}