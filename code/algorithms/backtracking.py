def backtrace(state_list): 
    
    moves = {}

    for state in state_list: 

        # get the current and next state 
        current_state = state_list[state]
        next_state = state_list[state + 1]

        # compare the two states to get the moved car 
        original_position = list(set(current_state) - set(next_state))
        next_position = list(set(next_state) - set(current_state))

        # check in what way the car moves
        if original_position.x < next_position.x: 
            if original_position not in moves: 
                moves[{original_position}] = 1
            else: 
                moves[{original_position}] += 1

        if original_position.x > next_position.x: 
            if original_position not in moves: 
                moves[{original_position}] = 1
            else: 
                moves[{original_position}] -= 1


        if original_position.x > next_position.x: 
            if original_position not in moves: 
                moves[{original_position}] = 1
            else:
                moves[{original_position}] -= 1
        
        if original_position.y < next_position.y: 
            if original_position not in moves: 
                moves[{original_position}] = 1
            else: 
                moves[{original_position}] += 1

    return moves