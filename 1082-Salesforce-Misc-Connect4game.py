print('Player 1 turn')
player_turn = 1
n = int(input())
while n != -1:
    #  7 x 6
    board = [[0 for j in range(6)]
             for i in range(7)]

    # validate n inside board

    # place n for current player, n can "fall" to the botton

    # check for winner / draw

    if player_turn is 1:
        player_turn = 2
    else:
        player_turn = 1
    print(f'Player {player_turn} turn')
    n = int(input())
    pass
