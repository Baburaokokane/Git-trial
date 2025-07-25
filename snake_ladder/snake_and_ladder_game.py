import pygame
import random
import sys
import os
import time
print("hello")

pygame.init()
pygame.mixer.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 900, 600
WINDOW = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Modern Snake and Ladder Game")

player_images = [
    pygame.image.load(r"C:\Toshal\devlopment\MINE\snake_ladder\assets\avatars\player1.jpg"),
    pygame.image.load(r"C:\Toshal\devlopment\MINE\snake_ladder\assets\avatars\bot.jpg"),
    pygame.image.load(r'C:\Toshal\devlopment\MINE\snake_ladder\assets\avatars\player2.jpg'),
]

dice_images = [
    pygame.image.load(r"C:\Toshal\devlopment\MINE\snake_ladder\assets\dice\dice1.jpg"),
    pygame.image.load(r"C:\Toshal\devlopment\MINE\snake_ladder\assets\dice\dice2.jpg"),
    pygame.image.load(r"C:\Toshal\devlopment\MINE\snake_ladder\assets\dice\dice3.jpg"),
    pygame.image.load(r"C:\Toshal\devlopment\MINE\snake_ladder\assets\dice\dice4.jpg"),
    pygame.image.load(r"C:\Toshal\devlopment\MINE\snake_ladder\assets\dice\dice5.jpg"),
    pygame.image.load(r"C:\Toshal\devlopment\MINE\snake_ladder\assets\dice\dice6.jpg"),
]

dice_sound = pygame.mixer.Sound(r"C:\Toshal\devlopment\MINE\snake_ladder\assets\sounds\dice_roll.mp3")
snake_sound = pygame.mixer.Sound(r"C:\Toshal\devlopment\MINE\snake_ladder\assets\sounds\snake_hiss.mp3")
ladder_sound = pygame.mixer.Sound(r"C:\Toshal\devlopment\MINE\snake_ladder\assets\sounds\ladder_climb.mp3")
win_sound = pygame.mixer.Sound(r"C:\Toshal\devlopment\MINE\snake_ladder\assets\sounds\game_win.mp3")

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake and Ladder - DSA Mini Project")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
GREY = (200, 200, 200)
DARK_GREY = (40, 40, 40)

FONT = pygame.font.SysFont("arial", 24)
BIG_FONT = pygame.font.SysFont("comicsansms", 40)

def get_board_position(pos):
    row = (pos - 1) // 10
    col = (pos - 1) % 10 if row % 2 == 0 else 9 - (pos - 1) % 10
    x = col * 50 + 50
    y = 550 - row * 50
    return x, y

def move_player_animation(player_pos, new_pos, player_index):
    while player_pos < new_pos:
        player_pos += 1
        draw_board()
        draw_players([player_pos if i == player_index else positions[i] for i in range(3)])
        pygame.display.update()
        time.sleep(0.1)
    return new_pos

def draw_players(pos_list):
    for i, pos in enumerate(pos_list):
        if pos == 0:
            continue
        x, y = get_board_position(pos)
        WINDOW.blit(pygame.transform.scale(player_images[i], (40, 40)), (x, y - 20))

