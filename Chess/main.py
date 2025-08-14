import tkinter as tk
from tkinter import messagebox

def start_pvp():
    # Code from chesspvp.py
    print("Starting Player vs Player Chess...")

    def run_pvp_game():
        # Importing Modules
        import pygame
        # Initialising pygame module
        pygame.init()
        # Setting width and height of the Chess Game screen
        WIDTH = 800
        HEIGHT = 800
        screen = pygame.display.set_mode([WIDTH, HEIGHT])
        pygame.display.set_caption('Two-Player Chess Game')
        font = pygame.font.Font('freesansbold.ttf', 20)
        medium_font = pygame.font.Font('freesansbold.ttf', 40)
        big_font = pygame.font.Font('freesansbold.ttf', 50)
        timer = pygame.time.Clock()
        fps = 60
        # game variables and images
        white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',

                        'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']

        white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),

                        (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]

        black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',

                        'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']

        black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),

                        (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]

        captured_pieces_white = []
        captured_pieces_black = []

        # 0 - whites turn no selection: 1-whites turn piece selected: 2- black turn no selection, 3 - black turn piece selected
        turn_step = 0
        selection = 100
        valid_moves = []
        # load in game piece images (queen, king, rook, bishop, knight, pawn) x 2
        black_queen = pygame.image.load("D:/Game Project/Image/Black Queen.png")
        black_queen = pygame.transform.scale(black_queen, (80, 80))
        black_queen_small = pygame.transform.scale(black_queen, (45, 45))
        black_king = pygame.image.load("D:/Game Project/Image/Black King.png")
        black_king = pygame.transform.scale(black_king, (80, 80))
        black_king_small = pygame.transform.scale(black_king, (45, 45))
        black_rook = pygame.image.load("D:/Game Project/Image/Black Rook.png")
        black_rook = pygame.transform.scale(black_rook, (80, 80))
        black_rook_small = pygame.transform.scale(black_rook, (45, 45))
        black_bishop = pygame.image.load("D:/Game Project/Image/Black Bishop.png")
        black_bishop = pygame.transform.scale(black_bishop, (80, 80))
        black_bishop_small = pygame.transform.scale(black_bishop, (45, 45))
        black_knight = pygame.image.load("D:/Game Project/Image/Black Knight.png")
        black_knight = pygame.transform.scale(black_knight, (80, 80))
        black_knight_small = pygame.transform.scale(black_knight, (45, 45))
        black_pawn = pygame.image.load("D:/Game Project/Image/Black Pawn.png")
        black_pawn = pygame.transform.scale(black_pawn, (65, 65))
        black_pawn_small = pygame.transform.scale(black_pawn, (45, 45))
        white_queen = pygame.image.load("D:/Game Project/Image/White Queen.png")
        white_queen = pygame.transform.scale(white_queen, (80, 80))
        white_queen_small = pygame.transform.scale(white_queen, (45, 45))
        white_king = pygame.image.load("D:/Game Project/Image/White King.png")
        white_king = pygame.transform.scale(white_king, (80, 80))
        white_king_small = pygame.transform.scale(white_king, (45, 45))
        white_rook = pygame.image.load("D:/Game Project/Image/White Rook.png")
        white_rook = pygame.transform.scale(white_rook, (80, 80))
        white_rook_small = pygame.transform.scale(white_rook, (45, 45))
        white_bishop = pygame.image.load("D:/Game Project/Image/White Bishop.png")
        white_bishop = pygame.transform.scale(white_bishop, (80, 80))
        white_bishop_small = pygame.transform.scale(white_bishop, (45, 45))
        white_knight = pygame.image.load("D:/Game Project/Image/White Knight.png")
        white_knight = pygame.transform.scale(white_knight, (80, 80))
        white_knight_small = pygame.transform.scale(white_knight, (45, 45))
        white_pawn = pygame.image.load("D:/Game Project/Image/White Pawn.png")
        white_pawn = pygame.transform.scale(white_pawn, (65, 65))
        white_pawn_small = pygame.transform.scale(white_pawn, (45, 45))

        white_images = [white_pawn, white_queen, white_king,

                        white_knight, white_rook, white_bishop]

        small_white_images = [white_pawn_small, white_queen_small, white_king_small, white_knight_small,

                            white_rook_small, white_bishop_small]

        black_images = [black_pawn, black_queen, black_king,

                        black_knight, black_rook, black_bishop]

        small_black_images = [black_pawn_small, black_queen_small, black_king_small, black_knight_small, black_rook_small, black_bishop_small]

        piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']

        # check variables/ flashing counter
        counter = 0
        winner = ''
        game_over = False

        # draw main game board
        def draw_board():

            for i in range(32):

                column = i % 4

                row = i // 4

                if row % 2 == 0:

                    pygame.draw.rect(screen, 'light gray', [

                                    600 - (column * 200), row * 100, 100, 100])

                else:

                    pygame.draw.rect(screen, 'light gray', [

                                    700 - (column * 200), row * 100, 100, 100])

                pygame.draw.rect(screen, 'gray', [0, 800, WIDTH, 100])

                pygame.draw.rect(screen, 'gold', [0, 800, WIDTH, 100], 5)

                pygame.draw.rect(screen, 'gold', [800, 0, 200, HEIGHT], 5)

                status_text = ['White: Select a Piece to Move!', 'White: Select a Destination!',

                            'Black: Select a Piece to Move!', 'Black: Select a Destination!']

                screen.blit(big_font.render(

                    status_text[turn_step], True, 'black'), (20, 820))

                for i in range(9):

                    pygame.draw.line(screen, 'black', (0, 100 * i), (800, 100 * i), 2)

                    pygame.draw.line(screen, 'black', (100 * i, 0), (100 * i, 800), 2)

                screen.blit(medium_font.render('FORFEIT', True, 'black'), (810, 830))

        
        # draw pieces onto board
        def draw_pieces():

            for i in range(len(white_pieces)):

                index = piece_list.index(white_pieces[i])

                if white_pieces[i] == 'pawn':

                    screen.blit(

                        white_pawn, (white_locations[i][0] * 100 + 22, white_locations[i][1] * 100 + 30))

                else:

                    screen.blit(white_images[index], (white_locations[i]

                                [0] * 100 + 10, white_locations[i][1] * 100 + 10))

                if turn_step < 2:

                    if selection == i:

                        pygame.draw.rect(screen, 'red', [white_locations[i][0] * 100 + 1, white_locations[i][1] * 100 + 1,

                                                        100, 100], 2)

        

            for i in range(len(black_pieces)):

                index = piece_list.index(black_pieces[i])

                if black_pieces[i] == 'pawn':

                    screen.blit(

                        black_pawn, (black_locations[i][0] * 100 + 22, black_locations[i][1] * 100 + 30))

                else:

                    screen.blit(black_images[index], (black_locations[i]

                                [0] * 100 + 10, black_locations[i][1] * 100 + 10))

                if turn_step >= 2:

                    if selection == i:

                        pygame.draw.rect(screen, 'blue', [black_locations[i][0] * 100 + 1, black_locations[i][1] * 100 + 1,

                                                        100, 100], 2)

        
        # function to check all pieces valid options on board
        def check_options(pieces, locations, turn):
            moves_list = []

            all_moves_list = []

            for i in range((len(pieces))):

                location = locations[i]

                piece = pieces[i]

                if piece == 'pawn':

                    moves_list = check_pawn(location, turn)

                elif piece == 'rook':

                    moves_list = check_rook(location, turn)

                elif piece == 'knight':

                    moves_list = check_knight(location, turn)

                elif piece == 'bishop':

                    moves_list = check_bishop(location, turn)

                elif piece == 'queen':

                    moves_list = check_queen(location, turn)

                elif piece == 'king':

                    moves_list = check_king(location, turn)

                all_moves_list.append(moves_list)

            return all_moves_list

        # check king valid moves
        def check_king(position, color):

            moves_list = []

            if color == 'white':

                enemies_list = black_locations

                friends_list = white_locations

            else:

                friends_list = black_locations

                enemies_list = white_locations

            # 8 squares to check for kings, they can go one square any direction

            targets = [(1, 0), (1, 1), (1, -1), (-1, 0),

                    (-1, 1), (-1, -1), (0, 1), (0, -1)]

            for i in range(8):

                target = (position[0] + targets[i][0], position[1] + targets[i][1])

                if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:

                    moves_list.append(target)

            return moves_list

        # check queen valid moves
        def check_queen(position, color):

            moves_list = check_bishop(position, color)

            second_list = check_rook(position, color)

            for i in range(len(second_list)):

                moves_list.append(second_list[i])

            return moves_list

        # check bishop moves
        def check_bishop(position, color):

            moves_list = []

            if color == 'white':

                enemies_list = black_locations

                friends_list = white_locations

            else:

                friends_list = black_locations

                enemies_list = white_locations

            for i in range(4):  # up-right, up-left, down-right, down-left

                path = True

                chain = 1

                if i == 0:

                    x = 1

                    y = -1

                elif i == 1:

                    x = -1

                    y = -1

                elif i == 2:

                    x = 1

                    y = 1

                else:

                    x = -1

                    y = 1

                while path:

                    if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and 0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:

                        moves_list.append(

                            (position[0] + (chain * x), position[1] + (chain * y)))

                        if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:

                            path = False

                        chain += 1

                    else:

                        path = False

            return moves_list

        # check rook moves
        def check_rook(position, color):

            moves_list = []

            if color == 'white':

                enemies_list = black_locations

                friends_list = white_locations

            else:

                friends_list = black_locations

                enemies_list = white_locations

            for i in range(4):  # down, up, right, left

                path = True

                chain = 1

                if i == 0:

                    x = 0

                    y = 1

                elif i == 1:

                    x = 0

                    y = -1

                elif i == 2:

                    x = 1

                    y = 0

                else:

                    x = -1

                    y = 0

                while path:

                    if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and 0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:

                        moves_list.append(

                            (position[0] + (chain * x), position[1] + (chain * y)))

                        if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:

                            path = False

                        chain += 1

                    else:

                        path = False

            return moves_list

        # check valid pawn moves
        def check_pawn(position, color):

            moves_list = []

            if color == 'white':

                if (position[0], position[1] + 1) not in white_locations and (position[0], position[1] + 1) not in black_locations and position[1] < 7:

                    moves_list.append((position[0], position[1] + 1))

                if (position[0], position[1] + 2) not in white_locations and (position[0], position[1] + 2) not in black_locations and position[1] == 1:

                    moves_list.append((position[0], position[1] + 2))

                if (position[0] + 1, position[1] + 1) in black_locations:

                    moves_list.append((position[0] + 1, position[1] + 1))

                if (position[0] - 1, position[1] + 1) in black_locations:

                    moves_list.append((position[0] - 1, position[1] + 1))

            else:

                if (position[0], position[1] - 1) not in white_locations and (position[0], position[1] - 1) not in black_locations and position[1] > 0:

                    moves_list.append((position[0], position[1] - 1))

                if (position[0], position[1] - 2) not in white_locations and (position[0], position[1] - 2) not in black_locations and position[1] == 6:

                    moves_list.append((position[0], position[1] - 2))

                if (position[0] + 1, position[1] - 1) in white_locations:

                    moves_list.append((position[0] + 1, position[1] - 1))

                if (position[0] - 1, position[1] - 1) in white_locations:

                    moves_list.append((position[0] - 1, position[1] - 1))

            return moves_list

        # check valid knight moves
        def check_knight(position, color):

            moves_list = []

            if color == 'white':

                enemies_list = black_locations

                friends_list = white_locations

            else:

                friends_list = black_locations

                enemies_list = white_locations

            # 8 squares to check for knights, they can go two squares in one direction and one in another

            targets = [(1, 2), (1, -2), (2, 1), (2, -1),

                    (-1, 2), (-1, -2), (-2, 1), (-2, -1)]

            for i in range(8):

                target = (position[0] + targets[i][0], position[1] + targets[i][1])

                if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:

                    moves_list.append(target)

            return moves_list

        # check for valid moves for just selected piece
        def check_valid_moves():

            if turn_step < 2:

                options_list = white_options

            else:

                options_list = black_options

            valid_options = options_list[selection]

            return valid_options

        # draw valid moves on screen
        def draw_valid(moves):

            if turn_step < 2:

                color = 'red'

            else:

                color = 'blue'

            for i in range(len(moves)):

                pygame.draw.circle(

                    screen, color, (moves[i][0] * 100 + 50, moves[i][1] * 100 + 50), 5)


        # draw captured pieces on side of screen
        def draw_captured():

            for i in range(len(captured_pieces_white)):

                captured_piece = captured_pieces_white[i]

                index = piece_list.index(captured_piece)

                screen.blit(small_black_images[index], (825, 5 + 50 * i))

            for i in range(len(captured_pieces_black)):

                captured_piece = captured_pieces_black[i]

                index = piece_list.index(captured_piece)

                screen.blit(small_white_images[index], (925, 5 + 50 * i))

        
        # draw a flashing square around king if in check
        def draw_check():

            if turn_step < 2:

                if 'king' in white_pieces:

                    king_index = white_pieces.index('king')

                    king_location = white_locations[king_index]

                    for i in range(len(black_options)):

                        if king_location in black_options[i]:

                            if counter < 15:

                                pygame.draw.rect(screen, 'dark red', [white_locations[king_index][0] * 100 + 1,

                                                                    white_locations[king_index][1] * 100 + 1, 100, 100], 5)

            else:

                if 'king' in black_pieces:

                    king_index = black_pieces.index('king')

                    king_location = black_locations[king_index]

                    for i in range(len(white_options)):

                        if king_location in white_options[i]:

                            if counter < 15:

                                pygame.draw.rect(screen, 'dark blue', [black_locations[king_index][0] * 100 + 1,

                                                                    black_locations[king_index][1] * 100 + 1, 100, 100], 5)

        def draw_game_over():
            pygame.draw.rect(screen, 'black', [200, 200, 400, 70])

            screen.blit(font.render(

                f'{winner} won the game!', True, 'white'), (210, 210))

            screen.blit(font.render(f'Press ENTER to Restart!',

                        True, 'white'), (210, 240))

        # main game loop
        black_options = check_options(black_pieces, black_locations, 'black')
        white_options = check_options(white_pieces, white_locations, 'white')
        run = True
        while run:

            timer.tick(fps)

            if counter < 30:

                counter += 1

            else:

                counter = 0

            screen.fill('dark gray')

            draw_board()

            draw_pieces()

            draw_captured()

            draw_check()

            if selection != 100:

                valid_moves = check_valid_moves()

                draw_valid(valid_moves)

            # event handling

            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over:

                    x_coord = event.pos[0] // 100

                    y_coord = event.pos[1] // 100

                    click_coords = (x_coord, y_coord)

                    if turn_step <= 1:

                        if click_coords == (8, 8) or click_coords == (9, 8):

                            winner = 'black'

                        if click_coords in white_locations:

                            selection = white_locations.index(click_coords)

                            if turn_step == 0:

                                turn_step = 1

                        if click_coords in valid_moves and selection != 100:

                            white_locations[selection] = click_coords

                            if click_coords in black_locations:

                                black_piece = black_locations.index(click_coords)

                                captured_pieces_white.append(black_pieces[black_piece])

                                if black_pieces[black_piece] == 'king':

                                    winner = 'white'

                                black_pieces.pop(black_piece)

                                black_locations.pop(black_piece)

                            black_options = check_options(

                                black_pieces, black_locations, 'black')

                            white_options = check_options(

                                white_pieces, white_locations, 'white')

                            turn_step = 2

                            selection = 100

                            valid_moves = []

                    if turn_step > 1:

                        if click_coords == (8, 8) or click_coords == (9, 8):

                            winner = 'white'

                        if click_coords in black_locations:

                            selection = black_locations.index(click_coords)

                            if turn_step == 2:

                                turn_step = 3

                        if click_coords in valid_moves and selection != 100:

                            black_locations[selection] = click_coords

                            if click_coords in white_locations:

                                white_piece = white_locations.index(click_coords)

                                captured_pieces_black.append(white_pieces[white_piece])

                                if white_pieces[white_piece] == 'king':

                                    winner = 'black'

                                white_pieces.pop(white_piece)

                                white_locations.pop(white_piece)

                            black_options = check_options(

                                black_pieces, black_locations, 'black')

                            white_options = check_options(

                                white_pieces, white_locations, 'white')

                            turn_step = 0

                            selection = 100

                            valid_moves = []

                if event.type == pygame.KEYDOWN and game_over:

                    if event.key == pygame.K_RETURN:

                        game_over = False

                        winner = ''

                        white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',

                                        'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']

                        white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),

                                        (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]

                        black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',

                                        'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']

                        black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),

                                        (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]

                        captured_pieces_white = []

                        captured_pieces_black = []

                        turn_step = 0

                        selection = 100

                        valid_moves = []

                        black_options = check_options(

                            black_pieces, black_locations, 'black')

                        white_options = check_options(

                            white_pieces, white_locations, 'white')

        

            if winner != '':

                game_over = True

                draw_game_over()

        

            pygame.display.flip()
        pygame.quit()
        # Add the PvP chess logic here
    run_pvp_game()    


