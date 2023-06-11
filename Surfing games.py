# 导入pygame模块
import pygame

# 初始化pygame
pygame.init()

# 设置窗口大小和标题
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Edge Surf Game")

# 加载图片资源
background = pygame.image.load("background.png")
surfer = pygame.image.load("surfer.png")
obstacle = pygame.image.load("obstacle.png")

# 设置图片位置和速度
background_x = 0
background_speed = -5
surfer_x = 100
surfer_y = 300
surfer_speed = 0
obstacle_x = 800
obstacle_y = 300
obstacle_speed = -10

# 设置游戏状态和分数
running = True
game_over = False
score = 0

# 设置字体和颜色
font = pygame.font.SysFont("arial", 32)
white = (255, 255, 255)
black = (0, 0, 0)

# 主循环
while running:

    # 处理事件
    for event in pygame.event.get():

        # 如果点击关闭按钮，退出游戏
        if event.type == pygame.QUIT:
            running = False

        # 如果按下上下箭头键，让冲浪者上下移动
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and surfer_y > 100:
                surfer_speed = -10
            if event.key == pygame.K_DOWN and surfer_y < 500:
                surfer_speed = 10

        # 如果松开上下箭头键，让冲浪者停止移动
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                surfer_speed = 0

    # 更新图片位置
    background_x += background_speed
    surfer_y += surfer_speed
    obstacle_x += obstacle_speed

    # 如果背景图片移出屏幕，让它回到初始位置
    if background_x <= -800:
        background_x = 0

    # 如果障碍物移出屏幕，让它回到初始位置，并增加分数和速度
    if obstacle_x <= -100:
        obstacle_x = 800
        score += 1
        obstacle_speed -= 1

    # 检测冲浪者和障碍物是否碰撞，如果是，游戏结束
    if surfer_x + surfer.get_width() > obstacle_x and surfer_y + surfer.get_height() > obstacle_y:
        game_over = True

    # 绘制背景图片
    screen.blit(background, (background_x, 0))
    screen.blit(background, (background_x + 800, 0))

    # 绘制冲浪者和障碍物图片
    screen.blit(surfer, (surfer_x, surfer_y))
    screen.blit(obstacle, (obstacle_x, obstacle_y))

    # 绘制分数和游戏结束提示文字
    score_text = font.render("Score: " + str(score), True, white)
    screen.blit(score_text, (10, 10))
    if game_over:
        game_over_text = font.render("Game Over", True, black)
        screen.blit(game_over_text, (350, 250))

    # 更新屏幕显示
    pygame.display.flip()
