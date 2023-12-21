from pygame import font


def draw_text(screen, text, size, colour, pos):
    my_font = font.SysFont(None, size)
    text_surface = my_font.render(text, True, colour)
    text_rect = text_surface.get_rect(topleft=pos)
    screen.blit(text_surface, text_rect)