# -------------------------------------------------------
# making a full game using python =>
# -------------------------------------------------------

# import modules
import os
import pygame
# now you can use pygame library font
pygame.font.init()
# the sound will play now
pygame.mixer.init()

# define the variable for use
WIDTH, HEIGHT = 1200, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
# the title for the window
pygame.display.set_caption("first game")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
# the fest for the game
FBS = 60
# the number for the change x-axis and y-axis

VEL = 5
BULLETS_VEL = 8
MAX_BULLETS = 4  # numbering for bullets for each time

# making center border for the game
BORDER = pygame.Rect(WIDTH // 2 - 5, 0, 10, HEIGHT)

# sound for the bullet
BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'Grenade+1.mp3'))  # hit sound
BULLET_FIRE = pygame.mixer.Sound(os.path.join('Assets', 'Gun+Silencer.mp3'))  # fire sound

SPACE_SHIP_WIDTH, SPACE_SHIP_HEIGHT = 55, 40

# making event for bullets
YELLOW_HIT = pygame.USEREVENT + 1  # the number not  mean anything it's for change
RED_HIT = pygame.USEREVENT + 2

# start first spaceship
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets", 'spaceship_yellow.png'))
# how to resize the Image and rotate
YELLOW_SPACESHIP_IMAGE = pygame.transform.rotate(
    pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACE_SHIP_WIDTH, SPACE_SHIP_HEIGHT)),
    90)  # the number for rotate in (90)

# second spaceship
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets", 'spaceship_red.png'))
RED_SPACESHIP_IMAGE = pygame.transform.rotate(
    pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACE_SHIP_WIDTH, SPACE_SHIP_HEIGHT)), -90)

# background image
SPACE = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'space.png')), (WIDTH, HEIGHT))

HEALTH_FONT = pygame.font.SysFont('comicsans', 30)  # first font for player health
WINNER_FONT = pygame.font.SysFont('comicsans', 80)  # second font for the player win


# making draw_wind for
def draw_wind(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health) -> None:
    """
    the order in draw_wind is very important because its define what gone show in the
    first and second for example if I add the spaceships before I make file for the window
    the spaceships will not show in the page because the file for the window cover the spaceships
    :return: add the spaceships and color and spaceship and bullets title and  for the window
    """

    # the code for the background image
    WIN.blit(SPACE, (0, 0))

    pygame.draw.rect(WIN, BLACK, BORDER)

    # health for scoro for the player
    red_health_text = HEALTH_FONT.render("Health: " + str(red_health), 1, WHITE)
    yellow_health_text = HEALTH_FONT.render("Health: " + str(yellow_health), 1, WHITE)
    WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
    WIN.blit(yellow_health_text, (10, 10))

    # add the ships
    # first the start form x and y (x = 0, y = 0)=> start axis  if
    # you want to go down or right increase the value

    # the position will be changed for the move form user yellow and red
    WIN.blit(YELLOW_SPACESHIP_IMAGE, (yellow.x, yellow.y,))

    WIN.blit(RED_SPACESHIP_IMAGE, (red.x, red.y))

    #   draw bullets on the screen
    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)

    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)

    # you must make update for the wind every time to save the changes in the code
    pygame.display.update()


def yellow_handle_movement(key_pressed, yellow):
    """
    the function for handle the move for the yellow spaceship
    :param key_pressed: the key i will press in it to mave the spaceship
    :param yellow: yellow
    :return: (x,y) -+ = 1
    """
    # check this part and understand how it works
    if key_pressed[pygame.K_a] and yellow.x - VEL > 0:  # left key
        yellow.x -= VEL

    if key_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x:  # right key
        yellow.x += VEL

    if key_pressed[pygame.K_w] and yellow.y - VEL > 0:  # up key
        yellow.y -= VEL

    if key_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT - 20:  # right key
        yellow.y += VEL


