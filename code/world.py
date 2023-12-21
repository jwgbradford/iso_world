from .settings import TILE_SIZE
from pygame import image, Surface
from random import randint
from noise import pnoise2

class World:
    def __init__(self, size):
        self.tiles = self.load_images()
        self.world_map = self.create_world_map(size)
        self.world_base = self.create_world_base(size)

    def create_world_base(self, size):
        base_surface = Surface((
            size[0] * TILE_SIZE * 2, 
            size[1] * TILE_SIZE + 2 * TILE_SIZE)
        ).convert_alpha()
        c, r = size
        for col in range(c):
            for row in range(r):
                render_pos = self.world_map[col][row]["render_pos"]
                base_surface.blit(
                    self.tiles["block"], 
                    (render_pos[0] + base_surface.get_width() / 2, render_pos[1])
                )
        return base_surface
    
    def create_world_map(self, size):
        c, r = size
        perlin_scale = c / 2
        world_map = []
        for col in range(c):
            world_map.append([])
            for row in range(r):
                world_tile = self.grid_to_world(col, row, perlin_scale)
                world_map[col].append(world_tile)
        return world_map

    def grid_to_world(self, col, row, perlin_scale):
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
        perlin = 100 * pnoise2(col/perlin_scale, row/perlin_scale)

        if (perlin >= 15) or (perlin <= -35):
            tile = "tree"
        else:
            if r == 1:
                tile = "tree"
            elif r == 2:
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
        block = image.load("assets/graphics/block.png").convert_alpha()
        tree = image.load("assets/graphics/tree.png").convert_alpha()
        rock = image.load("assets/graphics/rock.png").convert_alpha()
        return {"block": block, "tree": tree, "rock": rock}