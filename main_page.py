import pygame
import sys
import os
from pygame.locals import *
import subprocess
import play_board
import pygame.mixer

# 初始化pygame
pygame.init()
pygame.mixer.init()
# 定义窗口尺寸
window_size = (1280, 800)

# 创建窗口
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("World Conquest Game")

# 加载音乐文件并设置循环播放
background_music_path = os.path.join('music', 'background_music.wav')
pygame.mixer.music.load(background_music_path)
pygame.mixer.music.set_volume(0.5)  # 可选：设置音量（0.0到1.0之间的值）
pygame.mixer.music.play(-1)  # -1 表示循环播放

# 加载图片并确保支持透明度调整
def load_image_with_alpha(path):
    return pygame.image.load(path).convert_alpha()

current_directory = os.path.dirname(os.path.realpath(__name__))
image_directory = os.path.join(current_directory, 'image')
cover_image_path = os.path.join(image_directory, 'cover_image.png')
start_button_path = os.path.join(image_directory, 'start_button.png')
confirm_button_path = os.path.join(image_directory, 'confirm_button.png')
cover_image = load_image_with_alpha(cover_image_path)
start_button = load_image_with_alpha(start_button_path)
confirm_button = load_image_with_alpha(confirm_button_path)
cover_image = pygame.transform.scale(cover_image, (int(cover_image.get_width() * 1.4), int(cover_image.get_height() * 1.5)))

# 计算放大后的 cover_image 居中显示的位置
cover_image_rect = cover_image.get_rect()
cover_image_rect.center = (window_size[0] // 2, window_size[1] // 2)

# 定义页面状态
current_page = "main"
show_notice_board = False
fade_out = False
alpha = 255

# 加入一个变量，用于标记是否点击了 notice_board 图层
clicked_notice_board = False

# 新设置全局变量 player_num
player_num = None

# 获取按钮的 rect 对象
start_button_rect = start_button.get_rect(center=(window_size[0] // 2 + 500, window_size[1] // 2 + 150))
confirm_button_rect = confirm_button.get_rect(center=(window_size[0] // 2, window_size[1] // 2 + 150))
# 调整 confirm_button 的位置
confirm_button_rect.y -= 50  # 你可以根据需要调整这个值，负值表示往上移动
confirm_button_rect.x += 50  # 你可以根据需要调整这个值，正值表示往右移动
# 定义输入框的状态
input_text = ""
input_rect = pygame.Rect(window_size[0] // 2 - 100, window_size[1] // 2 - 25, 200, 50)
font = pygame.font.Font(None, 32)
input_color = (255, 255, 255)
input_active_color = (255, 0, 0)
input_box_active = False

# 主循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # 处理鼠标点击事件
        if event.type == pygame.MOUSEBUTTONDOWN:
            # 检查是否点击了 start_button
            if start_button_rect.collidepoint(event.pos):
                show_notice_board = True
                input_text = ""
                input_box_active = True
                # 检查是否点击了 confirm_button
            elif confirm_button_rect.collidepoint(event.pos) and show_notice_board:
                if input_text.strip():  # Check if the input is not empty (ignoring leading/trailing whitespaces)
                    player_num = input_text
                    print("Player Number changed:", player_num, "from Confirm Button")
                    input_text = ""
                    show_notice_board = False  # 关闭通知板
                    fade_out = True  # 开始淡出
                else:
                    print("Input Box is empty. Please enter a value.")
            # 检查是否点击了输入框
            elif input_rect.collidepoint(event.pos):
                print("Input Box Clicked")
                input_box_active = True
            else:
                input_box_active = False

        # 处理输入框事件
        if input_box_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    input_box_active = False
                    if input_text.strip():  # 确保输入不为空
                        player_num = input_text
                        print("Player Number changed:", player_num, "from Enter key")
                        input_text = ""
                        show_notice_board = False
                        fade_out = True  # 开始淡出
                    else:
                        print("Input Box is empty. Please enter a value.")
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    # 添加对输入字符的支持，并限制文本长度为1
                    if event.unicode.isdigit() and 1 <= int(event.unicode) <= 5 and len(input_text) < 1:
                        input_text += event.unicode

    screen.fill((0, 0, 0))

    # 渲染 cover 图片和 start 按钮
    if current_page == "main":
        screen.blit(cover_image, (0, 0))
        screen.blit(start_button, start_button_rect.topleft)

    # 在点击 start 后弹出一个图层
    if show_notice_board:
        # 渲染 notice_board 图层
        notice_board_path = os.path.join(image_directory, 'notice_board.png')
        notice_board = load_image_with_alpha(notice_board_path)
        notice_board_rect = notice_board.get_rect(center=(window_size[0] // 2, window_size[1] // 2))
        screen.blit(notice_board, notice_board_rect.topleft)

        # 更新输入框的位置
        input_rect.center = (notice_board_rect.centerx - 100, notice_board_rect.centery + 80)

        # 渲染输入框
        pygame.draw.rect(screen, (0, 0, 0) if input_box_active else input_color, input_rect, 2)
        text_surface = font.render(input_text, True, (255, 255, 255))
        input_rect.w = 40
        screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))

    # 渲染 confirm_button
    if show_notice_board:
        screen.blit(confirm_button, confirm_button_rect.topleft)

        # 如果点击了 notice_board 图层，则开始淡出
    if clicked_notice_board and fade_out:
        alpha -= 5  # 逐渐减少透明度
        if alpha < 0:
            alpha = 0
        cover_image.set_alpha(alpha)
        start_button.set_alpha(alpha)
        confirm_button.set_alpha(alpha)  # 添加 confirm_button 的透明度调整
    # 如果开始淡出，则逐渐减少透明度
    if fade_out:
        alpha -= 5  # 逐渐减少透明度
        if alpha < 0:
            alpha = 0
        cover_image.set_alpha(alpha)
        start_button.set_alpha(alpha)
        confirm_button.set_alpha(alpha)  # 添加 confirm_button 的透明度调整
    # 当淡出完成时
    if fade_out and alpha == 0:
        # 在这里添加你希望执行的 Python 文件的路径
        other_python_file_path = 'G:\\小程序自学\\day_1\\代码\\工具小程序-副本\\world conquest\\play_board.py'

        # 使用 subprocess 模块执行另一个 Python 文件
        subprocess.run(['python', other_python_file_path,str(player_num)])
        # 在淡出完成时调用 render_play_board 函数
        play_board.render_play_board(screen,player_num)

    pygame.display.flip()
    pygame.time.delay(10)
