import pygame
import sys

# 초기화
pygame.init()

# 화면 설정
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("블럭 깨기 게임")

# 색깔 정의
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# 패들 설정
paddle_width, paddle_height = 200, 10
paddle_x = (width - paddle_width) // 2
paddle_y = height - 20

# 공 설정
ball_radius = 10
ball_x, ball_y = width // 2, height // 2
ball_speed_x, ball_speed_y = 3, 3

# 블럭 설정
block_width, block_height = 50, 20
blocks = []
for i in range(5):
    for j in range(10):
        block = pygame.Rect(j * (block_width + 5), i * (block_height + 5), block_width, block_height)
        blocks.append(block)

# 게임 루프
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= 5
    if keys[pygame.K_RIGHT] and paddle_x < width - paddle_width:
        paddle_x += 5

    # 공 이동
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # 벽과 충돌 검사
    if ball_x <= 0 or ball_x >= width:
        ball_speed_x = -ball_speed_x
    if ball_y <= 0:
        ball_speed_y = -ball_speed_y

    # 패들과 충돌 검사
    if paddle_y <= ball_y <= paddle_y + paddle_height and paddle_x <= ball_x <= paddle_x + paddle_width:
        ball_speed_y = -ball_speed_y

    # 블럭과 충돌 검사
    for block in blocks:
        if block.colliderect(pygame.Rect(ball_x - ball_radius, ball_y - ball_radius, ball_radius * 2, ball_radius * 2)):
            blocks.remove(block)
            ball_speed_y = -ball_speed_y

    # 화면 그리기
    screen.fill(black)
    pygame.draw.rect(screen, white, (paddle_x, paddle_y, paddle_width, paddle_height))
    pygame.draw.circle(screen, red, (ball_x, ball_y), ball_radius)

    for block in blocks:
        pygame.draw.rect(screen, white, block)

    pygame.display.flip()
    clock.tick(60)
