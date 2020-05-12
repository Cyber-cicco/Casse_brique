import pygame
import Events

def events_parsing(main_items):
    if not main_items.ended:
        for event in pygame.event.get():
            Events.quit_game(event, main_items)
            Events.change_x_pad(event, main_items)
            Events.collisions(main_items)
        Events.ball_collision(main_items)
        Events.parselist(main_items)
        Events.set_ball_memory(main_items)
        Events.check_end(main_items)
        Events.ball_motion(main_items)
    else:
        for event in pygame.event.get():
            Events.quit_game(event, main_items)

def events_parsing_before(main_items):
    for event in pygame.event.get():
        Events.quit_game(event, main_items)
        Events.change_x_pad(event, main_items)
        Events.collisions_before(main_items)
        Events.click_to_start(event,main_items)