def draw_side_panel(current_player, dice_val):
    pygame.draw.rect(WINDOW, DARK_GREY, (600, 0, 300, SCREEN_HEIGHT))
    title = BIG_FONT.render("Dashboard", True, WHITE)
    WINDOW.blit(title, (550, 10))
    labels = ["You", "Bot", "Player 2"]
    for i in range(3):
        pygame.draw.circle(WINDOW, WHITE, (630, 80 + i * 80), 20)
        avatar = pygame.transform.scale(player_images[i], (40, 40))
        WINDOW.blit(avatar, (610, 60 + i * 80))
        label = FONT.render(labels[i], True, WHITE)
        WINDOW.blit(label, (660, 65 + i * 80))
    turn_text = FONT.render(f"Turn: {labels[current_player]}", True, GREEN)
    WINDOW.blit(turn_text, (630, 350))
    if dice_val is not None:
        if dice_val > 0:
            dice_display = pygame.transform.scale(dice_images[dice_val - 1], (50, 50))
            WINDOW.blit(dice_display, (170, 20))
    ds_start_y = 380
    ds_title = FONT.render("Data Structures:", True, CYAN)
    WINDOW.blit(ds_title, (550, ds_start_y))
    ds_list = [
        "player_images: list of avatar images",
        "dice_images: list of dice images",
        "snakes: dict mapping snake head->tail",
        "ladders: dict mapping ladder start->end",
        "positions: list of current positions"
    ]
    for idx, text in enumerate(ds_list):
        ds_text = FONT.render(text, True, WHITE)
        WINDOW.blit(ds_text, (550, ds_start_y + 30 + idx * 25))
    note_text = FONT.render("Red lines: Snake, Green lines: Ladder", True, YELLOW)
    WINDOW.blit(note_text, (550, ds_start_y + 30 + len(ds_list) * 25 + 10))

def draw_board():
    BOARD_X = 50
    BOARD_Y = 100
    BOARD_WIDTH = 500
    BOARD_HEIGHT = 500
    board_rect = pygame.Rect(BOARD_X, BOARD_Y, BOARD_WIDTH, BOARD_HEIGHT)
    pygame.draw.rect(WINDOW, WHITE, board_rect)
    for i in range(1, 101):
        x, y = get_board_position(i)
        pygame.draw.rect(WINDOW, BLACK, (x, y, 50, 50), 1)
        label = FONT.render(str(i), True, BLACK)
        WINDOW.blit(label, (x + 15, y + 15))
    for start, end in snakes.items():
        start_x, start_y = get_board_position(start)
        end_x, end_y = get_board_position(end)
        pygame.draw.line(WINDOW, RED, (start_x + 25, start_y + 25), (end_x + 25, end_y + 25), 5)
    for start, end in ladders.items():
        start_x, start_y = get_board_position(start)
        end_x, end_y = get_board_position(end)
        pygame.draw.line(WINDOW, GREEN, (start_x + 25, start_y + 25), (end_x + 25, end_y + 25), 5)

snakes = {16: 6, 48: 30, 64: 60, 79: 19, 93: 68, 95: 24, 97: 76, 98: 78}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

def check_snake_ladder(pos):
    if pos in snakes:
        pygame.mixer.Sound.play(snake_sound)
        return snakes[pos]
    if pos in ladders:
        pygame.mixer.Sound.play(ladder_sound)
        return ladders[pos]
    return pos

def roll_dice():
    pygame.mixer.Sound.play(dice_sound)
    BOARD_WIDTH = 500
    for _ in range(10):
        roll = random.randint(1, 6)
        draw_board()
        draw_players(positions)
        draw_side_panel(current_player, None)
        WINDOW.blit(dice_images[roll - 1], (0,0))
        pygame.display.update()
        time.sleep(0.1)
    final_roll = random.randint(1, 6)
    draw_board()
    draw_players(positions)
    draw_side_panel(current_player, final_roll)
    WINDOW.blit(dice_images[final_roll - 1], (0,0))
    pygame.display.update()
    time.sleep(1)
    return final_roll

def show_winner(winner_index):
    WINDOW.fill(BLACK)
    win_text = BIG_FONT.render(f"{['You', 'Bot', 'Player 2'][winner_index]} Wins!", True, GREEN)
    WINDOW.blit(win_text, (250, 250))
    pygame.mixer.Sound.play(win_sound)
    restart_btn = FONT.render("Press R to Restart or Q to Quit", True, WHITE)
    WINDOW.blit(restart_btn, (200, 320))
    pygame.display.update()
    waiting = True
    while waiting:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_r:
                    main()
                if e.key == pygame.K_q:
                    pygame.quit()
                    exit()

