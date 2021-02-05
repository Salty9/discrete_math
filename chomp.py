# A game of chomp
print("""Welcome to the game called CHOMP
Chomp is a game played by two players. In this game, cookies are laid out on a rectangular grid.
The cookie in the top left position is poisoned. The two players take turns making moves; at each move, a player is required to eat a remaining cookie, together with all cookies to the right and below it. The loser is the player who has no choice but to eat the poisoned cookie.
""")

height = int(input("How high do you want your board to be ? "))
width = int(input("How wide do you want your board to be ? "))

board = [[0]*width for _ in range(height) ]
first_player_move = True

def print_board():
    for i in range(height):
        print(board[i][:])

print_board()
print("Make your moves in the form (row, column) of the cookie that you want to take. E.x. (2, 3) would take the cookie in the 2nd row and 3rd column and all the cookies to the right and below it")

def update_board(x1):
    for row in range(x1[0]-1, height):
        for column in range(x1[1]-1, width):
            board[row][column] = 1

def is_game_over():

    return board[0][1] == 1 and board[1][0] == 1    # forces opponent to take take the poison cookie 

def winner():
    if board[0][0] == 1:                                # suicidal move. rarely will occur
        if not first_player_move:                       
            print("The second player is the winner!")
        else:
            print("The first player is the winner!")
        return None 


    if not first_player_move:                       # if it's the second player's move, he'll be forced to take the poisoned cookie
        print("The first player has won the game!")
    else:
        print("The second player has won the game!")
    
    

while not is_game_over():

    move = eval(input(f"{['Second', 'First'][first_player_move]} player's turn: "))
    
    first_player_move = not first_player_move          # one player has played. so *move* (pun intended) to the other player
    update_board(move)
    print_board()


winner()                # print the winner of the game (ties aren't possible)

print("The existence of a winning strategy for the first player can be mathematically proven but it is an open problem to describe the moves the first player should follow for an arbitary grid. See if you can find such strategies.")