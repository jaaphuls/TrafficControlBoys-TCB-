import random
import time
import queue
from code.classes.vehicle import Vehicle
from code.classes.board import Board

# breadth first algorithm
def breadth_first(board, board_size):
    start_time = time.time()
    previous_states = board.states_list
    previous_states.add(board.string_value)
    
    history = []

    states_visited = 0

    choices_queue = queue.Queue()
    choices_queue.put(board)

    
    if board_size == 6: 
        end_coord = 2,5

    if board_size == 9: 
        end_coord = 4,8
    
    if board_size == 12: 
        end_coord = 5, 11


    while True:
        current_state = choices_queue.get()
        for states in current_state.check_move():
            
            new_game = Board(states, board_size)

            if new_game.string_value not in board.states_list:
                history.append(board.car_list)

                states_visited += 1
                print(states_visited)
                # print(new_game.string_value)
                # print(board.states_list)
                board.states_list.add(new_game.string_value)
               
                new_game.create_board()
                new_game.visualize()

                choices_queue.put(new_game)

                if new_game.rush_board[end_coord] == "X":
                    runtime = time.time() - start_time

                    return runtime, history
            else:
                pass
        
