import pygame

def quit_game(event, main_items):
    if event.type == pygame.QUIT:
        main_items.launched = False

def change_x_pad(event, main_items):
    if event.type == pygame.MOUSEMOTION:
        newpos = event.pos[0] - 30
        main_items.pad.x = newpos
        if not main_items.started :
            main_items.ball.x = newpos + main_items.pad.width/2 - 10

def collisions(main_items):
    if main_items.pad.x < main_items.border_width:
        main_items.pad.x = main_items.border_width
    elif main_items.pad.x + main_items.pad.width > main_items.taille_srf_fond[0] - main_items.border_width:
        main_items.pad.x = main_items.taille_srf_fond[0] - (main_items.border_width +main_items.pad.width)

def collisions_before(main_items):
    if main_items.pad.x < main_items.border_width:
        main_items.pad.x = main_items.border_width
        main_items.ball.x = main_items.border_width + main_items.pad.width/2 - 10
    elif main_items.pad.x + main_items.pad.width > main_items.taille_srf_fond[0] - main_items.border_width:
        main_items.pad.x = main_items.taille_srf_fond[0] - (main_items.border_width +main_items.pad.width)
        main_items.ball.x = main_items.taille_srf_fond[0] - (main_items.border_width +main_items.pad.width) + main_items.pad.width/2 - 10

def click_to_start(event, main_items):
    if event.type == pygame.MOUSEBUTTONDOWN:
        main_items.ball.motion_y = - main_items.ball.speed - 1
        main_items.ball.motion_x = 0
        main_items.started = True

def ball_motion(main_items):
    main_items.ball.y = main_items.ball.y + main_items.ball.motion_y
    main_items.ball.x = main_items.ball.x + main_items.ball.motion_x

def ball_collision(main_items):
    for item in main_items.list_object_to_collide:
        if main_items.ball.colliderect(item):
            main_items.ball.change_motion(main_items.ball.trajectory(item))
            if item.id >= 0:
                main_items.id_to_kill = item.id

def set_ball_memory(main_items):
    main_items.ball.movement_memory((main_items.ball.x, main_items.ball.y))

def parselist(main_items):
    if main_items.id_to_kill >= 0:
        for rect in main_items.list_object_to_collide:
            if rect.id == main_items.id_to_kill:
                main_items.list_object_to_collide.remove(rect)
        for brick in main_items.list_to_draw:
            if brick[2].id == main_items.id_to_kill:
                main_items.list_to_draw.remove(brick)

def check_end(main_items):
    win = True
    for rectangle in main_items.list_to_draw:
        if rectangle[2].id >= 0:
            win = False
    if win:
        main_items.ended = True
        font_end = pygame.font.Font("Fonts/BADABB__.TTF", 160)
        main_items.txt_end = (font_end.render("BRAVO !!!", True, (255,0,0)), (300,200))
    elif main_items.ball.y > main_items.taille_srf_fond[1]:
        main_items.ended = True
        font_end = pygame.font.Font("Fonts/BADABB__.TTF", 160)
        main_items.txt_end = (font_end.render("GAME OVER", True, (255,0,0)), (225,200))

