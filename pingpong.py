import pygame

# Initsialiseeri pygame
pygame.init()

# Ekraani seaded
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("pingpong")

# Taustavärv
BG_COLOR = (200, 200, 255)

# Lae pildid (failid peavad olema samas kaustas)
ball_img = pygame.image.load("pall.png").convert_alpha()
paddle_img = pygame.image.load("alus.png").convert_alpha()

# Palli alguskoordinaadid
ball_rect = ball_img.get_rect(center=(screen_width // 2, screen_height // 2))
ball_speed_x = 4
ball_speed_y = 4

# Aluse alguskoordinaadid
paddle_rect = paddle_img.get_rect()
paddle_rect.x = (screen_width - paddle_rect.width) // 2
paddle_rect.y = int(screen_height / 1.5)
paddle_speed = 6

# Punktid ja font
score = 0
font = pygame.font.SysFont(None, 36)

# Kella seadistus
clock = pygame.time.Clock()
running = True

# Mängutsükkel
while running:
    screen.fill(BG_COLOR)

    # Sündmuste käsitlus
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Klahvijuhtimine
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_rect.left > 0:
        paddle_rect.x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_rect.right < screen_width:
        paddle_rect.x += paddle_speed

    # Palli liikumine
    ball_rect.x += ball_speed_x
    ball_rect.y += ball_speed_y

    # Seinapõrked
    if ball_rect.left <= 0 or ball_rect.right >= screen_width:
        ball_speed_x *= -1
    if ball_rect.top <= 0:
        ball_speed_y *= -1  # punkt ei muutu enam siin

    # Aluse tabamine
    if ball_rect.colliderect(paddle_rect) and ball_speed_y > 0:
        ball_speed_y *= -1
        score += 1

    # Alumise ääre kontroll
    if ball_rect.top > screen_height:
        score -= 1
        ball_rect.center = (screen_width // 2, screen_height // 2)
        ball_speed_y *= -1

    # Joonista alus ja pall
    screen.blit(paddle_img, paddle_rect)
    screen.blit(ball_img, ball_rect)

    # Kuva tulemus
    score_text = font.render(f"Punktid: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    # Uuenda kuva
    pygame.display.flip()
    clock.tick(60)

pygame.quit()