def start_ai():
    # Code from Chess.py
    print("Starting Player vs Computer Chess...")
    import pygame
    import chess
    import chess.engine
    import os

    # Initialize pygame
    pygame.init()

    # Constants
    WIDTH, HEIGHT = 800, 800
    BOARD_SIZE = 8
    SQUARE_SIZE = WIDTH // BOARD_SIZE
    COLORS = [(240, 217, 181), (181, 136, 99)]  # Light and dark squares
    PIECE_IMAGES = {}

    # Update with your Stockfish path
    STOCKFISH_PATH = r"D:\Game Project\stockfish-windows-x86-64\stockfish\stockfish-windows-x86-64.exe"

    # Load piece images
    IMAGE_DIR = r"D:\Game Project\Pieces1"  # Update with the correct folder path
    piece_types = ['p', 'r', 'n', 'b', 'q', 'k']
    colors = ['w', 'b']

    for color in colors:
        for piece in piece_types:
            image_path = os.path.join(IMAGE_DIR, f"{color}{piece}.png")
            if os.path.exists(image_path):
                PIECE_IMAGES[color + piece] = pygame.transform.scale(
                    pygame.image.load(image_path), (SQUARE_SIZE, SQUARE_SIZE)
                )
            else:
                print(f"Warning: Missing file {image_path}. The game may not display pieces correctly.")

    # Start Stockfish engine
    try:
        engine = chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH)
        print("Stockfish engine initialized successfully!")
    except Exception as e:
        print(f"Error: Unable to start Stockfish engine. Check path. {e}")
        exit()

    # Initialize board
    board = chess.Board()

    # Pygame window setup
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("AI-Powered Chess")

    # Convert pygame click coordinates to UCI format
    def get_square_from_mouse(pos):
        x, y = pos
        col = x // SQUARE_SIZE
        row = 7 - (y // SQUARE_SIZE)  # Invert row to match chess library's indexing
        return chess.square(col, row)

    # Draw chessboard
    def draw_board(selected_square=None):
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                color = COLORS[(row + col) % 2]
                pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

        if selected_square is not None:
            highlight_moves(selected_square)

    # Draw pieces on the board
    def draw_pieces():
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                square = chess.square(col, 7 - row)
                piece = board.piece_at(square)
                if piece:
                    piece_key = ('w' if piece.color == chess.WHITE else 'b') + piece.symbol().lower()
                    image = PIECE_IMAGES.get(piece_key)
                    if image:
                        screen.blit(image, (col * SQUARE_SIZE, row * SQUARE_SIZE))

    # Highlight possible legal moves
    def highlight_moves(selected_square):
        for move in board.legal_moves:
            if move.from_square == selected_square:
                col, row = chess.square_file(move.to_square), 7 - chess.square_rank(move.to_square)
                center = (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2)
                pygame.draw.circle(screen, (0, 255, 0, 100), center, SQUARE_SIZE // 6)  # Green transparent circle

    # Handle AI move
    def ai_move():
        if not board.is_game_over():
            result = engine.play(board, chess.engine.Limit(time=0.5))  # AI takes half a second per move
            board.push(result.move)

    # Main game loop
    def main():
        running = True
        selected_square = None

        while running:
            draw_board(selected_square)
            draw_pieces()
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.MOUSEBUTTONDOWN and not board.is_game_over():
                    square = get_square_from_mouse(event.pos)

                    if selected_square is None:
                        piece = board.piece_at(square)
                        if piece and piece.color == board.turn:
                            selected_square = square
                    else:
                        move = chess.Move(selected_square, square)
                        if move in board.legal_moves:
                            board.push(move)
                            pygame.time.delay(500)  # Delay before AI moves
                            ai_move()
                        else:
                            print("Invalid move!")
                        selected_square = None  # Reset selection

        engine.quit()
        pygame.quit()

    if __name__ == "__main__":
        main()

    # Add the AI chess logic here

def get_choice():
    def on_submit():
        choice = var.get()
        if choice:
            root.choice = choice  # Store choice in root window
            root.destroy()  # Close UI
        else:
            messagebox.showwarning("Warning", "Please make a selection!")

    root = tk.Tk()
    root.title("Main Menu")
    root.geometry("300x200")

    tk.Label(root, text="Choose an option:").pack(pady=10)

    var = tk.StringVar(value="")

    choices = {
        "1": "Start PVP",
        "2": "Start PVE",
        "3": "Exit"
    }

    for key, value in choices.items():
        tk.Radiobutton(root, text=value, variable=var, value=key).pack(anchor="w")

    tk.Button(root, text="Submit", command=on_submit).pack(pady=20)

    root.choice = None  # Default value
    root.mainloop()

    return root.choice  # Return selected choice after closing UI

def main():
    while True:
        choice = get_choice()  # Get user choice from UI

        if choice == "1":
            start_pvp()
        elif choice == "2":
            start_ai()
        elif choice == "3":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()

