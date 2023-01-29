import json

def main():
    file1 = open('10kgames.txt', 'r')
    file2 = open('10kgames.json', 'w')
    for line in file1:
        print("here")
        # file2.write(json.dumps(line))
        file2.write(line)
    file1.close()
    file2.close()

if __name__ == "__main__":
    main()

# #from cairosvg import svg2png
# #import cairosvg
# import pygame as pg
# #import cairo
# import time

# def main():
#     # cairosvg.svg2png(url='temp.svg', write_to='temp.png')
#     # svg = None
#     # with open('temp.svg', 'r') as sf:
#     #     svg = sf.read().format(w=100, h=100,
#     #                            r=0, sx=1, sy=1, tx=0, ty=0)
#     # cairosvg.svg2png(bytestring=svg, write_to='temp.png')

#     board = '1Q6/4r1k1/1p1Nbpp1/3n3p/7P/5P2/6PK/8'
#     board = board.split('/')

#     images = {}

#     P = pg.image.load('w_p.png')
#     p = pg.image.load('b_p.png')

#     images['P'] = P
#     images['p'] = p

#     K = pg.image.load('w_k.png')
#     k = pg.image.load('b_k.png')

#     images['K'] = K
#     images['k'] = k

#     Q = pg.image.load('w_q.png')
#     q = pg.image.load('b_q.png')

#     images['Q'] = Q
#     images['q'] = q

#     R = pg.image.load('w_r.png')
#     r = pg.image.load('b_r.png')

#     images['R'] = R
#     images['r'] = r

#     B = pg.image.load('w_b.png')
#     b = pg.image.load('b_b.png')

#     images['B'] = B
#     images['b'] = b

#     N = pg.image.load('w_n.png')
#     n = pg.image.load('b_n.png')

#     images['N'] = N
#     images['n'] = n

#     pg.init()
#     clock = pg.time.Clock()
#     screen = pg.display.set_mode([60*8,60*8])
#     screen.fill([255,255,255])
#     #screen.fill([240,217,181])
#     chunk = 60
#     for i in range(64):
#         x = i % 8
#         y = i // 8
#         if y % 2 == 0:
#             if i % 2 == 0:
#                 pg.draw.rect(screen, [240,217,181], (x * chunk, y * chunk, chunk, chunk))
#             else:
#                 pg.draw.rect(screen, [181,136,99], (x * chunk, y * chunk, chunk, chunk))
#         else:
#             if i % 2 == 0:
#                 pg.draw.rect(screen, [181,136,99], (x * chunk, y * chunk, chunk, chunk))
#             else:
#                 pg.draw.rect(screen, [240,217,181], (x * chunk, y * chunk, chunk, chunk))
#         #pg.draw.rect(screen, [181,136,99], (x * chunk, y * chunk, chunk, chunk))

#     x = 0
#     y = 0
#     for line in board:
#         x = 0
#         for character in line:
#             if character.isnumeric():
#                 x += int(character)
#             else:
#                 screen.blit(images[character],(x*chunk,y*chunk))
#                 x += 1
#         y += 1

    
#     pg.display.update()
#     time.sleep(3)
    
    

# if __name__ == "__main__":
#     main()