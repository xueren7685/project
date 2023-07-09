import pygame
import sys
import time
import random


color_red = pygame.Color(255, 0, 0)
color_white = pygame.Color(255, 255, 255)
color_pink = pygame.Color(255, 192, 203)
color_black = pygame.Color(0, 0, 0)


pygame.init()


screen = pygame.display.set_mode((700, 600))
pygame.display.set_caption("20202068 SHIYAN")


background_image = pygame.image.load("grass.jpg")
background_surface = pygame.transform.scale(background_image, (700, 600))

# 배경음악을 불러와 재생하기
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(-1)

# 먹은 음식의 음향을 불러오다
eat_sound = pygame.mixer.Sound("eat.mp3")

# 게임 영역 만들기
arr = [([0] * 61) for i in range(71)]  # 创建一个二维数组

# 뱀의 초기 위치와 길이
x = 10
y = 10
snake_lon = 3

# 뱀의 초기 운동 방향
way = 1  # 1: 오른쪽으로 이동, 2: 왼쪽으로 이동, 3: 위로 이동, 4: 아래로 이동

# 게임 종료 표시와 득점
game_over = False
score = 0

# 게임 상태
STATE_START = 0
STATE_PLAYING = 1
state = STATE_START

# 음식 그림 불러오기 및 크기 설정
food_size = 30
food_image = pygame.image.load("apple.png")
food_image = pygame.transform.scale(food_image, (food_size, food_size))

# 음식 위치 초기화
foodx = random.randint(1, 60)
foody = random.randint(1, 40)
arr[foodx][foody] = -1

while True:
    if state == STATE_START:
        # 시작 인터페이스
        screen.blit(background_surface, (0, 0))
        font = pygame.font.Font(None, 36)
        text = font.render("Snake Game", True, color_white)
        text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
        screen.blit(text, text_rect)
        pygame.display.flip()

        # 스페이스바를 눌러 게임을 시작하다
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                state = STATE_PLAYING

    elif state == STATE_PLAYING:
        screen.blit(background_surface, (0, 0))
        time.sleep(0.1)
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and way != 2:
                    way = 1
                if event.key == pygame.K_LEFT and way != 1:
                    way = 2
                if event.key == pygame.K_UP and way != 4:
                    way = 3
                if event.key == pygame.K_DOWN and way != 3:
                    way = 4

       # 방향에 따라 뱀의 위치를 갱신하다
        if way == 1:
            x += 1
        if way == 2:
            x -= 1
        if way == 3:
            y -= 1
        if way == 4:
            y += 1

        # 뱀이 경계를 벗어나거나 자신에게 닿았는지 검사하다.
        if x >70 or y >60 or x < 1 or y < 1 or arr[x][y] > 0:
            game_over = True

        if game_over:
            font = pygame.font.Font(None, 36)
            text = font.render("Game Over", True, color_red)
            text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
            screen.blit(text, text_rect)

            # 득점 보이기
            score_text = font.render(f"Score: {score}", True, color_black)
            score_rect = score_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 40))
            screen.blit(score_text, score_rect)

            pygame.display.flip()
            time.sleep(10)
            sys.exit()

        # 뱀 위치 정보 업데이트
        arr[x][y] = snake_lon

        # 뱀이 먹이를 먹었는지 검사하다
        if x == foodx and y == foody:
            snake_lon += 1
            while True:
                foodx = random.randint(1, 60)
                foody = random.randint(1, 40)
                if arr[foodx][foody] == 0:
                    break
            arr[foodx][foody] = -1
            score += 1
            # 먹은 음식의 음향을 틀다
            eat_sound.play()

        # 뱀의 몸과 먹이를 그리다
        for a, b in enumerate(arr, 1):
            for c, d in enumerate(b, 1):
                if d > 0:
                    # 뱀의 몸을 그리다
                    arr[a - 1][c - 1] = arr[a - 1][c - 1] - 1
                    pygame.draw.rect(screen, color_pink, ((a - 1) * 10, (c - 1) * 10, 10, 10))

        # 음식 그리기
        food_rect = food_image.get_rect()
        food_rect.topleft = ((foodx - 1) * 10, (foody - 1) * 10)
        screen.blit(pygame.transform.scale(food_image, (food_rect.width, food_rect.height)), food_rect)

        # 스코어를 그리다
        font = pygame.font.Font(None, 24)
        score_text = font.render(f"Score: {score}", True, color_black)
        screen.blit(score_text, (10, 10))

        pygame.display.update()
