try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

# Initialize global variables
WIDTH = 300
HEIGHT = 300
LINE_WIDTH = 5
GRID_SIZE = 3
SQUARE_SIZE = WIDTH // GRID_SIZE
board = [[' ' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
turn = 'X'
winner = None

# Helper function to draw the board
def draw_board(canvas):
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            x = col * SQUARE_SIZE
            y = row * SQUARE_SIZE
            canvas.draw_line((x, 0), (x, HEIGHT), LINE_WIDTH, "White")
            canvas.draw_line((0, y), (WIDTH, y), LINE_WIDTH, "White")
            
            symbol = board[row][col]
            if symbol != ' ':
                center_x = x + SQUARE_SIZE // 2
                center_y = y + SQUARE_SIZE // 2
                pos = (center_x - 18, center_y + 18)
                canvas.draw_text(symbol, pos, 60, "White")

# Helper function to check for a winner
def check_winner():
    global winner
    # Check rows
    for row in range(GRID_SIZE):
        if board[row][0] == board[row][1] == board[row][2] != ' ':
            winner = board[row][0]
            return True
    # Check columns
    for col in range(GRID_SIZE):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            winner = board[0][col]
            return True
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        winner = board[0][0]
        return True
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        winner = board[0][2]
        return True
    return False

# Helper function to handle mouse click
def mouse_handler(pos):
    global turn, winner
    if winner is None:
        row = pos[1] // SQUARE_SIZE
        col = pos[0] // SQUARE_SIZE
        if board[row][col] == ' ':
            board[row][col] = turn
            if check_winner():
                print("Winner:", winner)
            else:
                turn = 'O' if turn == 'X' else 'X'

# Helper function to reset the game
def reset():
    global board, turn, winner
    board = [[' ' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    turn = 'X'
    winner = None

# Create frame and register event handlers
frame = simplegui.create_frame("Tic Tac Toe", WIDTH, HEIGHT)
frame.set_canvas_background("Black")
frame.set_draw_handler(draw_board)
frame.set_mouseclick_handler(mouse_handler)
frame.add_button("Reset", reset)

# Start the frame
frame.start()