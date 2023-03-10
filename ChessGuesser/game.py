import random
import time
import os
import json
import chess
import chess.svg
import pygame
import sys
#import cairosvg
#import cairo
#from wand.api import library 
#import wand.image
# from svglib.svglib import svg2rlg
# from reportlab.graphics import renderPM
# import fitz
# from svglib import svglib
# from reportlab.graphics import renderPDF

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FULLSCREEN = False

def lose(screen, score, eval):
    font4 = pygame.font.Font(None, 80)
    font5 = pygame.font.Font(None, 50)
    font6 = pygame.font.Font(None, 40)
    
    lose1 = font4.render("YOU", True, [0,0,0])
    lose2 = font4.render("LOSE", True, [0,0,0])
    actual_eval = font6.render("The actual evaluation was " + str(eval/100),True,[50,50,50])
    score_text = font5.render("Final Score: " + str(score), True, [0,0,0])
    lose_rect1 = lose1.get_rect(center=(1280/2, 720 - 260))
    lose_rect2 = lose2.get_rect(center=(1280/2, 720 - 200))
    actual_eval_rect = actual_eval.get_rect(center=(1280/2, 720-100))
    score_rect = score_text.get_rect(center=(1280/2, 720 - 40))
    
    pygame.draw.rect(screen,[255,255,255], (60*8+50,60*8+20,220 + 60*8,220))
    
    screen.blit(lose1, lose_rect1)
    screen.blit(lose2, lose_rect2)
    screen.blit(actual_eval, actual_eval_rect)
    screen.blit(score_text, score_rect)

    pygame.draw.rect(screen,[200,200,200], (1280-50-60*8+180,480+30,480-180,200))
    again = font5.render("Play Again!", True, [0,0,0])
    again_rect = again.get_rect(center=(1280-50-60*8+180+(480-180)/2,480+30+100))
    screen.blit(again, again_rect)

    pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                (x,y) = pygame.mouse.get_pos()
                if x > 930 and x < 930 + 300 and y > 480+30 and y < 480+30 + 200:
                    return
    
    return

def screenDisplay(screen, clock, prev_board, next_board, score):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            sys.exit()
    #print(prev_board)
    #print(next_board)
    
    font = pygame.font.Font(None, 25)
    font2 = pygame.font.Font(None, 50)
    
    text = str(prev_board['eval']['value']/100)
    
    text1 = font.render("Board's eval is greater than " + text,True, [120,120,120])
    text2 = font.render("Board's eval is less than " + text,True, [120,120,120])
    text1_rect = text1.get_rect(center=(1280-50-60*8+240,480+30+50))
    text2_rect = text2.get_rect(center=(1280-50-60*8+240,480+130+50))
    
    text3 = font.render("User: " + str(prev_board['black']) + " Elo: " + str(prev_board['bElo']),True, [120,120,120])
    text4 = font.render("User: " + str(prev_board['white']) + " Elo: " + str(prev_board['wElo']),True, [120,120,120])
    text5 = font2.render(prev_board['url'],True, [120,120,120])
    text7 = font2.render("Evaluation: " + text,True, [0,0,0])
    text3_rect = text3.get_rect(center=(50+240,10))
    text4_rect = text4.get_rect(center=(50+240,30+480))
    text5_rect = text5.get_rect(center=(20+240,720-20))
    text7_rect = text7.get_rect(center=(50+240,60+480))

    text6 = font.render("White to Play",True, [0,0,0])
    text6_rect = text6.get_rect(center=(1280/2,10))
    
    screen.fill([255,255,255])
    drawBoard(screen, prev_board["position"], (50,20))
    drawBoard(screen, next_board["position"], (1280-50-60*8,20))
    screen.blit(text3, text3_rect)
    screen.blit(text4, text4_rect)
    screen.blit(text5, text5_rect)
    screen.blit(text6, text6_rect)
    screen.blit(text7, text7_rect)
    
    pygame.draw.rect(screen,[240,240,240], (1280-50-60*8,480+30,480,100))
    pygame.draw.rect(screen,[0,0,0], (1280-50-60*8,480+130,480,100))
    
    font2 = pygame.font.Font(None, 50)
    font3 = pygame.font.Font(None, 100)
    
    score_label = font2.render("SCORE:", True, [0,0,0])
    score_text = font3.render(str(score), True, [0,0,0])
    score_rect1 = score_label.get_rect(center=(1280/2, 720 - 180))
    score_rect2 = score_text.get_rect(center=(1280/2, 720 - 100))
    
    screen.blit(text1, text1_rect)
    screen.blit(text2, text2_rect)
    screen.blit(score_label, score_rect1)
    screen.blit(score_text, score_rect2)
    
    pygame.display.update()
    
    success = True
    
    prev_eval = prev_board['eval']['value']
    next_eval = next_board['eval']['value']
    
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                (x,y) = pygame.mouse.get_pos()
                if x > 1280-50-60*8 and x < 1280-50-60*8 + 480 and y > 480+30 and y < 480+30 + 100:
                    if prev_eval > next_eval:
                        lose(screen, score, next_eval)
                        return False
                    return True
                if x > 1280-50-60*8 and x < 1280-50-60*8 + 480 and y > 480+30 + 100 and y < 480+30 + 200:
                    if prev_eval > next_eval:
                        return True
                    lose(screen, score, next_eval)
                    return False


