from .settings import TILE_SIZE

class World:
    def __init__(self, size):
        self.world = self.create_world(size)

    def create_world(self, size):
        c, r = size
        world = []
        for col in range(c):
            world.append([])
            for row in range(r):
                world_tile = self.grid_to_world(col, row)
                world[col].append(world_tile)
        return world

    def grid_to_world(self, col, row):
        tile = [
            (col * TILE_SIZE, row * TILE_SIZE),
            (col * TILE_SIZE + TILE_SIZE, row * TILE_SIZE),
            (col * TILE_SIZE + TILE_SIZE, row * TILE_SIZE + TILE_SIZE),
            (col * TILE_SIZE, row * TILE_SIZE + TILE_SIZE)
        ]
        iso_poly = [self.cart_to_iso(x, y) for x, y in tile]
        out = {
            "grid": [col, row],
            "cart_rect": tile,
            "iso_poly": iso_poly
        }
        return out

    def cart_to_iso(self, x, y):
        iso_x = x - y
        iso_y = (x + y)/2
        return iso_x, iso_y