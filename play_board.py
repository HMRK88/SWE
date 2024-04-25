import os
import random
import sys
import time

import pygame
from pygame.locals import *

pygame.font.init()  # 初始化字体模块
# 全局变量
concentrate_on = None
enable_is_mouse_over = True
enable_handle_mouse_click = True
enable_mouse_position_detection = True
brightness_value = 0  # 当前亮度值
brightness_increment = 5  # 亮度每次改变的量
increasing_brightness = True  # 亮度增加还是减少
attack_board_visible = False  # 初始时不显示attack_board图层
selected_layer_within_180_pixels = None
font = pygame.font.SysFont(None, 24)  # 创建一个字体对象，None表示默认字体，24是字体大小
text_display_switch = True
text_content = 21
army_Brazil = 1
army_Alaska = 1
army_Alberta = 1
army_Ontario = 1
army_Northwest_Territory = 1
army_Greenland = 1
army_Argentina = 1
army_Peru = 1
army_Central_America = 1
army_Eastern_United_States = 1
army_Western_United_States = 1
army_Egypt = 1
army_North_Africa = 1
army_East_Africa = 1
army_Congo = 1
army_South_Africa = 1
army_Madagascar = 1
army_Eastern_Australia = 1
army_Western_Australia = 1
army_New_Guinea = 1
army_Indonesia = 1
army_Iceland = 1
army_Northern_Europe = 1
army_Great_Britain = 1
army_Southern_Europe = 1
army_Western_Europe = 1
army_Ukraine = 1
army_Scandinovia = 1
army_Ural = 1
army_Siberia = 1
army_Middle_East = 1
army_Afghanistan = 1
army_India = 1
army_China = 1
army_Irkutsk = 1
army_Japan = 1
army_Yakutsk = 1
army_Kamchatka = 1
army_Mongolia = 1
army_Siam = 1
army_Venezula = 1
army_Quebec = 1
# 定义按钮的位置和尺寸
rolling_button_x = 400
rolling_button_y = 500
rolling_button_width = 100
rolling_button_height = 50
font = pygame.font.SysFont(None, 24)
random.seed()
show_point_1 = False  # 控制point_1显示的开关
final_point_layer_1 = None  # 存储最终的点数图层名称
final_point_layer_2 = None
final_point_layer_3 = None
final_point_layer_4 = None
render_reinforcement = True
render_red_circle_2 = True
is_rolling_button_rendered = False
player_1 = []
player_2 = []
player_3 = []
player_4 = []
player_5 = []
player_6 = []
not_1_for_player_2 = []
not_1_for_player_3 = []
not_1_for_player_4 = []
not_1_for_player_5 = []
not_1_for_player_6 = []
dice_winner_1 = None
dice_winner_2 = None
show_explosion_1 = False
show_explosion_2 = False
show_explosion_3 = False
show_explosion_4 = False
formatted_concentrate_on_click = None
formatted_selected_layer_click = None
render_attack_completed = False
render_Reinforce_Brighter = True
render_Attack_Brighter = False
render_Fortify_Brighter = False
render_move_army_number = False
render_Fortification_completed = False
concentrate_on_leave = None
selected_leave = None
render_round = False
render_round_num = 15
random_choose_1 = None
random_choose_2 = None
machine_each_round = 20
main_player_adding_army = 5
render_ending = False
none_player = []
playing_result = None
loser = None
is_none_player_updated = False
attack_auto_rolling = False
render_risk_bag = True
render_risk_card_board = False
player_1_cards = []
infantry_card = False
cavalry_card = False
artillery_card = False
wild_card = False
update_player_1 = []
adding_times = 0
cavalry_card_num = 0
wild_card_num = 0
artillery_card_num = 0
infantry_card_num = 0
total_adding = 0
choose_artillery = 0
choose_cavalry = 0
choose_wild = 0
choose_infantry = 0
using_cards = []
risk_adding_army = 0
pygame.mixer.init()
sound_effect_playing = False
# 定义地区数据字典
area_data = {
    "area_Alaska": {"position": (60, 113), "army": 1},
    "area_Alberta": {"position": (130, 157), "army": 1},
    "area_Ontario": {"position": (200, 149), "army": 1},
    "area_Northwest_Territory": {"position": (165, 110), "army": 1},
    "area_Greenland": {"position": (380, 70), "army": 1},
    "area_Argentina": {"position": (280, 520), "army": 1},
    "area_Peru": {"position": (230, 440), "army": 1},
    "area_Central_America": {"position": (120, 265), "army": 1},
    "area_Eastern_United_States": {"position": (200, 190), "army": 1},
    "area_Quebec": {"position": (269, 139), "army": 1},
    "area_Western_United_States": {"position": (120, 195), "army": 1},
    "area_Venezula": {"position": (250, 352), "army": 1},
    "area_Brazil": {"position": (290, 400), "army": 1},
    "area_Egypt": {"position": (565, 279), "army": 1},
    "area_North_Africa": {"position": (450, 260), "army": 1},
    "area_East_Africa": {"position": (620, 380), "army": 1},
    "area_Congo": {"position": (555, 430), "army": 1},
    "area_South_Africa": {"position": (555, 500), "army": 1},
    "area_Madagascar": {"position": (700, 510), "army": 1},
    "area_Eastern_Australia": {"position": (1100, 510), "army": 1},
    "area_Western_Australia": {"position": (1000, 520), "army": 1},
    "area_New_Guinea": {"position": (1080, 390), "army": 1},
    "area_Indonesia": {"position": (930, 390), "army": 1},
    "area_Iceland": {"position": (575, 80), "army": 1},
    "area_Northern_Europe": {"position": (620, 160), "army": 1},
    "area_Great_Britain": {"position": (530, 120), "army": 1},
    "area_Southern_Europe": {"position": (630, 205), "army": 1},
    "area_Western_Europe": {"position": (568, 198), "army": 1},
    "area_Ukraine": {"position": (740, 10), "army": 1},
    "area_Scandinovia": {"position": (600, 90), "army": 1},
    "area_Ural": {"position": (782, 115), "army": 1},
    "area_Siberia": {"position": (900, 120), "army": 1},
    "area_Middle_East": {"position": (720, 290), "army": 1},
    "area_Afghanistan": {"position": (770, 220), "army": 1},
    "area_India": {"position": (840, 290), "army": 1},
    "area_China": {"position": (880, 230), "army": 1},
    "area_Irkutsk": {"position": (970, 130), "army": 1},
    "area_Japan": {"position": (1180, 200), "army": 1},
    "area_Yakutsk": {"position": (970, 80), "army": 1},
    "area_Kamchatka": {"position": (1040, 95), "army": 1},
    "area_Mongolia": {"position": (970, 200), "army": 1},
    "area_Siam": {"position": (1080, 300), "army": 1}
}


# 定义后面的增加部队
def adding_army():
    global adding_times, total_adding
    if adding_times == 1:
        total_adding = 4
    if adding_times == 2:
        total_adding = 6
    if adding_times == 3:
        total_adding = 8
    if adding_times == 4:
        total_adding = 10
    if adding_times == 5:
        total_adding = 12
    if adding_times == 6:
        total_adding = 15
    if adding_times >= 7:
        total_adding = 20


# 风险卡的点击区域设定
def handle_risk_bag_click(mouse_pos):
    global risk_bag_image_rect
    if risk_bag_image_rect.collidepoint(mouse_pos):
        return True
    return False


# 渲染移动军队按钮
def render_move_army_buttons(screen):
    # 定义按钮的基本属性
    button_width = 120
    button_height = 50
    button_color = (0, 255, 0)  # 绿色
    text_color = (255, 255, 255)  # 白色文本
    font = pygame.font.Font(None, 36)  # 定义字体和大小

    # 定义cancel按钮的位置
    cancel_button_position = (550, 500)  # 根据需要调整位置
    cancel_button_rect = pygame.Rect(cancel_button_position[0], cancel_button_position[1], button_width, button_height)
    pygame.draw.rect(screen, button_color, cancel_button_rect)
    cancel_text = font.render("Cancel", True, text_color)
    screen.blit(cancel_text, (cancel_button_position[0] + 10, cancel_button_position[1] + 10))  # 调整文本位置以居中

    # 定义confirm按钮的位置
    confirm_button_position = (400, 500)  # 根据需要调整位置
    confirm_button_rect = pygame.Rect(confirm_button_position[0], confirm_button_position[1], button_width,
                                      button_height)
    pygame.draw.rect(screen, button_color, confirm_button_rect)
    confirm_text = font.render("Confirm", True, text_color)
    screen.blit(confirm_text, (confirm_button_position[0] + 10, confirm_button_position[1] + 10))  # 调整文本位置以居中


# move_army_number界面的取消按钮
def handle_cancel_button_click(mouse_pos):
    global render_move_army_number
    # 定义cancel按钮的位置和尺寸
    cancel_button_x = 550
    cancel_button_y = 500
    button_width = 120
    button_height = 50
    # 创建一个矩形来代表cancel按钮的区域
    cancel_button_rect = pygame.Rect(cancel_button_x, cancel_button_y, button_width, button_height)
    # 检查鼠标点击的位置是否在cancel按钮的区域内
    if cancel_button_rect.collidepoint(mouse_pos):
        # 如果在cancel按钮区域内，则设置render_move_army_number为False
        render_move_army_number = False


# move_army_number界面的确认按钮
def handle_confirm_button_click(mouse_pos):
    global concentrate_on, selected_layer_within_180_pixels, concentrate_on_leave, selected_leave
    # 定义confirm按钮的位置和尺寸
    confirm_button_x = 400
    confirm_button_y = 500
    button_width = 120
    button_height = 50
    # 创建一个矩形来代表confirm按钮的区域
    confirm_button_rect = pygame.Rect(confirm_button_x, confirm_button_y, button_width, button_height)
    # 检查鼠标点击的位置是否在confirm按钮的区域内
    if confirm_button_rect.collidepoint(mouse_pos):
        # 格式化concentrate_on和selected_layer_within_180_pixels
        formatted_concentrate_on = "army_" + concentrate_on.split("area_")[-1] if concentrate_on else None
        formatted_selected_layer = "army_" + selected_layer_within_180_pixels.split("area_")[
            -1] if selected_layer_within_180_pixels else None

        # 更新全局变量中对应的军队数量
        if formatted_concentrate_on and formatted_concentrate_on in globals():
            globals()[formatted_concentrate_on] = concentrate_on_leave if concentrate_on_leave is not None else \
                globals()[formatted_concentrate_on]

        if formatted_selected_layer and formatted_selected_layer in globals():
            globals()[formatted_selected_layer] = selected_leave if selected_leave is not None else globals()[
                formatted_selected_layer]


# 对于其他玩家的军队数量+1，对于player_2_army_random列表
def update_global_army_values_2(player_2_army_random):
    for army_name in player_2_army_random:
        if army_name in globals():
            globals()[army_name] += 1
            attack_board_visible = True
        else:
            print(f"Warning: {army_name} does not exist as a global variable.")


def update_global_army_values_3(player_3_army_random):
    for army_name in player_3_army_random:
        if army_name in globals():
            globals()[army_name] += 1
            attack_board_visible = True
        else:
            print(f"Warning: {army_name} does not exist as a global variable.")


def update_global_army_values_4(player_4_army_random):
    for army_name in player_4_army_random:
        if army_name in globals():
            globals()[army_name] += 1
            attack_board_visible = True
        else:
            print(f"Warning: {army_name} does not exist as a global variable.")


def update_global_army_values_5(player_5_army_random):
    for army_name in player_5_army_random:
        if army_name in globals():
            globals()[army_name] += 1
            attack_board_visible = True
        else:
            print(f"Warning: {army_name} does not exist as a global variable.")


def update_global_army_values_6(player_6_army_random):
    for army_name in player_6_army_random:
        if army_name in globals():
            globals()[army_name] += 1
            attack_board_visible = True
        else:
            print(f"Warning: {army_name} does not exist as a global variable.")


# 格式化处理开始阶段的其他player的图层名字，从area改成army，方便进行全局变量的修改
def format_and_store_player_2_layers(player_2):
    global render_round_num, machine_each_round  # 引入全局变量
    player_2_army = []  # 新列表用于存储格式化后的图层名
    for layer_name in player_2:
        # 去除前缀"area_"并添加前缀"army_"
        formatted_name = "army_" + layer_name.split("area_")[-1]
        player_2_army.append(formatted_name)
    print(f"player_2_army:{player_2_army}")

    # 确保列表不为空
    if player_2_army:
        # 根据render_round_num的值决定k的值
        k_value = 21 if render_round_num == 15 else machine_each_round
        # 从player_2_army中随机抽取k_value个图层，允许重复
        player_2_army_random = random.choices(player_2_army, k=k_value)
        print(f"player_2_army_random:{player_2_army_random}")
        update_global_army_values_2(player_2_army_random)
        return player_2_army_random
    else:
        print("player_2_army is empty, cannot perform random.choices()")
        player_2_army_random = []


def format_and_store_player_3_layers(player_3):
    global render_round_num, machine_each_round  # 引入全局变量
    player_3_army = []  # 新列表用于存储格式化后的图层名
    for layer_name in player_3:
        # 去除前缀"area_"并添加前缀"army_"
        formatted_name = "army_" + layer_name.split("area_")[-1]
        player_3_army.append(formatted_name)
    print(f"player_3_army:{player_3_army}")

    # 确保列表不为空
    if player_3_army:
        # 根据render_round_num的值决定k的值
        k_value = 21 if render_round_num == 15 else machine_each_round
        # 从player_3_army中随机抽取k_value个图层，允许重复
        player_3_army_random = random.choices(player_3_army, k=k_value)
        print(f"player_3_army_random:{player_3_army_random}")
        update_global_army_values_3(player_3_army_random)
        return player_3_army_random
    else:
        print("player_3_army is empty, cannot perform random.choices()")
        player_3_army_random = []


def format_and_store_player_4_layers(player_4):
    global render_round_num, machine_each_round  # 引入全局变量
    player_4_army = []  # 新列表用于存储格式化后的图层名
    for layer_name in player_4:
        # 去除前缀"area_"并添加前缀"army_"
        formatted_name = "army_" + layer_name.split("area_")[-1]
        player_4_army.append(formatted_name)
    print(f"player_4_army:{player_4_army}")

    # 确保列表不为空
    if player_4_army:
        # 根据render_round_num的值决定k的值
        k_value = 21 if render_round_num == 15 else machine_each_round
        # 从player_4_army中随机抽取k_value个图层，允许重复
        player_4_army_random = random.choices(player_4_army, k=k_value)
        print(f"player_4_army_random:{player_4_army_random}")
        update_global_army_values_4(player_4_army_random)
        return player_4_army_random
    else:
        print("player_4_army is empty, cannot perform random.choices()")
        player_4_army_random = []


def format_and_store_player_5_layers(player_5):
    global render_round_num, machine_each_round  # 引入全局变量
    player_5_army = []  # 新列表用于存储格式化后的图层名
    for layer_name in player_5:
        # 去除前缀"area_"并添加前缀"army_"
        formatted_name = "army_" + layer_name.split("area_")[-1]
        player_5_army.append(formatted_name)
    print(f"player_5_army:{player_5_army}")

    # 确保列表不为空
    if player_5_army:
        # 根据render_round_num的值决定k的值
        k_value = 21 if render_round_num == 15 else machine_each_round
        # 从player_5_army中随机抽取k_value个图层，允许重复
        player_5_army_random = random.choices(player_5_army, k=k_value)
        print(f"player_5_army_random:{player_5_army_random}")
        update_global_army_values_5(player_5_army_random)
        return player_5_army_random
    else:
        print("player_5_army is empty, cannot perform random.choices()")
        player_5_army_random = []


def format_and_store_player_6_layers(player_6):
    global render_round_num, machine_each_round  # 引入全局变量
    player_6_army = []  # 新列表用于存储格式化后的图层名
    for layer_name in player_6:
        # 去除前缀"area_"并添加前缀"army_"
        formatted_name = "army_" + layer_name.split("area_")[-1]
        player_6_army.append(formatted_name)
    print(f"player_6_army:{player_6_army}")

    # 确保列表不为空
    if player_6_army:
        # 根据render_round_num的值决定k的值
        k_value = 21 if render_round_num == 15 else machine_each_round
        # 从player_6_army中随机抽取k_value个图层，允许重复
        player_6_army_random = random.choices(player_6_army, k=k_value)
        print(f"player_6_army_random:{player_6_army_random}")
        update_global_army_values_6(player_6_army_random)
        return player_6_army_random
    else:
        print("player_6_army is empty, cannot perform random.choices()")
        player_6_army_random = []


# 渲染21的数字
def render_text(screen, text, position, font_size=36, color=(255, 255, 255), display=True):
    if display:
        font = pygame.font.Font(None, font_size)  # 创建字体对象
        text_surface = font.render(str(text), True, color)  # 创建文本表面对象
        screen.blit(text_surface, position)  # 在指定位置渲染文本


