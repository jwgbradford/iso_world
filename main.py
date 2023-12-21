from pygame import init, mixer, display, time, FULLSCREEN
from code.game import Game

def main():
    running = True
    playing = True
    init()
    mixer.init()
    screen = display.set_mode((0, 0), FULLSCREEN)
    clock = time.Clock()
    # implement menus
    # implement game
    game = Game(screen, clock)
    while running:
        # start menu goes here
        while playing:
            # game loop here
            game.run()

if __name__ == "__main__":
    main()