def red_handle_movement(key_pressed, red):
    """
    the function for handle the move for the red spaceship
    :param key_pressed: the key i will press in it to mave the spaceship
    :param red: yellow
    :return: (x,y) -+ = 1
    """
    if key_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width:  # left key
        red.x -= VEL

    if key_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH:  # right key
        red.x += VEL

    if key_pressed[pygame.K_UP] and red.y - VEL > 0:  # up key
        red.y -= VEL

    if key_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT - 20:  # right key
        red.y += VEL


# handle bullets function
def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    """
    first move the bull if its in yellow_bullets list and remove the bullet if it hit other spaceship or hit the
    right or left corner :param yellow_bullets: list for the bullets yellow :param red_bullets: List for the bullets
    red :param yellow: yellow spaceship :param red: red spaceship :return: the bullets move or deleted the bullets
    that hits the other spaceship or hit the right or left corner
    """
    for bullet in yellow_bullets:
        bullet.x += BULLETS_VEL
        # if bullet hit another spaceship
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)

        # when the bullet out of screen you can hit again
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x -= BULLETS_VEL
        # if bullet hit another spaceship
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        # when the bullet out of screen you can hit again
        elif bullet.x < 0:
            red_bullets.remove(bullet)


# making function for the winner
def draw_winner(text):
    """
    # when the player win its return massage for the player that when and in center of the window
    :param text: The winner
    :return:  the winner in game
    """
    # the type for the color and size
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    # center the text in window
    WIN.blit(draw_text, (WIDTH / 2 - draw_text.get_width() / 2, HEIGHT / 2 - draw_text.get_height() / 2))
    # make update for the screen
    pygame.display.update()
    # make delay to wait 5s and quit the program
    pygame.time.delay(5000)


# make the function for the game loop
def main():
    """
    the function contain red yellow spaceships and red,yellow bullets list and the while loop for the game and more...
    :return: the winner and bullets player health
    """
    # I make this to check for every time if for the position for the yellow and red
    red = pygame.Rect(700, 300, SPACE_SHIP_WIDTH, SPACE_SHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACE_SHIP_WIDTH, SPACE_SHIP_HEIGHT)

    # start making bullets
    red_bullets = []
    yellow_bullets = []

    # making health for the players
    yellow_health = 5
    red_health = 5

    # its show thr frames in second and can change it to look more really and its need good pc
    clock = pygame.time.Clock()

    print(clock)
    run = True
    # make the loop
    while run:
        # for frames in game
        clock.tick(FBS)

        # start event
        for event in pygame.event.get():

            # first event for when event == QUIT the while loop while be false and break
            if event.type == pygame.QUIT:
                run = False

            # event for bullets-for lctrl and rctrl
            if event.type == pygame.KEYDOWN:
                # making the bullet show form the spaceship center to look like real the equation
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height // 2 - 2, 10, 5)
                    yellow_bullets.append(bullet)
                    BULLET_FIRE.play()
                # making the bullet show form the spaceship center to look like real the equation
                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x, red.y + red.height // 2 - 2, 10, 5)
                    red_bullets.append(bullet)
                    BULLET_FIRE.play()

            # check for the hit and health for the player
            if event.type == RED_HIT:
                red_health -= 1
                BULLET_HIT_SOUND.play()
            if event.type == YELLOW_HIT:
                yellow_health -= 1
                BULLET_HIT_SOUND.play()
        winner_text = ""
        # check for the player who the health is equal to 0 or less and show winner
        if red_health <= 0:
            winner_text = "Yellow Wins!"
        if yellow_health <= 0:
            winner_text = "Red Wins!"

        if winner_text != "":
            draw_winner(winner_text)
            break

        # the best way for keys because its every time check for new and can press multiples keys and
        # if I stall press on the key it's will continue to move its very good way
        key_pressed = pygame.key.get_pressed()

        # call the yellow movement function
        yellow_handle_movement(key_pressed, yellow)

        # call the red movement function
        red_handle_movement(key_pressed, red)

        handle_bullets(yellow_bullets, red_bullets, yellow, red)

        #  call the function for use draw wind
        draw_wind(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health)

    pygame.quit()


# this code for the file main while run form the file only not run when I make import for the file form another file
if __name__ == "__main__":
    main()
