from stockfish import Stockfish
import json
import re
import random
from pgn2fen import PgnToFen


def checkGame(game): 
    moves = game.count('.')
    if moves < 25:
        return ""
    pos_num = random.randint(20, moves - 5)
    pos = game.find(str(pos_num))
    spliced_game = game[:pos]

    return spliced_game

def main():
    # stockfish = Stockfish(path=r"C:\Users\justi\OneDrive\Desktop\stockfish_15.1_win_x64_avx2\stockfish_15.1_win_x64_avx2\stockfish-windows-2022-x86-64-avx2.exe", depth=28, parameters={"Threads": 8, "Minimum Thinking Time": 100000})
    # stockfish.set_position(["e2e4", "e7e5", "d1f3", "b8a6", "f1c4", "a6b4"])
    # print(stockfish.get_evaluation())
    game_dict = {}
    game_dict['games'] = []
    
    file1 = open('lichess_elite_2020-08_1MIL.txt', 'r')
    count = 0
    game_bool = False
    game_str = ""
    # games = []
    current_game = {}
    for line in file1:
        if "[LichessURL" in line:
            current_game['url'] = re.findall(r'"([^"]*)"', line)[0]
        if "[White " in line:
            current_game['white'] = re.findall(r'"([^"]*)"', line)[0]
        if "[Black " in line:
            current_game['black'] = re.findall(r'"([^"]*)"', line)[0]
        if game_bool:
            game_str += line.removesuffix('\n')
        if line == "\n":
            if game_bool == True:
                
                game = checkGame(game_str)
                if not game:
                    current_game = {}
                    game_str = ""
                    game_bool = False
                    continue
                
                
                
                current_game['position'] = game_str
                game_dict['games'].append(current_game)
                
                current_game = {}
                # game_dict[count] = game_str
                game_bool = False
                # games.append(game_str)
                game_str = ""
                count += 1
            else:
                game_bool = True
        #print("Line{}: {}".format(count, line.strip()))
        if count > 1000:
            break
    #print(game_dict)
    # for game in games:
    #     print("Game: ", game)
    json_ = json.dumps(game_dict)
    #print(json_)
    # for game in game_dict:
    #     if " 2. Ke2" in game_dict[game]:
    #         print(game_dict[game])
    file2 = open('10kgames.txt', 'w')
    file2.write(json_)


if __name__ == "__main__":
    main()