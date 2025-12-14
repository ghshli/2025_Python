import pygame
import random

# pygame 초기화
pygame.init()

# 화면 설정
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("도망쳐, 파란네모!")

# FPS 설정
clock = pygame.time.Clock()

# 색깔 정의
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# 플레이어 설정
player = pygame.Surface((40, 40))
player.fill(BLUE)
player_rect = player.get_rect()
player_rect.centerx = 400
player_rect.bottom = 580

# 적 설정
enemy = pygame.Surface((40, 40))
enemy.fill(RED)
enemy_rect = enemy.get_rect()
enemy_rect.x = random.randint(0, 760)
enemy_rect.y = 0
enemy_speed = 15

# 점수 설정
score = 0
font = pygame.font.SysFont(None, 36)

# 게임 루프
running = True
while running:
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 키 입력 처리
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= 5
    if keys[pygame.K_RIGHT]:
        player_rect.x += 5
    if keys[pygame.K_UP]:
        player_rect.y -= 5
    if keys[pygame.K_DOWN]:
        player_rect.y += 5

    # 화면 밖 이동 제한
    if player_rect.left < 0:
        player_rect.left = 0
    if player_rect.right > 800:
        player_rect.right = 800
    if player_rect.top < 0:
        player_rect.top = 0
    if player_rect.bottom > 600:
        player_rect.bottom = 600

    # 적 이동
    enemy_rect.y += enemy_speed

    #적이 화면 밖으로 나가면 다시 위로
    if enemy_rect.top > 600:
        enemy_rect.y = 0
        enemy_rect.x = random.randint(0, 760)
        score += 1

    # 충돌 판정
    if player_rect.colliderect(enemy_rect):
        running = False

    # 화면 그리기
    screen.fill(WHITE)
    screen.blit(player, player_rect)
    screen.blit(enemy, enemy_rect)

    # 점수 표시
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    # 화면 업데이트
    pygame.display.flip()
    clock.tick(60)

# pygame 종료
pygame.quit()