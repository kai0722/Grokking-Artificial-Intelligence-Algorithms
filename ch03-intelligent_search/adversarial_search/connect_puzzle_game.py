import connect_ai_alpha_beta_pruning as caiab
import connect_ai as cai
import connect_puzzle as cp

SEARCH_DEPTH = 10000000
connect = cp.Connect()
while connect.has_winner() == 0:
    connect.print_turn()
    connect.play_move(caiab.choose_move(connect, SEARCH_DEPTH))
    connect.print_board()
    print(connect.has_winner())

    if connect.has_winner() != 0: break

    connect.print_turn()
    human_move_result = False
    while human_move_result is False:
        print('Make your move: ')
        human_move = int(input())
        human_move_result = connect.play_move(human_move)
    connect.print_board()
    print(connect.has_winner())
