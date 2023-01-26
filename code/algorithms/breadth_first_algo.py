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

    step = 0

    choices_queue = queue.Queue()
    choices_queue.put(board)

    
    if board_size == 6: 
        end_coord = 2,5

    if board_size == 9: 
        end_coord = 4,8
    
    if board_size == 12: 
        end_coord = 5, 11

    unsolved = True

    while unsolved:
        current_state = choices_queue.get()
        
        for states in current_state.check_move():
            
            new_game = Board(states, board_size)

            if new_game.string_value not in board.states_list:
                history.append(board.car_list)

                step += 1
                print(step)
                # print(new_game.string_value)
                # print(board.states_list)
                board.states_list.add(new_game.string_value)
               
                new_game.create_board()
                new_game.visualize()

                choices_queue.put(new_game)

                unsolved = new_game.rush_board[end_coord] != "X"

    runtime = time.time() - start_time
    # print(step)
    return runtime, history
