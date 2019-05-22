# -*- Coding: utf-8 -*-

def mini_max(game):
    """
    ミニマックス法。
    2手先まで読んで、最善の手を選択。
    """

    def calc_score(game, board):
        """
        boardを受け取ったら、評価値を返す
        """

        evaluation = [ \
            [ 30, -12,   0,  -1,  -1,   0, -12,  30], \
            [-12, -15,  -3,  -3,  -3,  -3, -15, -12], \
            [  0,  -3,   0,  -1,  -1,   0,  -3,   0], \
            [ -1,  -3,  -1,  -1,  -1,  -1,  -3,  -1], \
            [ -1,  -3,  -1,  -1,  -1,  -1,  -3,  -1], \
            [  0,  -3,   0,  -1,  -1,   0,  -3,   0], \
            [-12, -15,  -3,  -3,  -3,  -3, -15, -12], \
            [ 30, -12,   0,  -1,  -1,   0, -12,  30] \
        ]

        score = 0

        for y in range(1, game.BOARD_WIDTH+1):
            for x in range(1, game.BOARD_HEIGHT+1):
                if board[y][x] is None:
                    continue
                elif board[y][x] == game.turn.to_color():
                    score += evaluation[y-1][x-1] # game.boardは外周が含まれているため。
                else:
                    score -= evaluation[y-1][x-1]

        return score

    # 1手先読みしてみる
    max_score = -9999
    max_pos = game.putlist[0]
    for pos in game.putlist:
        board = game.put_stone(pos, game.turn, test=True) # 1手先置きした盤面
        # print('if put ({}, {})'.format(pos[0], pos[1]))

        # 2手先読み
        next_poslist = game.make_putlist(game.opponent(game.turn), board)
        min_score = 9999
        if len(next_poslist) == 0:
            # 連続で打てる -> 最強
            return pos
            
        min_pos = next_poslist[0]
        for next_pos in next_poslist:
            next_board = game.put_stone(next_pos, game.opponent(game.turn), test=True, test_board=board)
            next_score = calc_score(game, next_board)
            # print('    next put ({}, {}) -> {} points'.format(next_pos[0], next_pos[1], next_score))

            if next_score < min_score:
                min_score = next_score
                min_pos = next_pos

        # print('        min score is {} points'.format(min_score))

        if min_score > max_score:
            max_score = min_score
            max_pos = pos


    # print("press ({}, {})".format(max_pos[0], max_pos[1]))
    return max_pos



def max_only(game):
    """
    マックス法。
    1手先まで読んで、最善の手を選択。
    """

    def calc_score(game, board):
        """
        boardを受け取ったら、評価値を返す
        """

        evaluation = [ \
            [ 30, -12,   0,  -1,  -1,   0, -12,  30], \
            [-12, -15,  -3,  -3,  -3,  -3, -15, -12], \
            [  0,  -3,   0,  -1,  -1,   0,  -3,   0], \
            [ -1,  -3,  -1,  -1,  -1,  -1,  -3,  -1], \
            [ -1,  -3,  -1,  -1,  -1,  -1,  -3,  -1], \
            [  0,  -3,   0,  -1,  -1,   0,  -3,   0], \
            [-12, -15,  -3,  -3,  -3,  -3, -15, -12], \
            [ 30, -12,   0,  -1,  -1,   0, -12,  30] \
        ]

        score = 0

        for y in range(1, game.BOARD_WIDTH+1):
            for x in range(1, game.BOARD_HEIGHT+1):
                if board[y][x] is None:
                    continue
                elif board[y][x] == game.turn.to_color():
                    score += evaluation[y-1][x-1] # game.boardは外周が含まれているため。
                else:
                    score -= evaluation[y-1][x-1]

        return score

    # 1手先読みしてみる
    max_score = -9999
    max_pos = game.putlist[0]
    for pos in game.putlist:
        board = game.put_stone(pos, game.turn, test=True) # 1手先置きした盤面
        score = calc_score(game, board)
        # print('if put ({}, {}) -> {} points'.format(pos[0], pos[1], score))
        if score > max_score:
            max_score = score
            max_pos = pos


    # print("press ({}, {})".format(max_pos[0], max_pos[1]))
    return max_pos