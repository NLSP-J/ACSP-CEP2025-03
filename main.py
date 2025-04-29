import random
import word as w

ans = random.choice(w.word_list)

import pygame as pg
import time
pg.init()

win_width = 500
win_height = 650
screen = pg.display.set_mode([win_width, win_height])
pg.display.set_caption('wordle')

white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 0)
gray = (128, 128, 128)

font = pg.font.Font(None, 70)

game_board = [[' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' '], 
              [' ', ' ', ' ', ' ', ' '], 
              [' ', ' ', ' ', ' ', ' '], 
              [' ', ' ', ' ', ' ', ' '], 
              [' ', ' ', ' ', ' ', ' ']]
count = 0
letters = 0
game_over = False
running = True

def draw_board():
    for col in range(5):
        for row in range(10):
            square = pg.Rect(col * 50 + 6, row * 50 + 6, 37, 37)
            pg.draw.rect(screen, white, square, width = 1)

            letter_text = font.render(game_board[row][col], True, gray)
            screen.blit(letter_text, (col * 50 + 15, row * 50))
    rectangle = pg.Rect(5, count * 50 + 3, win_width - 10, 45)
    pg.draw.rect(screen, green, rectangle, width = 1)

def check_match():
    global game_over
    for col in range(5):
        for row in range(10):
            highlight = pg.Rect(col * 50 + 6, row * 50 + 6, 37, 37)
            if ans[col] == game_board[row][col] and count > row:
                pg.draw.rect(screen, green, highlight)
            elif game_board[row][col] in ans and count > row:
                pg.draw.rect(screen, yellow, highlight)
    for row in range(10):
        guess = ''.join(game_board[row])
        if guess == ans and row < count:
            game_over = True

def draw_win():
    global game_over, running
    if count == 10:
        game_over = True
        text = font.render('You lost😒', True, yellow)
        screen.blit(text, (15, 560))
        pg.display.flip()
        time.sleep(2)
        running = False
    if game_over and count < 10:
        text = font.render('You win!🙌',True, yellow)
        screen.blit(text, (15, 560))
        pg.display.flip()
        time.sleep(2)
        running = False

def main():
    global running, letters, count
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.TEXTINPUT and letters < 5 and not game_over:
                entry = event.text
                if entry != ' ':
                    game_board[count][letters] = entry
                    letters += 1
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_BACKSPACE and letters > 0:
                    game_board[count][letters - 1] = ' '
                    letters -=  1
                if letters == 5 and not game_over:
                    count += 1
                    letters = 0
                    break
        screen.fill(black)
        check_match()
        draw_board()
        draw_win()

        pg.display.flip()

main()
