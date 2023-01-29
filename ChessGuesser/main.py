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
    stockfish = Stockfish(path=r"C:\Users\justi\OneDrive\Desktop\stockfish_15.1_win_x64_avx2\stockfish_15.1_win_x64_avx2\stockfish-windows-2022-x86-64-avx2.exe", depth=24, parameters={"Threads": 12, "Minimum Thinking Time": 1000})
    # stockfish.set_position(["e2e4", "e7e5", "d1f3", "b8a6", "f1c4", "a6b4"])
    # print(stockfish.get_evaluation())
    game_dict = {}
    game_dict['games'] = []

    pgnConverter = PgnToFen()
    
    file1 = open('lichess_elite_2020-08_1MIL.txt', 'r')
    count = 0
    line_count = 0
    total_game_count = 0
    pgn_fail_count = 0
    checkgame_fail_count = 0
    game_bool = False
    game_str = ""
    # games = []
    current_game = {}
    for line in file1:
        line_count += 1
        if "[LichessURL" in line:
            current_game['url'] = re.findall(r'"([^"]*)"', line)[0]
        if "[White " in line:
            current_game['white'] = re.findall(r'"([^"]*)"', line)[0]
        if "[Black " in line:
            current_game['black'] = re.findall(r'"([^"]*)"', line)[0]
        if "[WhiteElo " in line:
            current_game['wElo'] = re.findall(r'"([^"]*)"', line)[0]
        if "[BlackElo " in line:
            current_game['bElo'] = re.findall(r'"([^"]*)"', line)[0]
        if game_bool:
            game_str += line.removesuffix('\n')
            game_str += " "
        if line == "\n":
            if game_bool == True:
                total_game_count += 1
                
                game = checkGame(game_str)
                if not game:
                    checkgame_fail_count += 1
                    current_game = {}
                    game_str = ""
                    game_bool = False
                    continue
                
                #PGNMoves = '1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 g6 6. Be3 Bg7 7. Bc4 O-O 8. f3 Nc6 9. Qd2 a6 10. Bb3 Nxd4 11. Bxd4 b5 12. a4 b4 13. Nd5 Nxd5 14. Bxd5 Rb8 15. a5 e6 16. Bb3 d5 17. Bxg7 Kxg7 18. exd5 exd5 19. Qd4+ Kg8 20. O-O Be6 21. Rfd1 Qc7 22. Kh1 Rb5 23. Ra4 Qe7 24. Re1 Qd6 25. Re5 Rc8 26. h3 Rcc5 27. f4 Rxa5 28. Qxb4 Rab5 29. Qd4 a5 30. Ra3 Rb4 31. Qd2 Qd8 32. Qf2 Rc8 33. f5 Qf6'
                #print(game)
                try:
                    pgnConverter.pgnToFen(game.split(' '))
                except:
                    pgn_fail_count += 1
                    current_game = {}
                    game_str = ""
                    game_bool = False
                    pgnConverter.resetBoard()
                    continue
                game = pgnConverter.getFullFen()
                pgnConverter.resetBoard()
                
                current_game['position'] = game

                stockfish.set_fen_position(game)
                current_game['eval'] = stockfish.get_evaluation()
                
                game_dict['games'].append(current_game)

                
                # game_dict[count] = game_str
                game_bool = False
                # games.append(game_str)
                game_str = ""
                count += 1
                print("Game ",count," ",current_game['eval'])
                current_game = {}
                if count != len(game_dict['games']):
                    print("here")
            else:
                game_bool = True
        #print("Line{}: {}".format(count, line.strip()))
        if count >= 500:
            break
    file1.close()
    print("game_dict['games'] len:",len(game_dict['games']))
    print("total game count from file:", total_game_count)
    print("total lines: ", line_count)
    print("pgn conversion failure count: ", pgn_fail_count)
    print("game didn't pass check game count: ",checkgame_fail_count)
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