def update_text_content():
    global player_1, text_content, concentrate_on, army_Brazil, army_Alaska, army_Alberta, army_Ontario, army_Northwest_Territory, army_Greenland, army_Quebec, army_Venezula
    global army_Argentina, army_Peru, army_Central_America, army_Eastern_United_States, army_Western_United_States, army_Egypt, army_North_Africa
    global army_East_Africa, army_Congo, army_South_Africa, army_Madagascar, army_Eastern_Australia, army_Western_Australia, army_New_Guinea, army_Indonesia
    global army_Iceland, army_Northern_Europe, army_Great_Britain, army_Southern_Europe, army_Western_Europe, army_Ukraine, army_Scandinovia, army_Ural
    global army_Siberia, army_Middle_East, army_Afghanistan, army_India, army_China, army_Irkutsk, army_Japan, army_Yakutsk, army_Kamchatka, army_Mongolia, army_Siam
    global render_reinforcement, render_red_circle_2, text_display_switch, render_attack_completed, render_Reinforce_Brighter, render_Attack_Brighter
    if concentrate_on is not None and concentrate_on in player_1 and text_content > 0:
        text_content -= 1
        if text_content == 0:
            render_reinforcement = False  # 当 text_content 为 0 时，设置 render_reinforcement 为 False
            render_red_circle_2 = False
            text_display_switch = False
            render_attack_completed = True
            player_2_army = format_and_store_player_2_layers(player_2)

            player_3_army = format_and_store_player_3_layers(player_3)

            player_4_army = format_and_store_player_4_layers(player_4)

            player_5_army = format_and_store_player_5_layers(player_5)

            player_6_army = format_and_store_player_6_layers(player_6)
            render_Reinforce_Brighter = False
            render_Attack_Brighter = True
        elif concentrate_on == "area_Brazil":  # 假设巴西图层的名称是 "area_Brazil"
            army_Brazil += 1
        elif concentrate_on == "area_Alaska":
            army_Alaska += 1
        elif concentrate_on == "area_Alberta":
            army_Alberta += 1
        elif concentrate_on == "area_Ontario":
            army_Ontario += 1
        elif concentrate_on == "area_Northwest_Territory":
            army_Northwest_Territory += 1
        elif concentrate_on == "area_Greenland":
            army_Greenland += 1
        elif concentrate_on == "area_Argentina":
            army_Argentina += 1
        elif concentrate_on == "area_Peru":
            army_Peru += 1
        elif concentrate_on == "area_Central_America":
            army_Central_America += 1
        elif concentrate_on == "area_Eastern_United_States":
            army_Eastern_United_States += 1
        elif concentrate_on == "area_Western_United_States":
            army_Western_United_States += 1
        elif concentrate_on == "area_Egypt":
            army_Egypt += 1
        elif concentrate_on == "area_North_Africa":
            army_North_Africa += 1
        elif concentrate_on == "area_East_Africa":
            army_East_Africa += 1
        elif concentrate_on == "area_Congo":
            army_Congo += 1
        elif concentrate_on == "area_South_Africa":
            army_South_Africa += 1
        elif concentrate_on == "area_Madagascar":
            army_Madagascar += 1
        elif concentrate_on == "area_Eastern_Australia":
            army_Eastern_Australia += 1
        elif concentrate_on == "area_Western_Australia":
            army_Western_Australia += 1
        elif concentrate_on == "area_New_Guinea":
            army_New_Guinea += 1
        elif concentrate_on == "area_Indonesia":
            army_Indonesia += 1
        elif concentrate_on == "area_Iceland":
            army_Iceland += 1
        elif concentrate_on == "area_Northern_Europe":
            army_Northern_Europe += 1
        elif concentrate_on == "area_Great_Britain":
            army_Great_Britain += 1
        elif concentrate_on == "area_Southern_Europe":
            army_Southern_Europe += 1
        elif concentrate_on == "area_Western_Europe":
            army_Western_Europe += 1
        elif concentrate_on == "area_Ukraine":
            army_Ukraine += 1
        elif concentrate_on == "area_Scandinovia":
            army_Scandinovia += 1
        elif concentrate_on == "area_Ural":
            army_Ural += 1
        elif concentrate_on == "area_Siberia":
            army_Siberia += 1
        elif concentrate_on == "area_Middle_East":
            army_Middle_East += 1
        elif concentrate_on == "area_Afghanistan":
            army_Afghanistan += 1
        elif concentrate_on == "area_India":
            army_India += 1
        elif concentrate_on == "area_China":
            army_China += 1
        elif concentrate_on == "area_Irkutsk":
            army_Irkutsk += 1
        elif concentrate_on == "area_Japan":
            army_Japan += 1
        elif concentrate_on == "area_Yakutsk":
            army_Yakutsk += 1
        elif concentrate_on == "area_Kamchatka":
            army_Kamchatka += 1
        elif concentrate_on == "area_Mongolia":
            army_Mongolia += 1
        elif concentrate_on == "area_Siam":
            army_Siam += 1
        elif concentrate_on == "area_Quebec":
            army_Quebec += 1
        elif concentrate_on == "area_Venezula":
            army_Venezula += 1


def load_and_adjust_alpha(image_path, alpha):
    # 加载图像
    image = pygame.image.load(image_path)
    # 转换图像以支持透明度
    image = image.convert_alpha()
    # 调整图像的透明度
    image.set_alpha(alpha)
    return image


def load_text_positions_and_numbers_from_dict():
    text_positions_and_numbers = []
    for area_name, info in area_data.items():
        position = info["position"]
        army = info["army"]
        # 假设我们想要对位置进行同样的调整
        adjusted_position = (position[0] + 15, position[1] + 20)
        text_positions_and_numbers.append((area_name, adjusted_position, str(army)))
    return text_positions_and_numbers


def render_text_positions(screen, file_path):
    text_positions_and_numbers = load_text_positions_and_numbers(file_path)
    font = pygame.font.Font(None, 24)  # 创建字体对象
    for area_name, adjusted_position, number in text_positions_and_numbers:
        text_surface = font.render(f"{area_name}: {number}", True, (255, 255, 255))  # 创建文本表面对象
        screen.blit(text_surface, adjusted_position)
    # cancel_button的点击事件


def check_cancel_button_clicked(mouse_pos):
    global show_explosion_1, show_explosion_2, show_explosion_3, show_explosion_4, attack_auto_rolling
    cancel_button_x = rolling_button_x + rolling_button_width + 20 + rolling_button_width + 20  # 根据之前的计算方式
    cancel_button_y = rolling_button_y
    button_rect = pygame.Rect(cancel_button_x, cancel_button_y, rolling_button_width, rolling_button_height)
    if button_rect.collidepoint(mouse_pos):
        # 当取消按钮被点击时，隐藏所有爆炸效果
        show_explosion_1 = False
        show_explosion_2 = False
        show_explosion_3 = False
        show_explosion_4 = False
        is_rolling_button_rendered = False

        return True  # 表示取消按钮被点击
    return False  # 表示取消按钮未被点击


def check_rolling_button_clicked(mouse_pos):
    global show_point_1, show_explosion_1, show_explosion_2, show_explosion_3, show_explosion_4
    global concentrate_on, selected_layer_within_180_pixels, formatted_concentrate_on_click, formatted_selected_layer_click
    global final_point_layer_3, final_point_layer_4
    show_point_1 = True
    button_rect = pygame.Rect(rolling_button_x, rolling_button_y, rolling_button_width, rolling_button_height)
    if button_rect.collidepoint(mouse_pos):
        # 切换爆炸效果的显示状态
        show_explosion_1 = False
        show_explosion_2 = False
        show_explosion_3 = False
        show_explosion_4 = False
        return True
    return False  # 注意这里始终返回False，可能需要根据实际逻辑调整


def check_auto_rolling(mouse_pos):
    global show_point_1, show_explosion_1, show_explosion_2, show_explosion_3, show_explosion_4
    global concentrate_on, selected_layer_within_180_pixels, formatted_concentrate_on_click, formatted_selected_layer_click
    global final_point_layer_3, final_point_layer_4
    show_point_1 = True
    auto_rect = pygame.Rect(rolling_button_x + rolling_button_width + 20, rolling_button_y, rolling_button_width,
                            rolling_button_height)
    if auto_rect.collidepoint(mouse_pos):
        # 切换爆炸效果的显示状态
        show_explosion_1 = False
        show_explosion_2 = False
        show_explosion_3 = False
        show_explosion_4 = False
        return True
    return False


# 在 attack_board 图层上绘制rolling_button并添加文本
def draw_rolling_button(screen):
    global auto_button_x, auto_button_y, rolling_button_width, rolling_button_height, attack_auto_rolling
    # 绘制按钮
    attack_auto_rolling = True
    pygame.draw.rect(screen, (0, 255, 0),
                     (rolling_button_x, rolling_button_y, rolling_button_width, rolling_button_height))
    # 渲染文本
    text_surface = font.render("Rolling", True, (0, 0, 0))  # 黑色文本
    # 获取文本表面的矩形区域
    text_rect = text_surface.get_rect(
        center=(rolling_button_x + rolling_button_width / 2, rolling_button_y + rolling_button_height / 2))
    # 将文本绘制到按钮上
    screen.blit(text_surface, text_rect)
    is_rolling_button_rendered = True

    # 计算Auto按钮的位置，假设按钮间隔为20像素
    auto_button_x = rolling_button_x + rolling_button_width + 20
    auto_button_y = rolling_button_y
    # 绘制Auto按钮
    if attack_auto_rolling:
        pygame.draw.rect(screen, (0, 255, 0),
                         (auto_button_x, auto_button_y, rolling_button_width, rolling_button_height))
        text_surface = font.render("Auto", True, (0, 0, 0))  # 黑色文本
        text_rect = text_surface.get_rect(
            center=(auto_button_x + rolling_button_width / 2, auto_button_y + rolling_button_height / 2))
        screen.blit(text_surface, text_rect)

    # 计算Cancel按钮的位置，继续使用20像素的间隔
    cancel_button_x = auto_button_x + rolling_button_width + 20
    cancel_button_y = rolling_button_y
    # 绘制Cancel按钮
    pygame.draw.rect(screen, (0, 255, 0),
                     (cancel_button_x, cancel_button_y, rolling_button_width, rolling_button_height))
    text_surface = font.render("Cancel", True, (0, 0, 0))  # 黑色文本
    text_rect = text_surface.get_rect(
        center=(cancel_button_x + rolling_button_width / 2, cancel_button_y + rolling_button_height / 2))
    screen.blit(text_surface, text_rect)


def load_forbidden_layers(file_path):
    forbidden_layers = set()
    with open(file_path, 'r') as file:
        for line in file:
            forbidden_layers.add(line.strip())
    return forbidden_layers


def load_image_info_from_file(file_path):
    image_info = {}
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(',', 2)
            if len(parts) == 3:
                layer_name, file_name, position_str = parts
                try:
                    position = eval(position_str)
                    image_info[layer_name] = (file_name, position)
                except Exception as e:
                    print(f"Error parsing position for {layer_name}: {e}")
    return image_info


# 使用新函数加载image_info
current_directory = os.path.dirname(os.path.realpath(__file__))
image_info_file_path = os.path.join(current_directory, 'image_info.txt')
image_info = load_image_info_from_file(image_info_file_path)


def load_dice_images_positions(file_path):
    dice_images_positions = {}

    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(',', 1)
            if len(parts) == 2:
                image_name, position_str = parts
                try:
                    position = eval(position_str)
                    dice_images_positions[image_name] = position
                except Exception as e:
                    print(f"Error parsing position for {image_name}: {e}")
    return dice_images_positions


def render_dice_images_1(screen, image_directory):
    if show_point_1:
        # 定义point_1图层需要渲染的位置
        position = (550, 300)
        # 加载point_1图层的图像
        image_path = os.path.join(image_directory, "point_cover_1.png")
        image = load_image_with_alpha(image_path, scale_factor=0.5)  # 假设你想要缩放到原始大小的50%

        # 在指定的位置渲染图像
        screen.blit(image, position)


def render_dice_images_2(screen, image_directory):
    if show_point_1:
        # 定义point_1图层需要渲染的位置
        position = (650, 300)
        # 加载point_1图层的图像
        image_path = os.path.join(image_directory, "point_cover_2.png")
        image = load_image_with_alpha(image_path, scale_factor=0.5)  # 假设你想要缩放到原始大小的50%

        # 在指定的位置渲染图像
        screen.blit(image, position)


def render_dice_images_3(screen, image_directory):
    if show_point_1:
        # 定义point_1图层需要渲染的位置
        position = (550, 400)
        # 加载point_1图层的图像
        image_path = os.path.join(image_directory, "point_cover_3.png")
        image = load_image_with_alpha(image_path, scale_factor=0.5)  # 假设你想要缩放到原始大小的50%

        # 在指定的位置渲染图像
        screen.blit(image, position)


def render_dice_images_4(screen, image_directory):
    if show_point_1:
        # 定义point_1图层需要渲染的位置
        position = (650, 400)
        # 加载point_1图层的图像
        image_path = os.path.join(image_directory, "point_cover_4.png")
        image = load_image_with_alpha(image_path, scale_factor=0.5)  # 假设你想要缩放到原始大小的50%

        # 在指定的位置渲染图像
        screen.blit(image, position)


def format_layer_name(layer_name):
    # 移除"area_"前缀并将"_"替换为空格
    return layer_name.replace("area_", "").replace("_", " ")


# 小红点位置
def load_layers_from_file(file_path):
    red_circle_positions = {}

    with open(file_path, 'r') as file:
        for line in file:
            # 通过逗号分隔，但只拆分成两部分
            layer_name, rest = line.strip().split(',', 1)
            # 这里将 rest 中的字符串解析为元组
            try:
                x, y = eval(rest)
                red_circle_positions[layer_name] = (int(x), int(y))
            except Exception as e:
                print(f"Error parsing position for {layer_name}: {e}")
    return red_circle_positions


# 调整的是鼠标移动时候的亮度
def adjust_layer_brightness(image_info, layer_name, brightness):
    # 调整图层亮度
    if layer_name in image_info:
        image_name, (file_name, position) = layer_name, image_info[layer_name]
        image_path = os.path.join(image_directory, file_name)
        image = load_image_with_alpha(image_path, scale_factor=1.4)

        bright_image = pygame.Surface(image.get_size(), flags=pygame.SRCALPHA)
        bright_image.fill(brightness)
        bright_image.blit(image, (0, 0), special_flags=pygame.BLEND_RGBA_ADD)
        # 更新图层信息
        image_info[layer_name] = (file_name, position, bright_image)


# 新建一个列表用于存储距离 concentrate_on 的图层 180 个像素范围内的所有图层的名字
layers_within_180_pixels = []


def get_layers_within_radius(center_position, image_info, exclude_layers, concentrate_on, render_Fortify_Brighter,
                             player_1):
    nearby_layers = []
    for image_name, (_, position) in image_info.items():
        if image_name not in exclude_layers:  # 检查图层名是否不在排除的列表中
            distance = pygame.math.Vector2(position[0] - center_position[0], position[1] - center_position[1]).length()
            if 0 <= distance <= 180:
                nearby_layers.append(image_name)
    return nearby_layers


