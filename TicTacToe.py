board = {
    'T1': ' ', 'T2': ' ', 'T3': ' ',
    'M1': ' ', 'M2': ' ', 'M3': ' ',
    'D1': ' ', 'D2': ' ', 'D3': ' '
}

player = 1        
total_moves = 0     
end_check = 0


def check_win():

    #horizontal
    if board['T1'] == 'X' and board['T2'] == 'X' and board['T3'] == 'X':
        print('Player one won !')
        return 1
    if board['M1'] == 'X' and board['M2'] == 'X' and board['M3'] == 'X':
        print('Player One Won!!')
        return 1
    if board['D1'] == 'X' and board['D2'] == 'X' and board['D3'] == 'X':
        print('Player One Won!!')
        return 1
    
    # diagonal
    if board['T1'] == 'X' and board['M2'] == 'X' and board['D3'] == 'X':
        print('Player One Won!!')
        return 1
    
    # vertical
    if board['T1'] == 'X' and board['M1'] == 'X' and board['D1'] == 'X':
        print('Player One Won!!')
        return 1
    if board['T2'] == 'X' and board['M2'] == 'X' and board['D2'] == 'X':
        print('Player One Won!!')
        return 1
    if board['T3'] == 'X' and board['M3'] == 'X' and board['D3'] == 'X':
        print('Player One Won!!')
        return 1
    

    #player 2
    #horizontal
    if board['T1'] == 'O' and board['T2'] == 'O' and board['T3'] == 'O':
        print('Player Two Won!!')
        return 1  
    if board['M1'] == 'O' and board['M2'] == 'O' and board['M3'] == 'O':
        print('Player Two Won!!')
        return 1
    if board['D1'] == 'O' and board['D2'] == 'O' and board['D3'] == 'O':
        print('Player Two Won!!')
        return 1
    
    #Diagonal
    if board['T1'] == 'O' and board['M2'] == 'O' and board['D3'] == 'O':
        print('Player Two Won!!')
        return 1

    #vertical
    if board['T1'] == 'O' and board['M1'] == 'O' and board['D1'] == 'O':
        print('Player Two Won!!')
        return 1
    if board['T2'] == 'O' and board['M2'] == 'O' and board['D2'] == 'O':
        print('Player Two Won!!')
        return 1
    if board['T3'] == 'O' and board['M3'] == 'O' and board['D3'] == 'O':
        print('Player Two Won!!')
        return 1
    return 0


print('T1|T2|T3')
print('- +- +-')
print('M1|M2|M3')
print('- +- +-')
print('D1|D2|D3')

while True:
    print(board['T1']+'|'+board['T2']+'|'+board['T3'])
    print('-+-+-')
    print(board['M1'] + '|' + board['M2'] + '|' + board['M3'])
    print('-+-+-')
    print(board['D1'] + '|' + board['D2'] + '|' + board['D3'])

    end_check = check_win()

    if total_moves == 9 or end_check == 1:
        break

    while True:     
        if player == 1: 
            p1_input = input('Select position as T1, M1, D1 player one \n')
            if p1_input.upper() in board and board[p1_input.upper()] == ' ':
                board[p1_input.upper()] = 'X'
                player = 2
                break
            
            else:
                print('Invalid input, please try again')
                continue
        else:
            p2_input = input('Select position as T1, M1, D1 player two \n')
            if p2_input.upper() in board and board[p2_input.upper()] == ' ':
                board[p2_input.upper()] = 'O'
                player = 1
                break
            else:  
                print('Invalid input, please try again')
                continue
            
    total_moves += 1
    print('***************************')
    print()
