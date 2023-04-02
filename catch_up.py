from pygame import *

def my_sprite_collide(x1, y1, x2, y2):
    if x1 <= x2 <= x1 +80 and y1 <= y2 <= y1 +80:
        return True
    return False


main_win = display.set_mode((800,600))
display.set_caption('Догонялки')

background = transform.scale(image.load("background.png"), (800, 600))


ghost1 = transform.scale(image.load("sprite1.png"), (80, 80))
ghost2 = transform.scale(image.load("sprite2.png"), (80, 80))

run = True
clock = time.Clock()

ghost1_xcor = 100
ghost1_ycor = 300
ghost2_xcor = 300
ghost2_ycor = 300
while run:
    keys_pressed = key.get_pressed()
    if keys_pressed[K_UP] and ghost1_ycor > 0:
        ghost1_ycor -= 10
    if keys_pressed[K_DOWN] and ghost1_ycor < 520:
        ghost1_ycor += 10
    if keys_pressed[K_LEFT] and ghost1_xcor > 0:
        ghost1_xcor -= 10
    if keys_pressed[K_RIGHT] and ghost1_xcor < 720:
        ghost1_xcor += 10

    if keys_pressed[K_w] and ghost2_ycor > 0:
        ghost2_ycor -= 10
    if keys_pressed[K_s] and ghost2_ycor < 520:
        ghost2_ycor += 10
    if keys_pressed[K_a] and ghost2_xcor > 0:
        ghost2_xcor -= 10
    if keys_pressed[K_d] and ghost2_xcor < 720:
        ghost2_xcor += 10

    if my_sprite_collide(ghost1_xcor, ghost1_ycor, ghost2_xcor, ghost2_ycor):
        print('Столкновение')
        

    main_win.blit(background, (0,0))
    main_win.blit(ghost1, (ghost1_xcor,ghost1_ycor))
    main_win.blit(ghost2, (ghost2_xcor,ghost2_ycor))
    
    display.update()

    for e in event.get():
        if e.type == QUIT:
            run = False

        
    clock.tick(60)