def drawBoard(screen, board, location):
    #board = '1Q6/4r1k1/1p1Nbpp1/3n3p/7P/5P2/6PK/8'
    board = board.split(' ')
    board = board[0].split('/')

    images = {}

    P = pygame.image.load('images/w_p.png')
    p = pygame.image.load('images/b_p.png')

    images['P'] = P
    images['p'] = p

    K = pygame.image.load('images/w_k.png')
    k = pygame.image.load('images/b_k.png')

    images['K'] = K
    images['k'] = k

    Q = pygame.image.load('images/w_q.png')
    q = pygame.image.load('images/b_q.png')

    images['Q'] = Q
    images['q'] = q

    R = pygame.image.load('images/w_r.png')
    r = pygame.image.load('images/b_r.png')

    images['R'] = R
    images['r'] = r

    B = pygame.image.load('images/w_b.png')
    b = pygame.image.load('images/b_b.png')

    images['B'] = B
    images['b'] = b

    N = pygame.image.load('images/w_n.png')
    n = pygame.image.load('images/b_n.png')

    images['N'] = N
    images['n'] = n

    #pygame.init()
    #clock = pygame.time.Clock()
    #screen = pygame.display.set_mode([60*8,60*8])
    #screen.fill([255,255,255])
    #screen.fill([240,217,181])
    chunk = 60
    for i in range(64):
        x = i % 8
        y = i // 8
        pos = (x * chunk + location[0], y * chunk + location[1], chunk, chunk)
        if y % 2 == 0:
            if i % 2 == 0:
                pygame.draw.rect(screen, [240,217,181], pos)
            else:
                pygame.draw.rect(screen, [181,136,99], pos)
        else:
            if i % 2 == 0:
                pygame.draw.rect(screen, [181,136,99], pos)
            else:
                pygame.draw.rect(screen, [240,217,181], pos)
        #pg.draw.rect(screen, [181,136,99], (x * chunk, y * chunk, chunk, chunk))

    x = 0
    y = 0
    for line in board:
        x = 0
        for character in line:
            if character.isnumeric():
                x += int(character)
            else:
                screen.blit(images[character],(x*chunk + location[0],y*chunk + location[1]))
                x += 1
        y += 1


def pickBoard(games, prev_game, difficulty):
    prev_eval = prev_game["eval"]["value"]
    valid = False
    
    while not valid:
        
        game = random.choice(list(games))
        eval_type = game["eval"]['type']
        eval = game["eval"]["value"]
        if eval_type != "cp":
            continue
        if difficulty == "easy":
            if abs(eval - prev_eval) >= 100:
                valid = True        
        else:
            valid = True
            
    return game

def start(screen):
    screen.fill([255,255,255])

    font1 = pygame.font.Font(None, 100)
    font2 = pygame.font.Font(None, 40)
    font3 = pygame.font.Font(None, 60)
    font4 = pygame.font.Font(None, 30)

    text1 = font1.render("Higher or Lower",True, [0,0,0])
    text2 = font1.render("Chess Position Evaluation",True, [0,0,0])
    text1_rect = text1.get_rect(center=(1280/2,50))
    text2_rect = text2.get_rect(center=(1280/2,120))
    screen.blit(text1,text1_rect)
    screen.blit(text2,text2_rect)

    text3 = font2.render("The position on the left will have a displayed evaluation.",True, [70,70,70])
    text4 = font2.render("The goal is to analyze the position on the right and determine",True, [70,70,70])
    text5 = font2.render("if it's evaluation is higher or lower than the evaluation on the left.",True, [70,70,70])
    text6 = font4.render("Game made by Justin Masters and Nate Bollman",True, [70,70,70])
    text7 = font4.render("Made for Michigan State University's SpartaHack 8",True, [70,70,70])
    text3_rect = text3.get_rect(center=(1280/2,170))
    text4_rect = text4.get_rect(center=(1280/2,200))
    text5_rect = text5.get_rect(center=(1280/2,230))
    text6_rect = text6.get_rect(center=(1280/2,520))
    text7_rect = text7.get_rect(center=(1280/2,550))
    screen.blit(text3,text3_rect)
    screen.blit(text4,text4_rect)
    screen.blit(text5,text5_rect)
    screen.blit(text6,text6_rect)
    screen.blit(text7,text7_rect)

    pygame.draw.rect(screen,[100,100,100], (1280/2-300,280,600,200))
    again = font3.render("Play", True, [255,255,255])
    again_rect = again.get_rect(center=(1280/2,380))
    screen.blit(again, again_rect)

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                (x,y) = pygame.mouse.get_pos()
                if x > 1280/2-300 and x < 1280/2-300 + 600 and y > 280 and y < 280 + 200:
                    return

def main():
    
    f = open("10kgames.json")
    data = json.load(f)
    games = data['games']
    
    # Set up game
    pygame.init()
    
    if FULLSCREEN:
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    start(screen)

    running = True
    
    while running:
        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
              
        prev_bool = True  # True for prev board, False for next board
            
        prev_board = random.choice(list(games))
        prev_board_FEN = prev_board['position']
        #prev_board_img = getBoardImage(prev_board_FEN, prev_bool)
        
        fail = False
        prev_bool = False
        
        difficulty = "easy"
        score = 0
        while not fail:
            next_board = pickBoard(games, prev_board, difficulty)
            #next_board_FEN = next_board['position']
            
            #next_board_img = getBoardImage(next_board_FEN, prev_bool)
            
            fail = not screenDisplay(screen, clock, prev_board, next_board, score)
            
            #prev_board_img = next_board_img
            score += 1
            prev_board = next_board
        
    pygame.display.quit()
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
    