def load_image_with_alpha(path, scale_factor=1.0, alpha=None):
    original_image = pygame.image.load(path).convert_alpha()
    width, height = [int(dim * scale_factor) for dim in original_image.get_size()]
    scaled_image = pygame.transform.scale(original_image, (width, height))

    if alpha is not None:
        new_image = pygame.Surface((width, height), flags=pygame.SRCALPHA)
        new_image.fill((255, 255, 255, alpha))  # 白色背景，透明度为指定值
        new_image.blit(scaled_image, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        return new_image
    else:
        return scaled_image


def is_mouse_over(rect, mouse_pos):
    if enable_is_mouse_over:
        return rect.collidepoint(mouse_pos)
    return False


def handle_mouse_click(image_info, image_directory, mouse_pos, player_1, attack_completed_rect):
    global render_attack_completed, render_round_num, render_round, layers_within_180_pixels, concentrate_on, render_Attack_Brighter, render_Fortify_Brighter, render_Fortification_completed, render_attack_completed, render_move_army_number, enable_is_mouse_over, layers_within_180_pixels, attack_board_visible, enable_handle_mouse_click, text_display_switch, selected_layer_within_180_pixels, render_Fortify_Brighter
    global not_1_for_player_2, not_1_for_player_3, not_1_for_player_4, not_1_for_player_5, not_1_for_player_6, infantry_card_num, cavalry_card_num, artillery_card_num, wild_card_num
    global random_choose_1, random_choose_2, render_Reinforce_Brighter, render_reinforcement, render_red_circle_2, text_content, render_risk_card_board, main_player_adding_army
    global render_ending, none_player, is_none_player_updated, playing_result, player_1_cards, infantry_card, cavalry_card, artillery_card, wild_card, risk_adding_army, using_cards
    global choose_artillery, choose_cavalry, choose_infantry, choose_wild, sound_effect_playing
    target_color = (208, 197, 178)  # 定义目标颜色

    if not enable_handle_mouse_click:
        return
    # 现在，因为Fortification_completed_rect已经被初始化，下面的检查就不会引发错误了
    if render_Fortification_completed and Fortification_completed_rect.collidepoint(
            mouse_pos) and render_Fortify_Brighter == True and render_Fortification_completed == True:
        render_move_army_number = False
        render_Fortify_Brighter = False
        render_Fortification_completed = False
        render_round = True
        render_attack_completed = True
        render_round_num -= 1
        render_Reinforce_Brighter = True
        render_reinforcement = True
        render_red_circle_2 = True
        text_content = main_player_adding_army + risk_adding_army
        text_display_switch = True
        render_risk_card_board = False
        choose_wild = 0
        choose_artillery = 0
        choose_infantry = 0
        choose_cavalry = 0
        infantry_card = False
        cavalry_card = False
        artillery_card = False
        wild_card = False
        # 清空列表以存储新一轮的数据
        not_1_for_player_2.clear()
        not_1_for_player_3.clear()
        not_1_for_player_4.clear()
        not_1_for_player_5.clear()
        not_1_for_player_6.clear()
        using_cards = []
        choose_artillery = 0
        choose_cavalry = 0
        choose_infantry = 0
        choose_wild = 0
        # 遍历player_2到player_6的每个图层
        for player_index in range(2, 7):
            player_var_name = f'player_{player_index}'
            player_layers = globals().get(player_var_name, [])
            for layer in player_layers:
                formatted_layer_name = f'army_{layer.split("_", 1)[1]}'
                army_count = globals().get(formatted_layer_name, 0)
                if army_count != 1:
                    globals()[f'not_1_for_player_{player_index}'].append(layer)  # 存储原始图层名

        # 打印出来not_1_for_player_2一直到player_6的内容
        print("not_1_for_player_2:", not_1_for_player_2)
        print("not_1_for_player_3:", not_1_for_player_3)
        print("not_1_for_player_4:", not_1_for_player_4)
        print("not_1_for_player_5:", not_1_for_player_5)
        print("not_1_for_player_6:", not_1_for_player_6)
        # 遍历每个not_1_for_player_xxx列表
        for player_index in range(2, 7):
            player_var_name = f'not_1_for_player_{player_index}'
            for layer in globals().get(player_var_name, []):
                center_position = image_info[layer][1]  # 获取图层的中心位置
                exclude_layers = ['blank_board']
                nearby_layers = get_layers_within_radius(center_position, image_info, layer, render_Fortify_Brighter,
                                                         player_1, exclude_layers)
                nearby_layer_names = [layer_name for layer_name in nearby_layers]
                random_count = random.randint(1, len(nearby_layer_names))  # 随机选择数量
                random_nearby_layers = random.sample(nearby_layer_names, random_count)  # 随机抽取图层
                for random_layer in random_nearby_layers:
                    random_choose_1 = random.randint(1, 6)
                    random_choose_2 = random.randint(1, 6)
                    globals()['random_choose_1'] = random_choose_1
                    globals()['random_choose_2'] = random_choose_2
                    print(f"随机选择的数字为：{random_choose_1} 和 {random_choose_2}")
                    if random_choose_1 > random_choose_2:
                        formatted_random_layer = f"army_{random_layer.split('_', 1)[1]}"
                        print(f"{layer} 打赢了 {random_layer}")
                        if formatted_random_layer in globals():
                            globals()[formatted_random_layer] -= 1
                            if globals()[formatted_random_layer] <= 0:
                                # 移除被打败的图层名
                                for player_index in range(1, 7):
                                    player_var_name = f'player_{player_index}'
                                    if random_layer in globals()[player_var_name]:
                                        globals()[player_var_name].remove(random_layer)
                                        break
                                # 找到攻击者所在的player_xxx列表，并将被打败的图层名加入
                                for player_index in range(1, 7):
                                    player_var_name = f'player_{player_index}'
                                    if layer in globals()[player_var_name]:
                                        globals()[player_var_name].append(random_layer)
                                        break
                                # 强制将被转移图层的军队数量设置为1
                                globals()[formatted_random_layer] = 1

                    elif random_choose_1 < random_choose_2:
                        formatted_random_layer = f"army_{layer.split('_', 1)[1]}"
                        print(f"{layer} 打 {random_layer}输了")
                        if formatted_random_layer in globals():
                            globals()[formatted_random_layer] -= 1
                            if globals()[formatted_random_layer] <= 0:
                                # 移除被打败的图层名
                                for player_index in range(1, 7):
                                    player_var_name = f'player_{player_index}'
                                    if layer in globals()[player_var_name]:
                                        globals()[player_var_name].remove(layer)
                                        break
                                # 找到防守者所在的player_xxx列表，并将被打败的图层名加入
                                for player_index in range(1, 7):
                                    player_var_name = f'player_{player_index}'
                                    if random_layer in globals()[player_var_name]:
                                        globals()[player_var_name].append(layer)
                                        break
                                globals()[formatted_random_layer] = 1

                    elif random_choose_1 == random_choose_2:
                        print(f"{layer} 打 {random_layer}平了")
                    print(f"player_{player_index} 距离 {layer} 图层 180像素的图层有 {nearby_layer_names}")
                    print(f"然后从 {nearby_layer_names} 中抽取出来这些图层：{random_nearby_layers}")

        if not is_none_player_updated:
            none_player = [f'player_{i}' for i in range(1, 7) if not globals().get(f'player_{i}', [])]
            print("空列表的玩家名字:", none_player)
            is_none_player_updated = True

        # 更新后的逻辑
        remaining_players = [f'player_{i}' for i in range(1, 7) if
                             globals().get(f'player_{i}', []) and f'player_{i}' not in none_player]

        if len(remaining_players) == 0:
            # 如果没有剩余的玩家，不执行任何操作
            pass
        elif len(remaining_players) == 1:
            # 如果只剩下一个玩家
            if 'player_1' in remaining_players:
                # 如果这个玩家是player_1
                playing_result = 'lost'
                render_ending = True
            else:
                # 如果剩下的玩家不是player_1
                playing_result = 'some_one_lost'
                render_ending = True
        else:
            # 如果有多于一个玩家剩余，不需要更新playing_result，因为游戏还在进行中
            pass
        # 不排除none_player的情况下检查player_2到player_6是否都为空列表
        player_lists_empty_without_exclusion = all(
            not globals().get(f'player_{i}', []) for i in range(2, 7))
        if player_lists_empty_without_exclusion:
            playing_result = 'win'
            render_ending = True
        if render_round_num == 0:
            playing_result = 'no_winner'
            render_ending = True

    # 检测鼠标点击是否发生在attack_completed图层的区域内
    if render_attack_completed and attack_completed_rect.collidepoint(mouse_pos) and render_Attack_Brighter == True:
        render_Fortify_Brighter = True
        render_Attack_Brighter = False
        concentrate_on = None
        layers_within_180_pixels = []
        # 在设置render_Fortification_completed = True之前初始化Fortification_completed_rect
        render_Fortification_completed = True
        risk_adding_army = 0
        print("received")

        # 检查update_player_1中的图层是否在player_1列表中
        # 初始化一个标志，用于指示是否已经抽取了卡片
        card_drawn = False
        for layer in update_player_1:
            if layer not in player_1 and not card_drawn:
                # 随机抽取一张risk_card
                risk_card = random.choice(['infantry_card', 'cavalry_card', 'artillery_card', 'wild_card'])
                # 将risk_card添加到player_1_cards列表中
                player_1_cards.append(risk_card)
                print(f"Added {risk_card} to player_1_cards")
                render_risk_card_board = True
                # 更新标志，表示已经抽取了卡片
                card_drawn = True
                # 根据抽取到的卡片名称，将对应的全局变量设置为True
                if risk_card == 'infantry_card':
                    infantry_card = True
                    infantry_card_num += 1  # 增加infantry_card的数量
                elif risk_card == 'cavalry_card':
                    cavalry_card = True
                    cavalry_card_num += 1  # 增加cavalry_card的数量
                elif risk_card == 'artillery_card':
                    artillery_card = True
                    artillery_card_num += 1  # 增加artillery_card的数量
                elif risk_card == 'wild_card':
                    wild_card = True
                    wild_card_num += 1  # 增加wild_card的数量
                # 既然已经抽取了卡片，就不需要再检查其他图层
                break

    # 用于存储与鼠标位置相交的图层及其位置信息
    intersecting_layers = []

    # 如果attack_board_visible或render_move_army_number为true，点击任意图层都将其设置为false
    if attack_board_visible or render_move_army_number or render_ending:
        current_directory = os.path.dirname(os.path.realpath(__file__))
        forbidden_layers_file_path = os.path.join(current_directory, 'forbid_selected.txt')
        forbidden_layers = load_forbidden_layers(forbidden_layers_file_path)

        if concentrate_on in forbidden_layers:
            print(f"{concentrate_on} is forbidden to select.")
            return
    for image_name, (file_name, position) in image_info.items():
        image_path = os.path.join(image_directory, file_name)
        image = load_image_with_alpha(image_path, scale_factor=1.4)

        if image_name != "blank_board":
            image_rect = image.get_rect(topleft=position)
            if image_rect.collidepoint(mouse_pos):
                # 收集所有与鼠标位置相交的图层信息
                intersecting_layers.append((image_name, position, image))

    # 检查是否点击了layers_within_180_pixels中的图层
    attack_success = False
    for layer in reversed(intersecting_layers):  # 从最顶层开始检测
        image_name, position, image = layer
        if concentrate_on is not None and image_name in layers_within_180_pixels:
            attack_success = True
            break  # 找到第一个符合条件的图层后就跳出循环

    if attack_success:
        selected_layer_within_180_pixels = image_name
        if concentrate_on in player_1 or selected_layer_within_180_pixels in player_1:
            if not text_display_switch and render_Fortify_Brighter == False:
                attack_board_visible = True
                enable_is_mouse_over = False
                print("攻击成功，现在将显示attack_board图层。")
            elif not text_display_switch and render_Fortify_Brighter == True:
                render_move_army_number = True
                print("军队移动板打开成功")
            else:
                print("文本显示开关为真，不显示attack_board图层。")

        else:
            print("攻击失败")
        return  # 在这里返回，避免执行后续的逻辑，特别是改变 concentrate_on 的逻辑

    if not attack_success:
        if selected_layer_within_180_pixels in player_1:
            print("移动成功")
    # 如果点击的不是layers_within_180_pixels中的图层，则取消选中
    if concentrate_on is not None:
        print("cancel selected:", concentrate_on)
        concentrate_on = None
        enable_is_mouse_over = True
        layers_within_180_pixels = []

    # 检测鼠标所指的颜色，并决定哪个图层被点击
    for layer in reversed(intersecting_layers):
        image_name, position, image = layer
        local_pos = (mouse_pos[0] - position[0], mouse_pos[1] - position[1])
        try:
            pixel_color = image.get_at(local_pos)
            if pixel_color[:3] == target_color:
                if concentrate_on is None and render_risk_card_board == False:
                    concentrate_on = image_name
                    print("selected:", concentrate_on)
                    enable_is_mouse_over = False

                    # 提取地区名称，并将下划线替换成空格，除了第一个下划线
                    area_name_parts = image_name.split('_', 2)
                    if len(area_name_parts) > 2:
                        area_name = area_name_parts[1] + " " + area_name_parts[2].replace('_', ' ')
                    else:
                        area_name = area_name_parts[1]
                    if not sound_effect_playing:
                        # 构建音频文件的路径
                        audio_directory = os.path.join(os.path.dirname(__file__), 'music')
                        audio_file_path = os.path.join(audio_directory, f"{area_name}.mp3")
                        if os.path.exists(audio_file_path):
                            # 使用Sound对象播放效果音
                            sound_effect = pygame.mixer.Sound(audio_file_path)
                            sound_effect.set_volume(0.5)  # 将音量设置为50%
                            sound_effect_playing = True  # 标记音效正在播放
                            # 寻找一个可用的声道并播放音效
                            channel = pygame.mixer.find_channel()
                            if channel:
                                channel.play(sound_effect)
                                # 设置一个事件，当声道播放完成时触发
                                channel.set_endevent(pygame.USEREVENT)
                            else:
                                print("No available audio channels.")
                                sound_effect_playing = False
                        else:
                            print(f"Audio file for {area_name} not found.")
                    else:
                        print("Sound files are not affected")
                    return
        except IndexError:
            continue


image_info = {}

# 使用新函数加载image_info
current_directory = os.path.dirname(os.path.realpath(__file__))
image_info_file_path = os.path.join(current_directory, 'image_info.txt')
image_info = load_image_info_from_file(image_info_file_path)


def render_play_board(screen, player_num):
    global layers_within_180_pixels, brightness_value, increasing_brightness, update_player_1
    global player_1, player_2, player_3, player_4, player_5, player_6  # 使用global关键字

    print("player_num value:", player_num)
    current_directory = os.path.dirname(os.path.realpath(__file__))
    image_directory = os.path.join(current_directory, 'image')

    player_num = int(player_num)  # 将player_num转换为整数类型
    if player_num == 1:
        # 从所有非 blank_board 图层中随机抽取21个
        available_layers = [layer for layer in image_info.keys() if layer != "blank_board"]
        player_1 = random.sample(available_layers, min(21, len(available_layers)))
        update_player_1 = random.sample(available_layers, min(21, len(available_layers)))
        print("player_1:", player_1)

        # 将剩余的非 blank_board 图层放入玩家2列表
        player_2 = [layer for layer in available_layers if layer not in player_1]
        print("player_2:", player_2)
        # 玩家3为空
        player_3 = []
        player_4 = []
        player_5 = []
        player_6 = []
    elif player_num == 2:
        # 从所有非 blank_board 图层中随机抽取14个
        available_layers = [layer for layer in image_info.keys() if layer != "blank_board"]
        player_1 = random.sample(available_layers, min(14, len(available_layers)))
        update_player_1 = random.sample(available_layers, min(21, len(available_layers)))
        print("player_1:", player_1)

        # 将剩余的非 blank_board 图层放入玩家2列表
        player_2 = random.sample([layer for layer in available_layers if layer not in player_1],
                                 min(14, len(available_layers)))
        print("player_2:", player_2)

        # 从剩余的非 blank_board 图层中随机抽取14个
        player_3 = random.sample([layer for layer in available_layers if layer not in player_1 + player_2],
                                 min(14, len(available_layers)))
        print("player_3:", player_3)
        player_4 = []
        player_5 = []
        player_6 = []
    elif player_num == 3:
        available_layers = [layer for layer in image_info.keys() if layer != "blank_board"]
        player_1 = random.sample(available_layers, min(11, len(available_layers)))
        update_player_1 = random.sample(available_layers, min(21, len(available_layers)))
        print("player_1:", player_1)

        player_2 = random.sample([layer for layer in available_layers if layer not in player_1],
                                 min(11, len(available_layers)))
        print("player_2:", player_2)

        player_3 = random.sample([layer for layer in available_layers if layer not in player_1 + player_2],
                                 min(10, len(available_layers)))
        print("player_3:", player_3)

        player_4 = random.sample([layer for layer in available_layers if layer not in player_1 + player_2 + player_3],
                                 min(10, len(available_layers)))
        print("player_4:", player_4)
        player_5 = []
        player_6 = []
    elif player_num == 4:
        available_layers = [layer for layer in image_info.keys() if layer != "blank_board"]
        player_1 = random.sample(available_layers, min(8, len(available_layers)))
        update_player_1 = random.sample(available_layers, min(21, len(available_layers)))
        print("player_1:", player_1)
        player_2 = random.sample([layer for layer in available_layers if layer not in player_1],
                                 min(8, len(available_layers)))
        print("player_2:", player_2)
        player_3 = random.sample([layer for layer in available_layers if layer not in player_1 + player_2],
                                 min(8, len(available_layers)))
        print("player_3:", player_3)
        player_4 = random.sample([layer for layer in available_layers if layer not in player_1 + player_2 + player_3],
                                 min(9, len(available_layers)))
        print("player_4:", player_4)
        player_5 = random.sample(
            [layer for layer in available_layers if layer not in player_1 + player_2 + player_3 + player_4],
            min(9, len(available_layers)))
        print("player_5:", player_5)
        player_6 = []
    elif player_num == 5:
        available_layers = [layer for layer in image_info.keys() if layer != "blank_board"]
        player_1 = random.sample(available_layers, min(7, len(available_layers)))
        update_player_1 = random.sample(available_layers, min(21, len(available_layers)))
        print("player_1:", player_1)
        player_2 = random.sample([layer for layer in available_layers if layer not in player_1],
                                 min(7, len(available_layers)))
        print("player_2:", player_2)
        player_3 = random.sample([layer for layer in available_layers if layer not in player_1 + player_2],
                                 min(7, len(available_layers)))
        print("player_3:", player_3)
        player_4 = random.sample([layer for layer in available_layers if layer not in player_1 + player_2 + player_3],
                                 min(7, len(available_layers)))
        print("player_4:", player_4)
        player_5 = random.sample(
            [layer for layer in available_layers if layer not in player_1 + player_2 + player_3 + player_4],
            min(7, len(available_layers)))
        print("player_5:", player_5)
        player_6 = random.sample(
            [layer for layer in available_layers if layer not in player_1 + player_2 + player_3 + player_4 + player_5],
            min(7, len(available_layers)))
        print("player_6:", player_6)
    alpha_increment = 5
    image_alpha = 0
    clock = pygame.time.Clock()
    # 加载红色圆圈图片
    red_circle_path = os.path.join(image_directory, 'red_circle.png')
    red_circle_image = load_image_with_alpha(red_circle_path, scale_factor=1)
    red_circle_image.set_alpha(128)  # 设置透明度为128
    # 加载绿色圆片
    green_circle_path = os.path.join(image_directory, 'green_circle.png')
    green_circle_image = load_image_with_alpha(green_circle_path, scale_factor=1)
    green_circle_image.set_alpha(128)  # 设置透明度为128
    # 加载棕色圆片
    brown_circle_path = os.path.join(image_directory, 'brown_circle.png')
    brown_circle_image = load_image_with_alpha(brown_circle_path, scale_factor=1)
    brown_circle_image.set_alpha(128)  # 设置透明度为128
    # 加载黄色圆片
    yellow_circle_path = os.path.join(image_directory, 'yellow_circle.png')
    yellow_circle_image = load_image_with_alpha(yellow_circle_path, scale_factor=1)
    yellow_circle_image.set_alpha(128)  # 设置透明度为128
    # 加载橙色圆片
    orange_circle_path = os.path.join(image_directory, 'orange_circle.png')
    orange_circle_image = load_image_with_alpha(orange_circle_path, scale_factor=1)
    orange_circle_image.set_alpha(128)  # 设置透明度为128
    # 加载紫色圆片
    purple_circle_path = os.path.join(image_directory, 'purple_circle.png')
    purple_circle_image = load_image_with_alpha(purple_circle_path, scale_factor=1)
    purple_circle_image.set_alpha(128)  # 设置透明度为128

    global show_point_1
    global final_point_layer_1
    global final_point_layer_2
    global final_point_layer_3
    global final_point_layer_4
    global attack_board_visible
    global is_rolling_button_rendered
    global show_explosion_1
    global show_explosion_2
    global show_explosion_3
    global show_explosion_4, infantry_card_num, artillery_card_num, cavalry_card_num, wild_card_num
    global render_move_army_number, choose_artillery, choose_cavalry, choose_infantry, choose_wild
    global render_Fortify_Brighter, Fortification_completed_rect, using_cards
    global selected_leave, render_risk_card_board, player_1_cards, adding_times
    global concentrate_on_leave, risk_adding_army
    global render_ending, risk_bag_image_rect, sound_effect_playing
    global playing_result, loser, render_round_num, attack_auto_rolling, render_risk_bag, infantry_card, cavalry_card, artillery_card, wild_card
    attack_completed_rect = None

    positions = [(550, 300), (550, 400), (650, 300), (650, 400)]
    slider_dragging = False
    slider_position = [500, 300]
    min_x = 500
    max_x = 800 - 100
    slider_range_width = max_x - min_x + 50
    slider_position_x = slider_position[0]  # 滑块当前位置
    top_y = 300  # 假设滑块中心y坐标为300，这里稍微上移一点作为顶部
    bottom_y = 332
    angle = 0
    # 加载文本位置和数字
    current_directory = os.path.dirname(os.path.realpath(__file__))
    text_positions_and_numbers = load_text_positions_and_numbers_from_dict()
    image_directory = os.path.join(current_directory, 'image')  # 假设图像在当前脚本同级的 image 文件夹中
    reinforcement_image_path = os.path.join(image_directory, 'reinforcement.png')
    reinforcement_image = load_image_with_alpha(reinforcement_image_path)
    red_circle_image_path = os.path.join(image_directory, 'red_circle.png')
    red_circle_image = load_and_adjust_alpha(red_circle_image_path, 128)  # 将透明度设置为 128
    file_path = os.path.join(current_directory, 'army_number.txt')
    Fortification_completed_rect = None
    wild_card_rect = pygame.Rect(700, 300, 0, 0)
    infantry_card_rect = pygame.Rect(400, 300, 0, 0)
    cavalry_card_rect = pygame.Rect(500, 300, 0, 0)
    artillery_card_rect = pygame.Rect(600, 300, 0, 0)
    minus_1_rect = pygame.Rect(410, 430, 0, 0)
    minus_2_rect = pygame.Rect(510, 430, 0, 0)
    minus_3_rect = pygame.Rect(610, 430, 0, 0)
    minus_4_rect = pygame.Rect(710, 430, 0, 0)
    plus_1_rect = pygame.Rect(480, 430, 0, 0)
    plus_2_rect = pygame.Rect(580, 430, 0, 0)
    plus_3_rect = pygame.Rect(680, 430, 0, 0)
    plus_4_rect = pygame.Rect(780, 430, 0, 0)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.USEREVENT:
                sound_effect_playing = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                mouse_x, mouse_y = event.pos
                if slider_position[0] <= mouse_pos[0] <= slider_position[0] + 100 and slider_position[1] <= mouse_pos[
                    1] <= slider_position[1] + 50:
                    slider_dragging = True
                    mouse_x_offset = slider_position[0] - mouse_pos[0]
                else:
                    handle_mouse_click(image_info, image_directory, mouse_pos, player_1, attack_completed_rect)
                    update_text_content()
                    is_rolling_button_rendered = True

                # 攻击面板的取消按钮
                if check_cancel_button_clicked(mouse_pos):
                    attack_board_visible = False
                    final_point_layer_1 = None
                    final_point_layer_2 = None
                    final_point_layer_3 = None
                    final_point_layer_4 = None
                    is_rolling_button_rendered = False
                    attack_auto_rolling = False
                # 调用移动面板的取消按钮函数
                handle_cancel_button_click(mouse_pos)
                # 调用移动面板的确认按钮
                handle_confirm_button_click(mouse_pos)
                # risk card点击加减号
                if minus_1_rect.collidepoint(mouse_pos):
                    if choose_infantry > 0:  # 只有当choose_infantry大于0时才能减少
                        choose_infantry -= 1
                        using_cards.remove('infantry_card')  # 从using_card中移除一个infantry_card
                    choose_infantry = max(choose_infantry, 0)
                    print(using_cards)

                if plus_1_rect.collidepoint(mouse_pos):
                    if choose_infantry < infantry_card_num:
                        choose_infantry += 1
                        using_cards.append('infantry_card')  # 向using_card中添加一个infantry_card
                    print(using_cards)
                if minus_3_rect.collidepoint(mouse_pos):
                    if choose_artillery > 0:
                        choose_artillery -= 1
                        using_cards.remove('artillery_card')  # 从using_card中移除一个artillery_card
                    choose_artillery = max(choose_artillery, 0)
                    print(using_cards)
                if plus_3_rect.collidepoint(mouse_pos):
                    if choose_artillery < artillery_card_num:
                        choose_artillery += 1
                        using_cards.append('artillery_card')  # 向using_card中添加一个artillery_card
                    print(using_cards)
                if minus_2_rect.collidepoint(mouse_pos):
                    if choose_cavalry > 0:
                        choose_cavalry -= 1
                        using_cards.remove('cavalry_card')  # 从using_card中移除一个cavalry_card
                    choose_cavalry = max(choose_cavalry, 0)
                    print(using_cards)
                if plus_2_rect.collidepoint(mouse_pos):
                    if choose_cavalry < cavalry_card_num:
                        choose_cavalry += 1
                        using_cards.append('cavalry_card')  # 向using_card中添加一个cavalry_card
                    print(using_cards)
                if minus_4_rect.collidepoint(mouse_pos):
                    if choose_wild > 0:
                        choose_wild -= 1
                        using_cards.remove('wild_card')  # 从using_card中移除一个wild_card
                    choose_wild = max(choose_wild, 0)
                    print(using_cards)
                if plus_4_rect.collidepoint(mouse_pos):
                    if choose_wild < wild_card_num:
                        choose_wild += 1
                        using_cards.append('wild_card')
                    print(using_cards)

                # 手动扔骰子
                if is_rolling_button_rendered and attack_board_visible and check_rolling_button_clicked(mouse_pos):
                    start_time = time.time()
                    show_point_1 = False

                    while time.time() - start_time < 1:  # 持续1秒
                        # 清除上一个point_xxx图层的区域
                        clear_rect_1 = pygame.Rect(550, 300, 100, 100)
                        clear_rect_2 = pygame.Rect(650, 300, 100, 100)  # 为第二个图层添加清除区域
                        clear_rect_3 = pygame.Rect(550, 400, 100, 100)
                        clear_rect_4 = pygame.Rect(650, 400, 100, 100)
                        screen.fill((65, 84, 91), clear_rect_1)
                        screen.fill((65, 84, 91), clear_rect_2)  # 清除第二个图层的区域
                        screen.fill((65, 84, 91), clear_rect_3)
                        screen.fill((65, 84, 91), clear_rect_4)
                        final_point_1 = random.randint(1, 6)
                        final_point_2 = random.randint(1, 6)
                        final_point_3 = random.randint(1, 6)
                        final_point_4 = random.randint(1, 6)
                        final_point_layer_1 = f"point_{final_point_1}"  # 更新最终的点数图层名称
                        final_point_layer_2 = f"point_{final_point_2}"
                        final_point_layer_3 = f"point_{final_point_3}"
                        final_point_layer_4 = f"point_{final_point_4}"
                        image_path_1 = os.path.join(image_directory, f"{final_point_layer_1}.png")
                        image_path_2 = os.path.join(image_directory, f"{final_point_layer_2}.png")  # 获取第二个图层的图像路径
                        image_path_3 = os.path.join(image_directory, f"{final_point_layer_3}.png")
                        image_path_4 = os.path.join(image_directory, f"{final_point_layer_4}.png")
                        image_1 = load_image_with_alpha(image_path_1, scale_factor=0.5)
                        image_2 = load_image_with_alpha(image_path_2, scale_factor=0.5)  # 加载第二个图层的图像
                        image_3 = load_image_with_alpha(image_path_3, scale_factor=0.5)
                        image_4 = load_image_with_alpha(image_path_4, scale_factor=0.5)
                        screen.blit(image_1, (550, 300))
                        screen.blit(image_2, (650, 300))  # 在(650, 300)位置渲染第二个图层
                        screen.blit(image_3, (550, 400))
                        screen.blit(image_4, (650, 400))

                        pygame.display.flip()

                        # 比较final_point_1和final_point_2的大小，并打印出胜者.这里是假设左边赢
                    if final_point_1 > final_point_2:
                        print("Final point 1 wins!")
                        dice_winner_1 = final_point_layer_1
                        show_explosion_2 = True
                        print(f"dice_winner_1:{dice_winner_1}")
                        # 读取并格式化selected_layer_within_180_pixels的值
                        formatted_layer_name_1 = "army_" + selected_layer_within_180_pixels.split("area_")[-1]
                        if formatted_layer_name_1 in globals() and globals()[formatted_layer_name_1] > 0:
                            globals()[formatted_layer_name_1] -= 1
                            print(f"{formatted_layer_name_1} value decreased by 1.")
                            # 检查是否减到0，如果是，则记录或采取特定操作
                            if globals()[formatted_layer_name_1] == 0:
                                print(f"{formatted_layer_name_1} has reached 0. No further decrements will be made.")
                                # 从selected_layer_within_180_pixels获取图层名
                                layer_to_remove = selected_layer_within_180_pixels
                                # 判断这个图层属于哪个player_几，并从相应列表中删除
                                removed = False
                                for i in range(1, 7):
                                    player_var = f'player_{i}'
                                    if layer_to_remove in globals()[player_var]:
                                        globals()[player_var].remove(layer_to_remove)
                                        print(
                                            f"Removed {layer_to_remove} from {player_var}. Current layers: {globals()[player_var]}")
                                        removed = True
                                        concentrate_on_layer = concentrate_on
                                        for j in range(1, 7):
                                            target_player_var = f'player_{j}'
                                            if concentrate_on_layer in globals()[target_player_var]:
                                                # 在这个player_几的列表中加入先前删除的selected_layer_within_180_pixels图层名
                                                globals()[target_player_var].append(layer_to_remove)
                                                print(
                                                    f"Added {layer_to_remove} to {target_player_var}. Current layers: {globals()[target_player_var]}")
                                                # 将格式化之后的selected_layer_within_180_pixels对应的全局变量赋值为1
                                                globals()[formatted_layer_name_1] = 1
                                                print(f"{formatted_layer_name_1} value set to 1.")
                                                update_text_content()
                                                final_point_layer_1 = None  # 存储最终的点数图层名称
                                                final_point_layer_2 = None
                                                final_point_layer_3 = None
                                                final_point_layer_4 = None
                                                attack_board_visible = False
                                                show_explosion_1 = False
                                                show_explosion_2 = False
                                                show_explosion_3 = False
                                                show_explosion_4 = False

                                                break

                                        break
                                if not removed:
                                    print(f"{layer_to_remove} was not found in any player's list.")

                        else:
                            print(
                                f"Warning: {formatted_layer_name_1} does not exist as a global variable or its value is already 0.")
                        # 这里是假设右边赢
                    elif final_point_2 > final_point_1:
                        print("Final point 2 wins!")
                        show_explosion_1 = True
                        dice_winner_1 = final_point_layer_2
                        print(f"dice_winner_1:{dice_winner_1}")
                        # 读取并格式化concentrate_on的值
                        formatted_layer_name_1 = "army_" + concentrate_on.split("area_")[-1]
                        if formatted_layer_name_1 in globals() and globals()[formatted_layer_name_1] > 0:
                            globals()[formatted_layer_name_1] -= 1
                            print(f"{formatted_layer_name_1} value decreased by 1.")
                            # 检查是否减到0，如果是，则记录或采取特定操作
                            if globals()[formatted_layer_name_1] == 0:
                                print(f"{formatted_layer_name_1} has reached 0. No further decrements will be made.")
                                layer_to_remove = concentrate_on
                                removed = False
                                for i in range(1, 7):
                                    player_var = f'player_{i}'
                                    if layer_to_remove in globals()[player_var]:
                                        globals()[player_var].remove(layer_to_remove)
                                        print(
                                            f"Removed {layer_to_remove} from {player_var}. Current layers: {globals()[player_var]}")
                                        removed = True
                                        selected_layer_within_180_pixels_layer = selected_layer_within_180_pixels
                                        for j in range(1, 7):
                                            target_player_var = f'player_{j}'
                                            if selected_layer_within_180_pixels_layer in globals()[target_player_var]:
                                                # 在这个player_几的列表中加入先前删除的selected_layer_within_180_pixels图层名
                                                globals()[target_player_var].append(layer_to_remove)
                                                print(
                                                    f"Added {layer_to_remove} to {target_player_var}. Current layers: {globals()[target_player_var]}")
                                                # 将格式化之后的selected_layer_within_180_pixels对应的全局变量赋值为1
                                                globals()[formatted_layer_name_1] = 1
                                                print(f"{formatted_layer_name_1} value set to 1.")
                                                update_text_content()

                                                final_point_layer_1 = None  # 存储最终的点数图层名称
                                                final_point_layer_2 = None
                                                final_point_layer_3 = None
                                                final_point_layer_4 = None
                                                attack_board_visible = False
                                                show_explosion_1 = False
                                                show_explosion_2 = False
                                                show_explosion_3 = False
                                                show_explosion_4 = False

                                                break
                                        break
                                if not removed:
                                    print(f"{layer_to_remove} was not found in any player's list.")
                        else:
                            print(
                                f"Warning: {formatted_layer_name_1} does not exist as a global variable or its value is already 0.")

                    elif final_point_1 == final_point_2 and final_point_1 is not None and final_point_2 is not None:
                        print("No winners in 1 and 2 ")
                    else:
                        print("There is something wrong in comparing！")

                    if final_point_3 > final_point_4:
                        # 读取并格式化selected_layer_within_180_pixels的值
                        formatted_layer_name_2 = "army_" + selected_layer_within_180_pixels.split("area_")[-1]
                        formatted_layer_name_3 = "army_" + concentrate_on.split("area_")[-1]
                        # 在这里添加判断
                        if globals().get(formatted_layer_name_2, 0) != 1 and globals().get(formatted_layer_name_3,
                                                                                           0) != 1:
                            print("Final point 3 wins!")
                            show_explosion_4 = True
                            dice_winner_2 = final_point_layer_3
                            print(f"dice_winner_2:{dice_winner_2}")

                            if formatted_layer_name_2 in globals() and globals()[formatted_layer_name_2] > 0:
                                globals()[formatted_layer_name_2] -= 1
                                print(f"{formatted_layer_name_2} value decreased by 1.")
                                # 检查是否减到0，如果是，则记录或采取特定操作
                                if globals()[formatted_layer_name_2] == 0:
                                    print(
                                        f"{formatted_layer_name_2} has reached 0. No further decrements will be made.")
                                    layer_to_remove = selected_layer_within_180_pixels
                                    removed = False
                                    for i in range(1, 7):
                                        player_var = f'player_{i}'
                                        if layer_to_remove in globals()[player_var]:
                                            globals()[player_var].remove(layer_to_remove)
                                            print(
                                                f"Removed {layer_to_remove} from {player_var}. Current layers: {globals()[player_var]}")
                                            removed = True
                                            concentrate_on_layer = concentrate_on
                                            for j in range(1, 7):
                                                target_player_var = f'player_{j}'
                                                if concentrate_on_layer in globals()[target_player_var]:
                                                    # 在这个player_几的列表中加入先前删除的selected_layer_within_180_pixels图层名
                                                    globals()[target_player_var].append(layer_to_remove)
                                                    print(
                                                        f"Added {layer_to_remove} to {target_player_var}. Current layers: {globals()[target_player_var]}")
                                                    # 将格式化之后的selected_layer_within_180_pixels对应的全局变量赋值为1
                                                    globals()[formatted_layer_name_2] = 1
                                                    print(f"{formatted_layer_name_2} value set to 1.")
                                                    update_text_content()

                                                    final_point_layer_1 = None  # 存储最终的点数图层名称
                                                    final_point_layer_2 = None
                                                    final_point_layer_3 = None
                                                    final_point_layer_4 = None
                                                    attack_board_visible = False
                                                    show_explosion_1 = False
                                                    show_explosion_2 = False
                                                    show_explosion_3 = False
                                                    show_explosion_4 = False

                                                    break
                                            break
                                    if not removed:
                                        print(f"{layer_to_remove} was not found in any player's list.")
                            else:
                                show_explosion_4 = False
                                print(
                                    f"Warning: {formatted_layer_name_1} does not exist as a global variable or its value is already 0.")
                    elif final_point_3 < final_point_4:
                        # 读取并格式化concentrate_on的值
                        formatted_layer_name_2 = "army_" + concentrate_on.split("area_")[-1]
                        formatted_layer_name_3 = "army_" + selected_layer_within_180_pixels.split("area_")[-1]
                        # 在这里添加判断
                        if globals().get(formatted_layer_name_2, 0) != 1 and globals().get(formatted_layer_name_3,
                                                                                           0) != 1:
                            print("Final point 4 wins!")
                            show_explosion_3 = True
                            dice_winner_2 = final_point_layer_4
                            print(f"dice_winner_2:{dice_winner_2}")

                            if formatted_layer_name_2 in globals() and globals()[formatted_layer_name_2] > 0:
                                globals()[formatted_layer_name_2] -= 1
                                print(f"{formatted_layer_name_2} value decreased by 1.")
                                # 检查是否减到0，如果是，则记录或采取特定操作
                                if globals()[formatted_layer_name_2] == 0:
                                    print(
                                        f"{formatted_layer_name_2} has reached 0. No further decrements will be made.")
                                    layer_to_remove = concentrate_on
                                    removed = False
                                    for i in range(1, 7):
                                        player_var = f'player_{i}'
                                        if layer_to_remove in globals()[player_var]:
                                            globals()[player_var].remove(layer_to_remove)
                                            print(
                                                f"Removed {layer_to_remove} from {player_var}. Current layers: {globals()[player_var]}")
                                            removed = True
                                            selected_layer_within_180_pixels_layer = selected_layer_within_180_pixels
                                            for j in range(1, 7):
                                                target_player_var = f'player_{j}'
                                                if selected_layer_within_180_pixels_layer in globals()[
                                                    target_player_var]:
                                                    # 在这个player_几的列表中加入先前删除的selected_layer_within_180_pixels图层名
                                                    globals()[target_player_var].append(layer_to_remove)
                                                    print(
                                                        f"Added {layer_to_remove} to {target_player_var}. Current layers: {globals()[target_player_var]}")
                                                    # 将格式化之后的selected_layer_within_180_pixels对应的全局变量赋值为1
                                                    globals()[formatted_layer_name_2] = 1
                                                    print(f"{formatted_layer_name_2} value set to 1.")
                                                    update_text_content()

                                                    final_point_layer_1 = None  # 存储最终的点数图层名称
                                                    final_point_layer_2 = None
                                                    final_point_layer_3 = None
                                                    final_point_layer_4 = None
                                                    attack_board_visible = False
                                                    show_explosion_1 = False
                                                    show_explosion_2 = False
                                                    show_explosion_3 = False
                                                    show_explosion_4 = False

                                                    break
                                            break
                                    if not removed:
                                        print(f"{layer_to_remove} was not found in any player's list.")
                            else:
                                show_explosion_3 = False
                                print(
                                    f"Warning: {formatted_layer_name_1} does not exist as a global variable or its value is already 0.")
                    elif final_point_3 == final_point_4 and final_point_3 is not None and final_point_4 is not None:
                        print("No winners in 3 and 4")
                    else:
                        print("There is something wrong in comparing！")

                    print(f"Final point 1: {final_point_1}")
                    print(f"Final point 2: {final_point_2}")
                    print(f"Final point 3: {final_point_3}")
                    print(f"Final point 4: {final_point_4}")
                    # 排除掉初始状态时的空列表，看有没有新增空列表，有的话就是已结束游戏的玩家
                    remaining_players = [f'player_{i}' for i in range(1, 7) if
                                         globals().get(f'player_{i}', []) and f'player_{i}' not in none_player]

                    if len(remaining_players) == 0:
                        # 如果没有剩余的玩家，不执行任何操作
                        pass
                    elif len(remaining_players) == 1:
                        # 如果只剩下一个玩家
                        if 'player_1' in remaining_players:
                            # 如果这个玩家是player_1
                            playing_result = 'lost'
                            render_ending = True
                        else:
                            # 如果剩下的玩家不是player_1
                            playing_result = 'some_one_lost'
                            render_ending = True
                    else:
                        # 如果有多于一个玩家剩余，不需要更新playing_result，因为游戏还在进行中
                        pass

                # 自动扔骰子
                while attack_auto_rolling and attack_board_visible and check_auto_rolling(mouse_pos):
                    start_time = time.time()
                    show_point_1 = False

                    while time.time() - start_time < 0.1:  # 持续1秒
                        # 清除上一个point_xxx图层的区域
                        clear_rect_1 = pygame.Rect(550, 300, 100, 100)
                        clear_rect_2 = pygame.Rect(650, 300, 100, 100)  # 为第二个图层添加清除区域
                        clear_rect_3 = pygame.Rect(550, 400, 100, 100)
                        clear_rect_4 = pygame.Rect(650, 400, 100, 100)
                        screen.fill((65, 84, 91), clear_rect_1)
                        screen.fill((65, 84, 91), clear_rect_2)  # 清除第二个图层的区域
                        screen.fill((65, 84, 91), clear_rect_3)
                        screen.fill((65, 84, 91), clear_rect_4)
                        final_point_1 = random.randint(1, 6)
                        final_point_2 = random.randint(1, 6)
                        final_point_3 = random.randint(1, 6)
                        final_point_4 = random.randint(1, 6)
                        final_point_layer_1 = f"point_{final_point_1}"  # 更新最终的点数图层名称
                        final_point_layer_2 = f"point_{final_point_2}"
                        final_point_layer_3 = f"point_{final_point_3}"
                        final_point_layer_4 = f"point_{final_point_4}"
                        image_path_1 = os.path.join(image_directory, f"{final_point_layer_1}.png")
                        image_path_2 = os.path.join(image_directory, f"{final_point_layer_2}.png")  # 获取第二个图层的图像路径
                        image_path_3 = os.path.join(image_directory, f"{final_point_layer_3}.png")
                        image_path_4 = os.path.join(image_directory, f"{final_point_layer_4}.png")
                        image_1 = load_image_with_alpha(image_path_1, scale_factor=0.5)
                        image_2 = load_image_with_alpha(image_path_2, scale_factor=0.5)  # 加载第二个图层的图像
                        image_3 = load_image_with_alpha(image_path_3, scale_factor=0.5)
                        image_4 = load_image_with_alpha(image_path_4, scale_factor=0.5)
                        screen.blit(image_1, (550, 300))
                        screen.blit(image_2, (650, 300))  # 在(650, 300)位置渲染第二个图层
                        screen.blit(image_3, (550, 400))
                        screen.blit(image_4, (650, 400))

                        pygame.display.flip()

                        # 比较final_point_1和final_point_2的大小，并打印出胜者.这里是假设左边赢
                    if final_point_1 > final_point_2:
                        print("Final point 1 wins!")
                        dice_winner_1 = final_point_layer_1
                        show_explosion_2 = True
                        print(f"dice_winner_1:{dice_winner_1}")
                        # 读取并格式化selected_layer_within_180_pixels的值
                        formatted_layer_name_1 = "army_" + selected_layer_within_180_pixels.split("area_")[-1]
                        if formatted_layer_name_1 in globals() and globals()[formatted_layer_name_1] > 0:
                            globals()[formatted_layer_name_1] -= 1
                            print(f"{formatted_layer_name_1} value decreased by 1.")
                            # 检查是否减到0，如果是，则记录或采取特定操作
                            if globals()[formatted_layer_name_1] == 0:
                                print(f"{formatted_layer_name_1} has reached 0. No further decrements will be made.")
                                # 从selected_layer_within_180_pixels获取图层名
                                layer_to_remove = selected_layer_within_180_pixels
                                # 判断这个图层属于哪个player_几，并从相应列表中删除
                                removed = False

                                for i in range(1, 7):
                                    player_var = f'player_{i}'
                                    if layer_to_remove in globals()[player_var]:
                                        globals()[player_var].remove(layer_to_remove)
                                        print(
                                            f"Removed {layer_to_remove} from {player_var}. Current layers: {globals()[player_var]}")
                                        removed = True
                                        concentrate_on_layer = concentrate_on
                                        for j in range(1, 7):
                                            target_player_var = f'player_{j}'
                                            if concentrate_on_layer in globals()[target_player_var]:
                                                # 在这个player_几的列表中加入先前删除的selected_layer_within_180_pixels图层名
                                                globals()[target_player_var].append(layer_to_remove)
                                                print(
                                                    f"Added {layer_to_remove} to {target_player_var}. Current layers: {globals()[target_player_var]}")
                                                # 将格式化之后的selected_layer_within_180_pixels对应的全局变量赋值为1
                                                globals()[formatted_layer_name_1] = 1
                                                print(f"{formatted_layer_name_1} value set to 1.")
                                                update_text_content()
                                                final_point_layer_1 = None  # 存储最终的点数图层名称
                                                final_point_layer_2 = None
                                                final_point_layer_3 = None
                                                final_point_layer_4 = None
                                                attack_board_visible = False
                                                show_explosion_1 = False
                                                show_explosion_2 = False
                                                show_explosion_3 = False
                                                show_explosion_4 = False

                                                break

                                        break
                                break
                                if not removed:
                                    print(f"{layer_to_remove} was not found in any player's list.")

                        else:
                            print(
                                f"Warning: {formatted_layer_name_1} does not exist as a global variable or its value is already 0.")
                        # 这里是假设右边赢
                    elif final_point_2 > final_point_1:
                        print("Final point 2 wins!")
                        show_explosion_1 = True
                        dice_winner_1 = final_point_layer_2
                        print(f"dice_winner_1:{dice_winner_1}")
                        # 读取并格式化concentrate_on的值
                        formatted_layer_name_1 = "army_" + concentrate_on.split("area_")[-1]
                        if formatted_layer_name_1 in globals() and globals()[formatted_layer_name_1] > 0:
                            globals()[formatted_layer_name_1] -= 1
                            print(f"{formatted_layer_name_1} value decreased by 1.")
                            # 检查是否减到0，如果是，则记录或采取特定操作
                            if globals()[formatted_layer_name_1] == 0:
                                print(f"{formatted_layer_name_1} has reached 0. No further decrements will be made.")
                                layer_to_remove = concentrate_on
                                removed = False

                                for i in range(1, 7):
                                    player_var = f'player_{i}'
                                    if layer_to_remove in globals()[player_var]:
                                        globals()[player_var].remove(layer_to_remove)
                                        print(
                                            f"Removed {layer_to_remove} from {player_var}. Current layers: {globals()[player_var]}")
                                        removed = True
                                        selected_layer_within_180_pixels_layer = selected_layer_within_180_pixels
                                        for j in range(1, 7):
                                            target_player_var = f'player_{j}'
                                            if selected_layer_within_180_pixels_layer in globals()[target_player_var]:
                                                # 在这个player_几的列表中加入先前删除的selected_layer_within_180_pixels图层名
                                                globals()[target_player_var].append(layer_to_remove)
                                                print(
                                                    f"Added {layer_to_remove} to {target_player_var}. Current layers: {globals()[target_player_var]}")
                                                # 将格式化之后的selected_layer_within_180_pixels对应的全局变量赋值为1
                                                globals()[formatted_layer_name_1] = 1
                                                print(f"{formatted_layer_name_1} value set to 1.")
                                                update_text_content()

                                                final_point_layer_1 = None  # 存储最终的点数图层名称
                                                final_point_layer_2 = None
                                                final_point_layer_3 = None
                                                final_point_layer_4 = None
                                                attack_board_visible = False
                                                show_explosion_1 = False
                                                show_explosion_2 = False
                                                show_explosion_3 = False
                                                show_explosion_4 = False

                                                break
                                        break
                                break
                                if not removed:
                                    print(f"{layer_to_remove} was not found in any player's list.")
                        else:
                            print(
                                f"Warning: {formatted_layer_name_1} does not exist as a global variable or its value is already 0.")

                    elif final_point_1 == final_point_2 and final_point_1 is not None and final_point_2 is not None:
                        print("No winners in 1 and 2 ")
                    else:
                        print("There is something wrong in comparing！")

                    if final_point_3 > final_point_4:
                        # 读取并格式化selected_layer_within_180_pixels的值
                        formatted_layer_name_2 = "army_" + selected_layer_within_180_pixels.split("area_")[-1]
                        formatted_layer_name_3 = "army_" + concentrate_on.split("area_")[-1]
                        # 在这里添加判断
                        if globals().get(formatted_layer_name_2, 0) != 1 and globals().get(formatted_layer_name_3,
                                                                                           0) != 1:
                            print("Final point 3 wins!")
                            show_explosion_4 = True
                            dice_winner_2 = final_point_layer_3
                            print(f"dice_winner_2:{dice_winner_2}")

                            if formatted_layer_name_2 in globals() and globals()[formatted_layer_name_2] > 0:
                                globals()[formatted_layer_name_2] -= 1
                                print(f"{formatted_layer_name_2} value decreased by 1.")
                                # 检查是否减到0，如果是，则记录或采取特定操作
                                if globals()[formatted_layer_name_2] == 0:
                                    print(
                                        f"{formatted_layer_name_2} has reached 0. No further decrements will be made.")
                                    layer_to_remove = selected_layer_within_180_pixels
                                    removed = False

                                    for i in range(1, 7):
                                        player_var = f'player_{i}'
                                        if layer_to_remove in globals()[player_var]:
                                            globals()[player_var].remove(layer_to_remove)
                                            print(
                                                f"Removed {layer_to_remove} from {player_var}. Current layers: {globals()[player_var]}")
                                            removed = True
                                            concentrate_on_layer = concentrate_on
                                            for j in range(1, 7):
                                                target_player_var = f'player_{j}'
                                                if concentrate_on_layer in globals()[target_player_var]:
                                                    # 在这个player_几的列表中加入先前删除的selected_layer_within_180_pixels图层名
                                                    globals()[target_player_var].append(layer_to_remove)
                                                    print(
                                                        f"Added {layer_to_remove} to {target_player_var}. Current layers: {globals()[target_player_var]}")
                                                    # 将格式化之后的selected_layer_within_180_pixels对应的全局变量赋值为1
                                                    globals()[formatted_layer_name_2] = 1
                                                    print(f"{formatted_layer_name_2} value set to 1.")
                                                    update_text_content()

                                                    final_point_layer_1 = None  # 存储最终的点数图层名称
                                                    final_point_layer_2 = None
                                                    final_point_layer_3 = None
                                                    final_point_layer_4 = None
                                                    attack_board_visible = False
                                                    show_explosion_1 = False
                                                    show_explosion_2 = False
                                                    show_explosion_3 = False
                                                    show_explosion_4 = False

                                                    break
                                            break
                                    break
                                    if not removed:
                                        print(f"{layer_to_remove} was not found in any player's list.")
                            else:
                                show_explosion_4 = False
                                print(
                                    f"Warning: {formatted_layer_name_1} does not exist as a global variable or its value is already 0.")
                    elif final_point_3 < final_point_4:
                        # 读取并格式化concentrate_on的值
                        formatted_layer_name_2 = "army_" + concentrate_on.split("area_")[-1]
                        formatted_layer_name_3 = "army_" + selected_layer_within_180_pixels.split("area_")[-1]
                        # 在这里添加判断
                        if globals().get(formatted_layer_name_2, 0) != 1 and globals().get(formatted_layer_name_3,
                                                                                           0) != 1:
                            print("Final point 4 wins!")
                            show_explosion_3 = True
                            dice_winner_2 = final_point_layer_4
                            print(f"dice_winner_2:{dice_winner_2}")

                            if formatted_layer_name_2 in globals() and globals()[formatted_layer_name_2] > 0:
                                globals()[formatted_layer_name_2] -= 1
                                print(f"{formatted_layer_name_2} value decreased by 1.")
                                # 检查是否减到0，如果是，则记录或采取特定操作
                                if globals()[formatted_layer_name_2] == 0:
                                    print(
                                        f"{formatted_layer_name_2} has reached 0. No further decrements will be made.")
                                    layer_to_remove = concentrate_on
                                    removed = False

                                    for i in range(1, 7):
                                        player_var = f'player_{i}'
                                        if layer_to_remove in globals()[player_var]:
                                            globals()[player_var].remove(layer_to_remove)
                                            print(
                                                f"Removed {layer_to_remove} from {player_var}. Current layers: {globals()[player_var]}")
                                            removed = True
                                            selected_layer_within_180_pixels_layer = selected_layer_within_180_pixels
                                            for j in range(1, 7):
                                                target_player_var = f'player_{j}'
                                                if selected_layer_within_180_pixels_layer in globals()[
                                                    target_player_var]:
                                                    # 在这个player_几的列表中加入先前删除的selected_layer_within_180_pixels图层名
                                                    globals()[target_player_var].append(layer_to_remove)
                                                    print(
                                                        f"Added {layer_to_remove} to {target_player_var}. Current layers: {globals()[target_player_var]}")
                                                    # 将格式化之后的selected_layer_within_180_pixels对应的全局变量赋值为1
                                                    globals()[formatted_layer_name_2] = 1
                                                    print(f"{formatted_layer_name_2} value set to 1.")
                                                    update_text_content()

                                                    final_point_layer_1 = None  # 存储最终的点数图层名称
                                                    final_point_layer_2 = None
                                                    final_point_layer_3 = None
                                                    final_point_layer_4 = None
                                                    attack_board_visible = False
                                                    show_explosion_1 = False
                                                    show_explosion_2 = False
                                                    show_explosion_3 = False
                                                    show_explosion_4 = False

                                                    break
                                            break
                                    break

                                    if not removed:
                                        print(f"{layer_to_remove} was not found in any player's list.")
                            else:
                                show_explosion_3 = False
                                print(
                                    f"Warning: {formatted_layer_name_1} does not exist as a global variable or its value is already 0.")
                    elif final_point_3 == final_point_4 and final_point_3 is not None and final_point_4 is not None:
                        print("No winners in 3 and 4")
                    else:
                        print("There is something wrong in comparing！")

                    print(f"Final point 1: {final_point_1}")
                    print(f"Final point 2: {final_point_2}")
                    print(f"Final point 3: {final_point_3}")
                    print(f"Final point 4: {final_point_4}")

                    remaining_players = [f'player_{i}' for i in range(1, 7) if
                                         globals().get(f'player_{i}', []) and f'player_{i}' not in none_player]

                    if len(remaining_players) == 0:
                        # 如果没有剩余的玩家，不执行任何操作
                        pass
                    elif len(remaining_players) == 1:
                        # 如果只剩下一个玩家
                        if 'player_1' in remaining_players:
                            # 如果这个玩家是player_1
                            playing_result = 'lost'
                            render_ending = True
                        else:
                            # 如果剩下的玩家不是player_1
                            playing_result = 'some_one_lost'
                            render_ending = True
                    else:
                        # 如果有多于一个玩家剩余，不需要更新playing_result，因为游戏还在进行中
                        pass
                    # 不排除none_player的情况下检查player_2到player_6是否都为空列表
                    player_lists_empty_without_exclusion = all(
                        not globals().get(f'player_{i}', []) for i in range(2, 7))
                    if player_lists_empty_without_exclusion:
                        playing_result = 'win'
                        render_ending = True
                    if render_round_num == 0:
                        playing_result = 'no_winner'
                        render_ending = True

                    # 去重，因为可能有重复添加的情况
                    player_1_cards = list(set(player_1_cards))
                    print("you have cards:", player_1_cards)
                    # 风险卡的显示
                if handle_risk_bag_click(mouse_pos):
                    render_risk_card_board = True

                # 在这里更新列表，存储距离 concentrate_on 的图层 180 个像素范围内的所有图层的名字
                if concentrate_on is not None:
                    # 格式化concentrate_on的值
                    formatted_concentrate_on = "army_" + concentrate_on.split("_", 1)[1]
                    # 检查全局变量中formatted_concentrate_on的值是否为1
                    if globals().get(formatted_concentrate_on, 0) == 1:
                        layers_within_180_pixels = []
                    else:
                        center_position = image_info[concentrate_on][1]
                        # 当 concentrate_on 非空且 render_Fortify_Brighter 为 true 时的逻辑
                        if render_Fortify_Brighter:
                            if concentrate_on in player_1:
                                # 如果 concentrate_on 属于 player_1，排除 player_2 到 player_6 的图层
                                exclude_layers = player_2 + player_3 + player_4 + player_5 + player_6 + [concentrate_on]
                            elif concentrate_on in player_2:
                                exclude_layers = player_1 + player_3 + player_4 + player_5 + player_6 + [concentrate_on]
                            elif concentrate_on in player_3:
                                exclude_layers = player_1 + player_2 + player_4 + player_5 + player_6 + [concentrate_on]
                            elif concentrate_on in player_4:
                                exclude_layers = player_1 + player_2 + player_3 + player_5 + player_6 + [concentrate_on]
                            elif concentrate_on in player_5:
                                exclude_layers = player_1 + player_2 + player_3 + player_4 + player_6 + [concentrate_on]
                            elif concentrate_on in player_6:
                                exclude_layers = player_1 + player_2 + player_3 + player_4 + player_5 + [concentrate_on]
                            else:
                                exclude_layers = []
                        else:
                            # 当 concentrate_on 非空但 render_Fortify_Brighter 为 false 时，保持原有逻辑
                            if concentrate_on in player_1:
                                exclude_layers = player_1  # 如果 concentrate_on 属于 player_1，排除 player_1 的图层
                            elif concentrate_on in player_2:
                                exclude_layers = player_2
                            elif concentrate_on in player_3:
                                exclude_layers = player_3
                            elif concentrate_on in player_4:
                                exclude_layers = player_4
                            elif concentrate_on in player_5:
                                exclude_layers = player_5
                            elif concentrate_on in player_6:
                                exclude_layers = player_6
                            else:
                                exclude_layers = []
                        exclude_layers.append("blank_board")
                        layers_within_180_pixels = get_layers_within_radius(center_position, image_info, exclude_layers,
                                                                            concentrate_on, render_Fortify_Brighter,
                                                                            player_1)
                        print("Layers within 180 pixels and not in exclude_layers:", layers_within_180_pixels)

            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                slider_dragging = False
            elif event.type == pygame.MOUSEMOTION:
                pygame.mouse.get_pos()
                if slider_dragging:
                    mouse_x, _ = event.pos
                    # 更新滑块位置前先计算新位置
                    new_slider_x = mouse_x + mouse_x_offset
                    # 确保新位置不会超出设定的范围
                    if new_slider_x < min_x:
                        new_slider_x = min_x
                    elif new_slider_x > max_x:
                        new_slider_x = max_x
                    # 更新滑块位置
                    slider_position[0] = new_slider_x

            # 计算滑块已滑动的范围百分比
        slider_range = max_x - min_x
        slider_progress = (slider_position[0] - min_x) / slider_range
        slider_progress_percentage = int(slider_progress * 100)  # 转换为整数百分比
        inverse_slider_progress_percentage = 100 - slider_progress_percentage
        image_alpha += alpha_increment
        image_alpha = min(image_alpha, 255)

        # 新增：用于存储与鼠标位置相交的图层及其位置信息
        intersecting_layers = []
        mouse_pos = pygame.mouse.get_pos()
        for image_name, (file_name, position) in image_info.items():
            image_path = os.path.join(image_directory, file_name)
            image = load_image_with_alpha(image_path, scale_factor=1.4)

            if image_name != "blank_board" and enable_is_mouse_over:
                image_rect = image.get_rect(topleft=position)
                if image_rect.collidepoint(mouse_pos):
                    # 收集所有与鼠标位置相交的图层信息
                    intersecting_layers.append((image_name, position, image))

        # 检测鼠标所指的颜色，并决定哪个图层亮起
        target_color = (208, 197, 178)
        layer_to_highlight = None
        for layer in reversed(intersecting_layers):  # 从最顶层开始检测
            image_name, position, image = layer
            local_pos = (mouse_pos[0] - position[0], mouse_pos[1] - position[1])
            try:
                pixel_color = image.get_at(local_pos)
                if pixel_color[:3] == target_color and enable_handle_mouse_click:  # 忽略alpha值
                    layer_to_highlight = image_name
                    break
                elif pixel_color[3] == 0:  # 如果是透明的，继续检测下一个图层
                    continue
            except IndexError:  # 鼠标位置超出图像范围
                continue

        # 首先渲染所有图层，包括应用基本的亮度调整
        for image_name, (file_name, position) in image_info.items():
            image_path = os.path.join(image_directory, file_name)
            image = load_image_with_alpha(image_path, scale_factor=1.4)

            bright_image = pygame.Surface(image.get_size(), flags=pygame.SRCALPHA)
            bright_image.fill((0, 0, 0, 0))  # 初始填充为透明

            if image_name != "blank_board":
                if image_name == layer_to_highlight or image_name == concentrate_on:
                    # 对匹配的图层或concentrate_on指向的图层应用亮起效果
                    bright_image.fill((60, 60, 60, 0))
            bright_image.blit(image, (0, 0), special_flags=pygame.BLEND_RGBA_ADD)
            screen.blit(bright_image, position)

        # 然后，专门处理180像素范围内的图层，确保它们在最顶层显示
        for image_name in layers_within_180_pixels:
            if image_name in image_info:
                file_name, position = image_info[image_name][:2]
                image_path = os.path.join(image_directory, file_name)
                image = load_image_with_alpha(image_path, scale_factor=1.4)

                bright_image = pygame.Surface(image.get_size(), flags=pygame.SRCALPHA)
                bright_color = (brightness_value, brightness_value, brightness_value, 0)
                bright_image.fill(bright_color)

                bright_image.blit(image, (0, 0), special_flags=pygame.BLEND_RGBA_ADD)
                screen.blit(bright_image, position)

        file_path = 'circle_position.txt'
        red_circle_positions = load_layers_from_file(file_path)
        green_circle_positions = load_layers_from_file(file_path)
        brown_circle_positions = load_layers_from_file(file_path)
        yellow_circle_positions = load_layers_from_file(file_path)
        orange_circle_positions = load_layers_from_file(file_path)
        purple_circle_positions = load_layers_from_file(file_path)
        # 获取player_1中的图层名
        player_1_layers = set(player_1)
        # 渲染小红片在所有图层之上
        for image_name, (x_position, y_position) in red_circle_positions.items():
            if image_name in player_1_layers:
                red_circle_position_absolute = (x_position, y_position)
                screen.blit(red_circle_image, red_circle_position_absolute)

                # 获取player_2中的图层名
        player_2_layers = set(player_2)
        # 渲染绿色圆片在所有图层之上
        for image_name, (x_position, y_position) in green_circle_positions.items():
            if image_name in player_2_layers:
                green_circle_position_absolute = (x_position, y_position)
                screen.blit(green_circle_image, green_circle_position_absolute)

        # 获取player_3中的图层名
        player_3_layers = set(player_3)
        # 渲染蓝色圆片在所有图层之上
        for image_name, (x_position, y_position) in brown_circle_positions.items():
            if image_name in player_3_layers:
                brown_circle_position_absolute = (x_position, y_position)
                screen.blit(brown_circle_image, brown_circle_position_absolute)

        # 获取player_4中的图层名
        player_4_layers = set(player_4)
        # 渲染黄色圆片在所有图层之上
        for image_name, (x_position, y_position) in yellow_circle_positions.items():
            if image_name in player_4_layers:
                yellow_circle_position_absolute = (x_position, y_position)
                screen.blit(yellow_circle_image, yellow_circle_position_absolute)

        # 获取player_5中的图层名
        player_5_layers = set(player_5)
        # 渲染橙色圆片在所有图层之上
        for image_name, (x_position, y_position) in orange_circle_positions.items():
            if image_name in player_5_layers:
                orange_circle_position_absolute = (x_position, y_position)
                screen.blit(orange_circle_image, orange_circle_position_absolute)

        # 获取player_6中的图层名
        player_6_layers = set(player_6)
        # 渲染紫色圆片在所有图层之上
        for image_name, (x_position, y_position) in purple_circle_positions.items():
            if image_name in player_6_layers:
                purple_circle_position_absolute = (x_position, y_position)
                screen.blit(purple_circle_image, purple_circle_position_absolute)

        # 遍历字典，渲染每个区域的军队数量文本
        for area_name, info in area_data.items():
            # 原始位置
            original_position = info["position"]
            # 调整位置，向右移动18个像素，向下移动15个像素
            adjusted_position = (original_position[0] + 18, original_position[1] + 15)

            # 构建全局变量名称，例如从"area_Alaska"到"army_Alaska"
            army_var_name = "army_" + area_name.split("_", 1)[1]
            # 使用globals()函数动态获取全局变量的值
            army_count = globals().get(army_var_name, 0)  # 如果变量不存在，则默认为0
            text_to_display = str(army_count)
            text_surface = font.render(text_to_display, True, (255, 255, 255))  # 白色文本
            screen.blit(text_surface, adjusted_position)

            # 渲染reinforcement
        if render_reinforcement:
            reinforcement_position = (820, 520)
            screen.blit(reinforcement_image, reinforcement_position)

        # 渲染reinforcement上面的红色圆片
        if render_red_circle_2:
            # 渲染红色圆片
            red_circle_position = (820, 450)
            screen.blit(red_circle_image, red_circle_position)

        # 渲染21以及它的文本框
        if text_display_switch:
            render_text(screen, str(text_content), (820, 450), display=text_display_switch)

        # 渲染attack_completed图层
        if render_attack_completed:
            attack_completed_image_path = os.path.join(image_directory, 'attack_completed.png')
            attack_completed_image = load_image_with_alpha(attack_completed_image_path, scale_factor=1.4)
            attack_completed_rect = attack_completed_image.get_rect(topleft=(1100, 680))
            screen.blit(attack_completed_image, (1100, 680))

            # 渲染移动军队的按钮fortification_completed
        if render_Fortification_completed:
            Fortification_completed_image_path = os.path.join(image_directory, 'Fortification_completed.png')
            Fortification_completed_image = load_image_with_alpha(Fortification_completed_image_path, scale_factor=1.4)
            Fortification_completed_rect = Fortification_completed_image.get_rect(topleft=(1100, 680))
            screen.blit(Fortification_completed_image, (1100, 680))

        # 渲染reinforce状态栏
        Reinforce_image_path = os.path.join(image_directory, 'Reinforce.png')
        Reinforce_image = load_image_with_alpha(Reinforce_image_path, scale_factor=1.0)
        screen.blit(Reinforce_image, (500, 700))

        # 渲染Attack状态栏
        Attack_image_path = os.path.join(image_directory, 'Attack.png')
        Attack_image = load_image_with_alpha(Attack_image_path, scale_factor=1.0)
        screen.blit(Attack_image, (600, 700))

        # 渲染Fortify状态栏
        Fortify_image_path = os.path.join(image_directory, 'Fortify.png')
        Fortify_image = load_image_with_alpha(Fortify_image_path, scale_factor=1.0)
        screen.blit(Fortify_image, (700, 700))

        # 渲染reinforce_Brighter状态栏
        if render_Reinforce_Brighter:
            Reinforce_Brighter_image_path = os.path.join(image_directory, 'Reinforce_Brighter.png')
            Reinforce_Brighter_image = load_image_with_alpha(Reinforce_Brighter_image_path, scale_factor=1.0)
            screen.blit(Reinforce_Brighter_image, (500, 700))

        # 渲染Attack_Brighter状态栏
        if render_Attack_Brighter:
            Attack_Brighter_image_path = os.path.join(image_directory, 'Attack_Brighter.png')
            AttackBrighter_image = load_image_with_alpha(Attack_Brighter_image_path, scale_factor=1.0)
            screen.blit(AttackBrighter_image, (600, 700))

        # 渲染Fortify_Brighter状态栏
        if render_Fortify_Brighter:
            Fortify_Brighter_image_path = os.path.join(image_directory, 'Fortify_Brighter.png')
            Fortify_Brighter_image = load_image_with_alpha(Fortify_Brighter_image_path, scale_factor=1.0)
            screen.blit(Fortify_Brighter_image, (700, 700))

        # 渲染risk_card 背包
        if render_risk_bag:
            risk_bag_image_path = os.path.join(image_directory, 'risk_bag.png')
            risk_bag_image = load_image_with_alpha(risk_bag_image_path, scale_factor=1.5)
            risk_bag_image_rect = risk_bag_image.get_rect(topleft=(1000, 715))
            screen.blit(risk_bag_image, (1000, 715))

        # 渲染risk card board
        if render_risk_card_board:
            risk_card_board_image_path = os.path.join(image_directory, 'risk_card_board.png')
            risk_card_board_image = load_image_with_alpha(risk_card_board_image_path, scale_factor=1.7)
            screen.blit(risk_card_board_image, (320, 180))
            risk_card_introduction = "Choose and use your risk cards"
            risk_card_introduction_surface = font.render(risk_card_introduction, True, (255, 255, 255))
            risk_card_introduction_position = (400, 250)
            screen.blit(risk_card_introduction_surface, risk_card_introduction_position)
            # 渲染纯色的confirm按钮
            confirm_button_2_rect = pygame.Rect(420, 600, 100, 50)  # 确认按钮的位置和大小
            pygame.draw.rect(screen, (0, 255, 0), confirm_button_2_rect)  # 使用绿色绘制确认按钮
            confirm_text_surface = font.render('Confirm', True, (255, 255, 255))
            screen.blit(confirm_text_surface, (confirm_button_2_rect.x + 10, confirm_button_2_rect.y + 15))

            # 渲染纯色的cancel按钮
            cancel_button_2_rect = pygame.Rect(550, 600, 100, 50)  # 取消按钮的位置和大小
            pygame.draw.rect(screen, (0, 255, 0), cancel_button_2_rect)  # 使用绿色绘制取消按钮
            cancel_text_surface = font.render('Cancel', True, (255, 255, 255))
            screen.blit(cancel_text_surface, (cancel_button_2_rect.x + 10, cancel_button_2_rect.y + 15))
            # 渲染暗黑风险卡
            infantry_card_dark_image_path = os.path.join(image_directory, 'infantry_card_dark.png')
            infantry_card_dark_image = load_image_with_alpha(infantry_card_dark_image_path, scale_factor=2)
            screen.blit(infantry_card_dark_image, (400, 300))

            cavalry_card_dark_image_path = os.path.join(image_directory, 'cavalry_card_dark.png')
            cavalry_card_dark_image = load_image_with_alpha(cavalry_card_dark_image_path, scale_factor=2)
            screen.blit(cavalry_card_dark_image, (500, 300))

            artillery_card_dark_image_path = os.path.join(image_directory, 'artillery_card_dark.png')
            artillery_card_dark_image = load_image_with_alpha(artillery_card_dark_image_path, scale_factor=2)
            screen.blit(artillery_card_dark_image, (600, 300))

            wild_card_dark_image_path = os.path.join(image_directory, 'wild_card_dark.png')
            wild_card_dark_image = load_image_with_alpha(wild_card_dark_image_path, scale_factor=2)
            screen.blit(wild_card_dark_image, (700, 300))
            # 渲染加减号
            minus_1_image_path = os.path.join(image_directory, 'minus_1.png')
            minus_1_image = load_image_with_alpha(minus_1_image_path, scale_factor=0.4)
            minus_1_rect.size = minus_1_image.get_size()
            screen.blit(minus_1_image, minus_1_rect.topleft)
            plus_1_image_path = os.path.join(image_directory, 'plus_1.png')
            plus_1_image = load_image_with_alpha(plus_1_image_path, scale_factor=0.4)
            plus_1_rect.size = plus_1_image.get_size()
            screen.blit(plus_1_image, plus_1_rect.topleft)
            choose_infantry_text = font.render(str(choose_infantry), True, (255, 255, 255))  # 白色数字
            screen.blit(choose_infantry_text, (460, 440))

            minus_2_image_path = os.path.join(image_directory, 'minus_2.png')
            minus_2_image = load_image_with_alpha(minus_2_image_path, scale_factor=0.4)
            minus_2_rect.size = minus_2_image.get_size()
            screen.blit(minus_2_image, minus_2_rect.topleft)
            plus_2_image_path = os.path.join(image_directory, 'plus_2.png')
            plus_2_image = load_image_with_alpha(plus_2_image_path, scale_factor=0.4)
            plus_2_rect.size = plus_2_image.get_size()
            screen.blit(plus_2_image, plus_2_rect.topleft)
            choose_cavalry_text = font.render(str(choose_cavalry), True, (255, 255, 255))  # 白色数字
            screen.blit(choose_cavalry_text, (560, 440))

            minus_3_image_path = os.path.join(image_directory, 'minus_3.png')
            minus_3_image = load_image_with_alpha(minus_3_image_path, scale_factor=0.4)
            minus_3_rect.size = minus_3_image.get_size()
            screen.blit(minus_3_image, minus_3_rect.topleft)
            plus_3_image_path = os.path.join(image_directory, 'plus_3.png')
            plus_3_image = load_image_with_alpha(plus_3_image_path, scale_factor=0.4)
            plus_3_rect.size = plus_3_image.get_size()
            screen.blit(plus_3_image, plus_3_rect.topleft)
            choose_artillery_text = font.render(str(choose_artillery), True, (255, 255, 255))  # 白色数字
            screen.blit(choose_artillery_text, (660, 440))

            minus_4_image_path = os.path.join(image_directory, 'minus_4.png')
            minus_4_image = load_image_with_alpha(minus_4_image_path, scale_factor=0.4)
            minus_4_rect.size = minus_4_image.get_size()
            screen.blit(minus_4_image, minus_4_rect.topleft)
            plus_4_image_path = os.path.join(image_directory, 'plus_4.png')
            plus_4_image = load_image_with_alpha(plus_4_image_path, scale_factor=0.4)
            plus_4_rect.size = plus_4_image.get_size()
            screen.blit(plus_4_image, plus_4_rect.topleft)
            choose_wild_text = font.render(str(choose_wild), True, (255, 255, 255))  # 白色数字
            screen.blit(choose_wild_text, (760, 440))

            # 渲染拥有卡牌数
            infantry_card_num_text = font.render(str(infantry_card_num), True, (255, 255, 255))  # 白色数字
            screen.blit(infantry_card_num_text, (450, 280))
            artillery_card_num_text = font.render(str(artillery_card_num), True, (255, 255, 255))  # 白色数字
            screen.blit(artillery_card_num_text, (650, 280))  # 调整位置以适应你的布局
            cavalry_card_num_text = font.render(str(cavalry_card_num), True, (255, 255, 255))  # 白色数字
            screen.blit(cavalry_card_num_text, (550, 280))  # 调整位置以适应你的布局
            wild_card_num_text = font.render(str(wild_card_num), True, (255, 255, 255))  # 白色数字
            screen.blit(wild_card_num_text, (750, 280))  # 调整位置以适应你的布局

            for card in player_1_cards:
                if card == 'infantry_card':
                    globals()['infantry_card'] = True
                elif card == 'cavalry_card':
                    globals()['cavalry_card'] = True
                elif card == 'artillery_card':
                    globals()['artillery_card'] = True
                elif card == 'wild_card':
                    globals()['wild_card'] = True
            # 取消点击逻辑
            if cancel_button_2_rect.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN:
                render_risk_card_board = False
                infantry_card = False
                cavalry_card = False
                artillery_card = False
                wild_card = False
                choose_wild = 0
                choose_artillery = 0
                choose_infantry = 0
                choose_cavalry = 0
                using_cards = []

            if confirm_button_2_rect.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN:
                infantry_card_count = using_cards.count("infantry_card")
                wild_card_count = using_cards.count("wild_card")
                cavalry_card_count = using_cards.count("cavalry_card")
                artillery_card_count = using_cards.count("artillery_card")
                if infantry_card_count == 1 and cavalry_card_count == 1 and artillery_card_count == 1:
                    # 如果有，读取adding_times的值
                    if adding_times < 5:
                        risk_adding_army = 4 + 2 * adding_times
                    elif adding_times == 5:
                        risk_adding_army = 15
                    else:
                        risk_adding_army = 20
                    adding_times += 1

                    # 移除使用的卡牌
                    using_cards.remove("infantry_card")
                    using_cards.remove("cavalry_card")
                    using_cards.remove("artillery_card")
                    player_1_cards.remove("infantry_card")
                    player_1_cards.remove("cavalry_card")
                    player_1_cards.remove("artillery_card")
                    # 重置选择的卡牌数量
                    choose_wild = 0
                    choose_artillery = 0
                    choose_infantry = 0
                    choose_cavalry = 0
                    infantry_card_num -= 1
                    cavalry_card_num -= 1
                    artillery_card_num -= 1
                    render_risk_card_board = False
                    infantry_card = False
                    cavalry_card = False
                    artillery_card = False
                    wild_card = False
                    print("匹配成功")
                elif infantry_card_count == 1 and cavalry_card_count == 1 and wild_card_count == 1:
                    if adding_times < 5:
                        risk_adding_army = 4 + 2 * adding_times
                    elif adding_times == 5:
                        risk_adding_army = 15
                    else:
                        risk_adding_army = 20
                    adding_times += 1
                    using_cards.remove("infantry_card")
                    using_cards.remove("cavalry_card")
                    using_cards.remove("wild_card")
                    player_1_cards.remove("infantry_card")
                    player_1_cards.remove("cavalry_card")
                    player_1_cards.remove("wild_card")
                    choose_wild = 0
                    choose_artillery = 0
                    choose_infantry = 0
                    choose_cavalry = 0
                    infantry_card_num -= 1
                    cavalry_card_num -= 1
                    wild_card_num -= 1
                    render_risk_card_board = False
                    infantry_card = False
                    cavalry_card = False
                    artillery_card = False
                    wild_card = False
                    print("匹配成功")
                elif infantry_card_count == 1 and artillery_card_count == 1 and wild_card_count == 1:
                    if adding_times < 5:
                        risk_adding_army = 4 + 2 * adding_times
                    elif adding_times == 5:
                        risk_adding_army = 15
                    else:
                        risk_adding_army = 20
                    adding_times += 1
                    using_cards.remove("infantry_card")
                    using_cards.remove("artillery_card")
                    using_cards.remove("wild_card")
                    player_1_cards.remove("infantry_card")
                    player_1_cards.remove("artillery_card")
                    player_1_cards.remove("wild_card")
                    choose_wild = 0
                    choose_artillery = 0
                    choose_infantry = 0
                    choose_cavalry = 0
                    infantry_card_num -= 1
                    wild_card_num -= 1
                    artillery_card_num -= 1
                    render_risk_card_board = False
                    infantry_card = False
                    cavalry_card = False
                    artillery_card = False
                    wild_card = False
                    print("匹配成功")
                elif cavalry_card_count == 1 and wild_card_count == 1 and artillery_card_count == 1:
                    if adding_times < 5:
                        risk_adding_army = 4 + 2 * adding_times
                    elif adding_times == 5:
                        risk_adding_army = 15
                    else:
                        risk_adding_army = 20
                    adding_times += 1
                    using_cards.remove("cavalry_card")
                    using_cards.remove("artillery_card")
                    using_cards.remove("wild_card")
                    player_1_cards.remove("cavalry_card")
                    player_1_cards.remove("artillery_card")
                    player_1_cards.remove("wild_card")
                    choose_wild = 0
                    choose_artillery = 0
                    choose_infantry = 0
                    choose_cavalry = 0
                    wild_card_num -= 1
                    cavalry_card_num -= 1
                    artillery_card_num -= 1
                    render_risk_card_board = False
                    infantry_card = False
                    cavalry_card = False
                    artillery_card = False
                    wild_card = False
                    print("匹配成功")
                elif infantry_card_count == 3:
                    if adding_times < 5:
                        risk_adding_army = 4 + 2 * adding_times
                    elif adding_times == 5:
                        risk_adding_army = 15
                    else:
                        risk_adding_army = 20
                    adding_times += 1
                    using_cards.remove("infantry_card")
                    using_cards.remove("infantry_card")
                    using_cards.remove("infantry_card")
                    player_1_cards.remove("infantry_card")
                    player_1_cards.remove("infantry_card")
                    player_1_cards.remove("infantry_card")
                    choose_wild = 0
                    choose_artillery = 0
                    choose_infantry = 0
                    choose_cavalry = 0
                    infantry_card_num -= 3
                    render_risk_card_board = False
                    print("匹配成功")
                elif cavalry_card_count == 3:
                    if adding_times < 5:
                        risk_adding_army = 4 + 2 * adding_times
                    elif adding_times == 5:
                        risk_adding_army = 15
                    else:
                        risk_adding_army = 20
                    adding_times += 1
                    using_cards.remove("cavalry_card")
                    using_cards.remove("cavalry_card")
                    using_cards.remove("cavalry_card")
                    player_1_cards.remove("cavalry_card")
                    player_1_cards.remove("cavalry_card")
                    player_1_cards.remove("cavalry_card")
                    choose_wild = 0
                    choose_artillery = 0
                    choose_infantry = 0
                    choose_cavalry = 0
                    cavalry_card_num -= 3
                    render_risk_card_board = False
                    infantry_card = False
                    cavalry_card = False
                    artillery_card = False
                    wild_card = False
                    print("匹配成功")
                elif artillery_card_count == 3:
                    if adding_times < 5:
                        risk_adding_army = 4 + 2 * adding_times
                    elif adding_times == 5:
                        risk_adding_army = 15
                    else:
                        risk_adding_army = 20
                    adding_times += 1
                    using_cards.remove("artillery_card")
                    using_cards.remove("artillery_card")
                    using_cards.remove("artillery_card")
                    player_1_cards.remove("artillery_card")
                    player_1_cards.remove("artillery_card")
                    player_1_cards.remove("artillery_card")
                    choose_wild = 0
                    choose_artillery = 0
                    choose_infantry = 0
                    choose_cavalry = 0
                    artillery_card_num -= 3
                    render_risk_card_board = False
                    infantry_card = False
                    cavalry_card = False
                    artillery_card = False
                    wild_card = False
                    print("匹配成功")
                elif wild_card_count == 3:
                    if adding_times < 5:
                        risk_adding_army = 4 + 2 * adding_times
                    elif adding_times == 5:
                        risk_adding_army = 15
                    else:
                        risk_adding_army = 20
                    adding_times += 1
                    using_cards.remove("wild_card")
                    using_cards.remove("wild_card")
                    using_cards.remove("wild_card")
                    player_1_cards.remove("wild_card")
                    player_1_cards.remove("wild_card")
                    player_1_cards.remove("wild_card")
                    choose_wild = 0
                    choose_artillery = 0
                    choose_infantry = 0
                    choose_cavalry = 0
                    wild_card_num -= 3
                    render_risk_card_board = False
                    infantry_card = False
                    cavalry_card = False
                    artillery_card = False
                    wild_card = False
                    print("匹配成功")
                elif infantry_card_count == 2 and wild_card_count == 1:
                    if adding_times < 5:
                        risk_adding_army = 4 + 2 * adding_times
                    elif adding_times == 5:
                        risk_adding_army = 15
                    else:
                        risk_adding_army = 20
                    adding_times += 1
                    using_cards.remove("infantry_card")
                    using_cards.remove("infantry_card")
                    using_cards.remove("wild_card")
                    player_1_cards.remove("infantry_card")
                    player_1_cards.remove("infantry_card")
                    player_1_cards.remove("wild_card")
                    choose_wild = 0
                    choose_artillery = 0
                    choose_infantry = 0
                    choose_cavalry = 0
                    infantry_card_num -= 2
                    wild_card_num -= 1
                    render_risk_card_board = False
                    infantry_card = False
                    cavalry_card = False
                    artillery_card = False
                    wild_card = False
                    print("匹配成功")
                elif cavalry_card_count == 2 and wild_card_count == 1:
                    if adding_times < 5:
                        risk_adding_army = 4 + 2 * adding_times
                    elif adding_times == 5:
                        risk_adding_army = 15
                    else:
                        risk_adding_army = 20
                    adding_times += 1
                    using_cards.remove("cavalry_card")
                    using_cards.remove("cavalry_card")
                    using_cards.remove("wild_card")
                    player_1_cards.remove("cavalry_card")
                    player_1_cards.remove("cavalry_card")
                    player_1_cards.remove("wild_card")
                    choose_wild = 0
                    choose_artillery = 0
                    choose_infantry = 0
                    choose_cavalry = 0
                    wild_card_num -= 1
                    cavalry_card_num -= 2
                    render_risk_card_board = False
                    infantry_card = False
                    cavalry_card = False
                    artillery_card = False
                    wild_card = False
                    print("匹配成功")
                elif wild_card_count == 1 and artillery_card_count == 2:
                    if adding_times < 5:
                        risk_adding_army = 4 + 2 * adding_times
                    elif adding_times == 5:
                        risk_adding_army = 15
                    else:
                        risk_adding_army = 20
                    adding_times += 1
                    using_cards.remove("artillery_card")
                    using_cards.remove("artillery_card")
                    using_cards.remove("wild_card")
                    player_1_cards.remove("artillery_card")
                    player_1_cards.remove("artillery_card")
                    player_1_cards.remove("wild_card")
                    choose_wild = 0
                    choose_artillery = 0
                    choose_infantry = 0
                    choose_cavalry = 0
                    wild_card_num -= 1
                    artillery_card_num -= 2
                    render_risk_card_board = False
                    infantry_card = False
                    cavalry_card = False
                    artillery_card = False
                    wild_card = False
                    print("匹配成功")
                elif infantry_card_count == 1 and wild_card_count == 2:
                    if adding_times < 5:
                        risk_adding_army = 4 + 2 * adding_times
                    elif adding_times == 5:
                        risk_adding_army = 15
                    else:
                        risk_adding_army = 20
                    adding_times += 1
                    using_cards.remove("wild_card")
                    using_cards.remove("wild_card")
                    using_cards.remove("infantry_card")
                    player_1_cards.remove("wild_card")
                    player_1_cards.remove("wild_card")
                    player_1_cards.remove("infantry_card")
                    choose_wild = 0
                    choose_artillery = 0
                    choose_infantry = 0
                    choose_cavalry = 0
                    wild_card_num -= 2
                    infantry_card_num -= 1
                    render_risk_card_board = False
                    infantry_card = False
                    cavalry_card = False
                    artillery_card = False
                    wild_card = False
                    print("匹配成功")
                elif cavalry_card_count == 1 and wild_card_count == 2:
                    if adding_times < 5:
                        risk_adding_army = 4 + 2 * adding_times
                    elif adding_times == 5:
                        risk_adding_army = 15
                    else:
                        risk_adding_army = 20
                    adding_times += 1
                    using_cards.remove("wild_card")
                    using_cards.remove("wild_card")
                    using_cards.remove("cavalry_card")
                    player_1_cards.remove("wild_card")
                    player_1_cards.remove("wild_card")
                    player_1_cards.remove("cavalry_card")
                    choose_wild = 0
                    choose_artillery = 0
                    choose_infantry = 0
                    choose_cavalry = 0
                    wild_card_num -= 2
                    cavalry_card_num -= 1
                    render_risk_card_board = False
                    infantry_card = False
                    cavalry_card = False
                    artillery_card = False
                    wild_card = False
                    print("匹配成功")
                elif wild_card_count == 2 and artillery_card_count == 1:
                    if adding_times < 5:
                        risk_adding_army = 4 + 2 * adding_times
                    elif adding_times == 5:
                        risk_adding_army = 15
                    else:
                        risk_adding_army = 20
                    adding_times += 1
                    using_cards.remove("wild_card")
                    using_cards.remove("wild_card")
                    using_cards.remove("artillery_card")
                    player_1_cards.remove("wild_card")
                    player_1_cards.remove("wild_card")
                    player_1_cards.remove("artillery_card")
                    choose_wild = 0
                    choose_artillery = 0
                    choose_infantry = 0
                    choose_cavalry = 0
                    wild_card_num -= 2
                    artillery_card_num -= 1
                    render_risk_card_board = False
                    infantry_card = False
                    cavalry_card = False
                    artillery_card = False
                    wild_card = False
                    print("匹配成功")
                else:
                    print("匹配失败")
        if infantry_card:
            infantry_card_image_path = os.path.join(image_directory, 'infantry_card.png')
            infantry_card_image = load_image_with_alpha(infantry_card_image_path, scale_factor=2)
            infantry_card_rect.size = infantry_card_dark_image.get_size()
            screen.blit(infantry_card_image, infantry_card_rect.topleft)
        if cavalry_card:
            cavalry_card_image_path = os.path.join(image_directory, 'cavalry_card.png')
            cavalry_card_image = load_image_with_alpha(cavalry_card_image_path, scale_factor=2)
            cavalry_card_rect.size = cavalry_card_dark_image.get_size()
            screen.blit(cavalry_card_image, cavalry_card_rect.topleft)
        if artillery_card:
            artillery_card_image_path = os.path.join(image_directory, 'artillery_card.png')
            artillery_card_image = load_image_with_alpha(artillery_card_image_path, scale_factor=2)
            artillery_card_rect.size = artillery_card_dark_image.get_size()
            screen.blit(artillery_card_image, artillery_card_rect.topleft)
        if wild_card:
            wild_card_image_path = os.path.join(image_directory, 'wild_card.png')
            wild_card_image = load_image_with_alpha(wild_card_image_path, scale_factor=2)
            wild_card_rect.size = wild_card_dark_image.get_size()
            screen.blit(wild_card_image, wild_card_rect.topleft)

            # 设置confirm逻辑

        # 渲染移动军队面板
        if render_move_army_number:
            move_army_number_path = os.path.join(image_directory, 'move_army_number.png')
            move_army_number_image = load_image_with_alpha(move_army_number_path, scale_factor=1.4)
            # 假设你已经有了渲染位置
            render_position = (350, 200)  # 你需要根据实际情况设置x和y的值
            screen.blit(move_army_number_image, render_position)
            # 渲染移动军队页面的concentrateon军队数量
            concentrate_on_parts = concentrate_on.split('_')
            concentrate_on_name = ' '.join(concentrate_on_parts[1:])
            army_concentrate_on_num = globals().get(f"army_{'_'.join(concentrate_on_parts[1:])}", 0)
            show_concentrate_on_name = f" {concentrate_on_name}:{army_concentrate_on_num}"  # 文本内容
            show_concentrate_on_name_surface = font.render(show_concentrate_on_name, True, (255, 255, 255))  # 白色文本
            show_concentrate_on_name_position = (370, 350)  # 文本位置，根据需要调整，这里假设在滑块活动范围上方30像素处
            screen.blit(show_concentrate_on_name_surface, show_concentrate_on_name_position)
            # selected的军队数量
            selected_layer_parts = selected_layer_within_180_pixels.split('_')  # 分割concentrateon
            selected_layer_name = ' '.join(selected_layer_parts[1:])  # 将空格转化，形如area Alaska
            army_selected_num = globals().get(f"army_{'_'.join(selected_layer_parts[1:])}",
                                              0)  # 将分割出来的concentrateon替换成army_
            show_selected_name = f" {selected_layer_name}:{army_selected_num}"  # 最终显示
            show_selected_name_surface = font.render(show_selected_name, True, (255, 255, 255))  # 白色文本
            show_selected_name_position = (700, 350)  # 文本位置，根据需要调整，这里假设在滑块活动范围上方30像素处
            screen.blit(show_selected_name_surface, show_selected_name_position)

            # 渲染白色滑块
            white_slider_surface = pygame.Surface((50, 30))
            white_slider_surface.fill((255, 255, 255))
            screen.blit(white_slider_surface, slider_position)
            pygame.draw.rect(screen, (200, 200, 200), (min_x, top_y, slider_range_width, bottom_y - top_y), 2)
            # 渲染文本
            concentrate_on_leave = max(1, army_concentrate_on_num - int(
                slider_progress_percentage / 100 * army_concentrate_on_num))
            text = f"Move from: {slider_progress_percentage}% , leave {concentrate_on_leave}"  # 文本内容
            text_surface = font.render(text, True, (255, 255, 255))  # 白色文本
            text_position = (370, 270)  # 文本位置
            screen.blit(text_surface, text_position)
            selected_leave = max(1, army_selected_num + int(slider_progress_percentage / 100 * army_concentrate_on_num))
            text_2 = f"Move to: {inverse_slider_progress_percentage}% , leave {selected_leave}"  # 文本内容
            text_surface_2 = font.render(text_2, True, (255, 255, 255))  # 白色文本
            text_position_2 = (680, 270)  # 文本位置
            screen.blit(text_surface_2, text_position_2)
            render_move_army_buttons(screen)

            pygame.display.flip()
            clock.tick(120)

        # 渲染回合
        if render_round:
            font_large = pygame.font.Font(None, 50)

            round_path = os.path.join(image_directory, "round.png")
            round_image = load_image_with_alpha(round_path, scale_factor=1.4)
            round_position = (20, 10)  # 假设这是你想要的位置
            screen.blit(round_image, round_position)
            round_txt = "ROUNDS LEFT"
            round_txt_surface = font.render(round_txt, True, (255, 255, 255))  # 白色文本
            round_txt_position = (20, 30)  # 文本位置，根据需要调整
            screen.blit(round_txt_surface, round_txt_position)
            show_round_num = f"{render_round_num}"  # 正确使用f-string格式化字符串
            round_num_surface = font_large.render(show_round_num, True, (255, 255, 255))  # 白色文本
            round_num_position = (40, 50)  # 文本位置，根据需要调整
            screen.blit(round_num_surface, round_num_position)

        # 渲染结算页面
        if render_ending:
            ending_path = os.path.join(image_directory, "ending.png")
            ending_image = load_image_with_alpha(ending_path, scale_factor=1.4)
            ending_position = (350, 200)  # 假设这是你想要的位置
            screen.blit(ending_image, ending_position)

            if playing_result == "some_one_lost":
                # 渲染电脑玩家输的提示词
                some_one_lost_text = f"loser set {loser}"  # 文本内容
                some_one_lost_text_surface = font.render(some_one_lost_text, True, (255, 255, 255))  # 白色文本
                some_one_lost_text_position = (680, 270)  # 文本位置
                screen.blit(some_one_lost_text_surface, some_one_lost_text_position)
            elif playing_result == "win":
                # 渲染我赢的提示词
                win_text = f"You win the game!"  # 文本内容
                win_text_surface = font.render(win_text, True, (255, 255, 255))  # 白色文本
                win_text_position = (680, 270)  # 文本位置
                screen.blit(win_text_surface, win_text_position)
            elif playing_result == "lost":
                lost_text = f"You lost the game!"  # 文本内容
                lost_text_surface = font.render(lost_text, True, (255, 255, 255))  # 白色文本
                lost_text_position = (680, 270)  # 文本位置
                screen.blit(lost_text_surface, lost_text_position)
            elif playing_result == "no_winner":
                no_winner_text = f"No winner!"  # 文本内容
                no_winner_text_surface = font.render(no_winner_text, True, (255, 255, 255))  # 白色文本
                no_winner_text_position = (680, 270)  # 文本位置
                screen.blit(no_winner_text_surface, no_winner_text_position)

        if attack_board_visible:
            attack_board_path = os.path.join(image_directory, "attack_board.png")
            attack_board_image = load_image_with_alpha(attack_board_path, scale_factor=1.4)
            attack_board_position = (350, 200)  # 假设这是你想要的位置
            screen.blit(attack_board_image, attack_board_position)

            # 渲染文本
            if concentrate_on is not None and selected_layer_within_180_pixels is not None:
                # 格式化图层名
                formatted_concentrate_on = format_layer_name(concentrate_on)
                formatted_selected_layer = format_layer_name(selected_layer_within_180_pixels)

                text = f"{formatted_concentrate_on} attacking {formatted_selected_layer}"
                text_surface = font.render(text, True, (255, 255, 255))  # 白色文本
                text_position = (400, 250)  # 文本位置，根据需要调整
                screen.blit(text_surface, text_position)

                # 渲染左边攻击目标的军队数量，注意这里用到的格式化图层名跟formatted不同
                army_var_name_left = "army_" + concentrate_on.split("_", 1)[1]
                army_count_left = globals().get(army_var_name_left, 0)  # 如果变量不存在，则默认为0
                army_text_left = f"{formatted_concentrate_on}: {army_count_left}"
                army_text_surface_left = font.render(army_text_left, True, (255, 255, 255))  # 白色文本
                army_text_position_left = (380, 450)  # 新文本位置，稍微下移以避免重叠
                screen.blit(army_text_surface_left, army_text_position_left)

                # 同理，渲染右边的
                army_var_name_right = "army_" + selected_layer_within_180_pixels.split("_", 1)[1]
                army_count_right = globals().get(army_var_name_right, 0)  # 如果变量不存在，则默认为0
                army_text_right = f"{formatted_selected_layer}: {army_count_right}"
                army_text_surface_right = font.render(army_text_right, True, (255, 255, 255))  # 白色文本
                army_text_position_right = (750, 450)  # 新文本位置，稍微下移以避免重叠
                screen.blit(army_text_surface_right, army_text_position_right)

            if concentrate_on in player_1:
                red_army_image_path = os.path.join(image_directory, "red_army_left.png")
                red_army_position = (400, 300)  # red_army_left的位置
                red_army_image = load_image_with_alpha(red_army_image_path, scale_factor=0.1)  # 假设这是加载图片并设置透明度的函数
                screen.blit(red_army_image, red_army_position)
                # 新增的条件判断
                if selected_layer_within_180_pixels in player_2:
                    green_army_image_path = os.path.join(image_directory, "green_army_right.png")
                    green_army_image = load_image_with_alpha(green_army_image_path,
                                                             scale_factor=0.1)  # 加载图片并调整大小为原来的0.1倍
                    green_army_position = (740, 300)
                    screen.blit(green_army_image, green_army_position)
                elif selected_layer_within_180_pixels in player_3:
                    brown_army_image_path = os.path.join(image_directory, "brown_army_right.png")
                    brown_army_image = load_image_with_alpha(brown_army_image_path,
                                                             scale_factor=0.1)  # 加载图片并调整大小为原来的0.1倍
                    brown_army_position = (740, 300)
                    screen.blit(brown_army_image, brown_army_position)
                elif selected_layer_within_180_pixels in player_4:
                    yellow_army_image_path = os.path.join(image_directory, "yellow_army_right.png")
                    yellow_army_image = load_image_with_alpha(yellow_army_image_path,
                                                              scale_factor=0.1)  # 加载图片并调整大小为原来的0.1倍
                    yellow_army_position = (740, 300)
                    screen.blit(yellow_army_image, yellow_army_position)
                elif selected_layer_within_180_pixels in player_5:
                    orange_army_image_path = os.path.join(image_directory, "orange_army_right.png")
                    orange_army_image = load_image_with_alpha(orange_army_image_path,
                                                              scale_factor=0.1)  # 加载图片并调整大小为原来的0.1倍
                    orange_army_position = (740, 300)
                    screen.blit(orange_army_image, orange_army_position)
                elif selected_layer_within_180_pixels in player_6:
                    purple_army_image_path = os.path.join(image_directory, "purple_army_right.png")
                    purple_army_image = load_image_with_alpha(purple_army_image_path,
                                                              scale_factor=0.1)  # 加载图片并调整大小为原来的0.1倍
                    brown_army_position = (740, 300)
                    screen.blit(purple_army_image, purple_army_position)

            elif selected_layer_within_180_pixels in player_1:
                red_army_image_path = os.path.join(image_directory, "red_army_right.png")
                red_army_position = (740, 300)  # red_army_right的位置
                red_army_image = load_image_with_alpha(red_army_image_path, scale_factor=0.1)
                screen.blit(red_army_image, red_army_position)
                army_image_path = None
                army_position = (400, 300)  # 所有军队图片的统一位置

                if concentrate_on in player_2:
                    army_image_path = os.path.join(image_directory, "green_army_left.png")
                elif concentrate_on in player_3:
                    army_image_path = os.path.join(image_directory, "brown_army_left.png")
                elif concentrate_on in player_4:
                    army_image_path = os.path.join(image_directory, "yellow_army_left.png")
                elif concentrate_on in player_5:
                    army_image_path = os.path.join(image_directory, "orange_army_left.png")
                elif concentrate_on in player_6:
                    army_image_path = os.path.join(image_directory, "purple_army_left.png")

                if army_image_path:
                    army_image = load_image_with_alpha(army_image_path, scale_factor=0.1)  # 加载图片并可能应用透明度设置
                    screen.blit(army_image, army_position)
        if show_explosion_2:
            explosion_1_image_path = os.path.join(image_directory, "explosion_1.png")
            explosion_1_position = (650, 300)  # explosion的位置
            explosion_1_image = load_image_with_alpha(explosion_1_image_path, scale_factor=0.1)
            screen.blit(explosion_1_image, explosion_1_position)

        if show_explosion_1:
            explosion_1_image_path = os.path.join(image_directory, "explosion_1.png")
            explosion_1_position = (550, 300)  # explosion的位置
            explosion_1_image = load_image_with_alpha(explosion_1_image_path, scale_factor=0.1)
            screen.blit(explosion_1_image, explosion_1_position)

        if show_explosion_3:
            explosion_2_image_path = os.path.join(image_directory, "explosion_2.png")
            explosion_2_position = (550, 400)  # explosion的位置
            explosion_2_image = load_image_with_alpha(explosion_2_image_path, scale_factor=0.1)
            screen.blit(explosion_2_image, explosion_2_position)

        if show_explosion_4:
            explosion_2_image_path = os.path.join(image_directory, "explosion_2.png")
            explosion_2_position = (650, 400)  # explosion的位置
            explosion_2_image = load_image_with_alpha(explosion_2_image_path, scale_factor=0.1)
            screen.blit(explosion_2_image, explosion_2_position)

        if final_point_layer_1 is not None:
            # 定义最终点数图层需要渲染的位置
            position = (550, 300)
            image_path = os.path.join(image_directory, f"{final_point_layer_1}.png")
            image = load_image_with_alpha(image_path, scale_factor=0.5)
            screen.blit(image, position)

        if final_point_layer_2 is not None:
            # 定义最终点数图层需要渲染的位置
            position = (650, 300)
            image_path = os.path.join(image_directory, f"{final_point_layer_2}.png")
            image = load_image_with_alpha(image_path, scale_factor=0.5)
            screen.blit(image, position)

        if final_point_layer_3 is not None:
            # 定义最终点数图层需要渲染的位置
            position = (550, 400)
            image_path = os.path.join(image_directory, f"{final_point_layer_3}.png")
            image = load_image_with_alpha(image_path, scale_factor=0.5)
            screen.blit(image, position)

        if final_point_layer_4 is not None:
            # 定义最终点数图层需要渲染的位置
            position = (650, 400)
            image_path = os.path.join(image_directory, f"{final_point_layer_4}.png")
            image = load_image_with_alpha(image_path, scale_factor=0.5)
            screen.blit(image, position)

        if attack_board_visible:
            draw_rolling_button(screen)
            render_dice_images_1(screen, image_directory)
            render_dice_images_2(screen, image_directory)
            render_dice_images_3(screen, image_directory)
            render_dice_images_4(screen, image_directory)

        if increasing_brightness:
            brightness_value += brightness_increment
            if brightness_value >= 60:
                brightness_value = 60
                increasing_brightness = False
        else:
            brightness_value -= brightness_increment
            if brightness_value <= 0:
                brightness_value = 0
                increasing_brightness = True

        pygame.display.flip()
        clock.tick(120)