def animate_move(player_index, start, end):
    if start == end:
        return
    step = 1 if end > start else -1
    for pos in range(start + step, end + step, step):
        positions[player_index] = pos
        draw_board()
        draw_players(positions)
        draw_side_panel(current_player, 0)
        pygame.display.update()
        time.sleep(0.2)

def main():
    global current_player, positions
    positions = [1, 1, 1]
    current_player = 0
    running = True
    while running:
        draw_board()
        draw_players(positions)
        draw_side_panel(current_player, 0)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and current_player == 0:
                if event.key == pygame.K_SPACE:
                    dice = roll_dice()
                    temp = positions[current_player] + dice
                    if temp <= 100:
                        animate_move(current_player, positions[current_player], temp)
                        positions[current_player] = temp
                        new_pos = check_snake_ladder(temp)
                        animate_move(current_player, positions[current_player], new_pos)
                        positions[current_player] = new_pos
                    if positions[current_player] == 100:
                        show_winner(current_player)
                    current_player = 1
        if current_player == 1:
            time.sleep(1)
            dice = roll_dice()
            temp = positions[current_player] + dice
            if temp <= 100:
                animate_move(current_player, positions[current_player], temp)
                positions[current_player] = temp
                new_pos = check_snake_ladder(temp)
                animate_move(current_player, positions[current_player], new_pos)
                positions[current_player] = new_pos
            if positions[current_player] == 100:
                show_winner(current_player)
            current_player = 2
        elif current_player == 2:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                dice = roll_dice()
                temp = positions[current_player] + dice
                if temp <= 100:
                    animate_move(current_player, positions[current_player], temp)
                    positions[current_player] = temp
                    new_pos = check_snake_ladder(temp)
                    animate_move(current_player, positions[current_player], new_pos)
                    positions[current_player] = new_pos
                if positions[current_player] == 100:
                    show_winner(current_player)
                current_player = 0

def show_start_menu():
    while True:
        screen.fill(DARK_GREY)
        title = BIG_FONT.render("Snake & Ladder", True, WHITE)
        screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 100))
        start_text = FONT.render("Press 'S' to Start", True, GREEN)
        screen.blit(start_text, (SCREEN_WIDTH // 2 - start_text.get_width() // 2, 250))
        instr_text = FONT.render("Press 'I' for Instructions", True, CYAN)
        screen.blit(instr_text, (SCREEN_WIDTH // 2 - instr_text.get_width() // 2, 300))
        quit_text = FONT.render("Press 'Q' to Quit", True, RED)
        screen.blit(quit_text, (SCREEN_WIDTH // 2 - quit_text.get_width() // 2, 350))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    return
                elif event.key == pygame.K_i:
                    show_instructions()
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

def show_instructions():
    showing = True
    while showing:
        screen.fill(BLACK)
        instr_title = BIG_FONT.render("Instructions", True, WHITE)
        screen.blit(instr_title, (SCREEN_WIDTH // 2 - instr_title.get_width() // 2, 50))
        lines = [
            "1. You are Player 1 (blue avatar).",
            "2. Player 2 is a Bot (red avatar).",
            "3. Player 3 is another player (green avatar).",
            "4. Press SPACE to roll the dice (Player 1).",
            "5. Bot moves automatically.",
            "6. Player 3 presses ENTER to roll.",
            "7. Land on ladders to climb, snakes to fall.",
            "8. First to reach 100 wins!"
        ]
        for i, line in enumerate(lines):
            line_render = FONT.render(line, True, CYAN)
            screen.blit(line_render, (50, 120 + i * 40))
        back_text = FONT.render("Press B to go Back", True, GREY)
        screen.blit(back_text, (SCREEN_WIDTH // 2 - back_text.get_width() // 2, 500))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_b:
                showing = False

show_start_menu()
main()
pygame.quit()
