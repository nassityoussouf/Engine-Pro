import pygame
import sys
from piecespro import *
import chess
from PIL import Image
from enginepro import *

# Icone du jeu
try:
    icon_path = r"C:\Users\Admin\Documents\code\Engine Pro\images\logochess.png"
    icon_image = Image.open(icon_path)
    icon_image = icon_image.convert("RGBA")
    icon_image.save("icon.png")
    icon_image = icon_image.resize((32, 32), Image.LANCZOS)
    icon_image.save("resized_icon.png")
    icon = pygame.image.load("resized_icon.png")
    pygame.display.set_icon(icon)
    print("Icone chargée")
except Exception as e:
    print("Impossible de charger l'icone", e)

# Constantes
WIDTH = 600
HEIGHT = 600
TILE_SIZE = WIDTH // 8
WHITE = (245, 245, 220)
BLACK = (139, 69, 19)
YELLOW = (255, 255, 0)
BUTTON_HOVER = (0, 180, 0)
BUTTON_COLOR = (0, 128, 0)
ANIMATION_STEPS = 19
ANIMATION_DELAY = 40  # en millisecondes

# Initialiser Pygame
pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption('Sk Engine Pro')

# Charger les images des pièces
pieces = load_pieces()

# Initialiser le plateau
board = chess.Board()

def initialize_board():
    global board
    board = chess.Board()  # Initialise le plateau avec la configuration standard
    return board

# Fonction pour dessiner l'échiquier et les pièces

def draw_board(window, board, pieces, tile_size, selected=None):
    """
    Dessine l'échiquier, les pièces, un cercle rouge autour du roi en échec,
    et un cercle vert autour du roi en cas d'échec et mat.
    """
    for row in range(8):
        for col in range(8):
            rect = pygame.Rect(col * tile_size, row * tile_size, tile_size, tile_size)
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(window, color, rect)

            if selected is not None and selected == chess.square(col, row):
                pygame.draw.rect(window, YELLOW, rect, 5)

    # Dessiner les pièces
    for sq in chess.SQUARES:
        piece = board.piece_at(sq)
        if piece:
            row, col = divmod(sq, 8)
            piece_key = piece.symbol()
            piece_img = pygame.transform.scale(pieces[piece_key], (tile_size, tile_size))
            window.blit(piece_img, (col * tile_size, row * tile_size))

    # Vérifier si le roi est en échec et dessiner un cercle rouge
    king_square = None  # Initialiser la variable
    if board.is_check():
        # Trouver la position du roi
        king_color = board.turn  # Le roi en échec est celui du joueur dont c'est le tour
        king_square = board.king(king_color)

    # Dessiner un cercle rouge autour du roi si celui-ci est en échec
    if king_square is not None:
        row, col = divmod(king_square, 8)
        center = (col * tile_size + tile_size // 2, row * tile_size + tile_size // 2)
        radius = tile_size // 2 + 10  # Taille du cercle
        thickness = 5  # Épaisseur du cercle

        # Dessiner un cercle rouge autour du roi
        pygame.draw.circle(window, (255, 0, 0), center, radius, thickness)

    # Vérifier si la partie est terminée par un échec et mat
    if board.is_checkmate():
        # Déterminer qui a perdu (Blancs ou Noirs)
        result = board.result()
        if result == "1-0":
            losing_color = chess.BLACK  # Les Noirs ont perdu
        elif result == "0-1":
            losing_color = chess.WHITE  # Les Blancs ont perdu
        else:
            losing_color = None

        # Trouver la position du roi perdant
        if losing_color is not None:
            losing_king_square = board.king(losing_color)
            if losing_king_square is not None:
                row, col = divmod(losing_king_square, 8)
                center = (col * tile_size + tile_size // 2, row * tile_size + tile_size // 2)
                radius = tile_size // 2 + 10  # Taille du cercle
                thickness = 5  # Épaisseur du cercle

                # Dessiner un cercle vert autour du roi perdant
                pygame.draw.circle(window, (0, 255, 0), center, radius, thickness)

# Écran de démarrage
def start_screen():
    global logo 
    logo = pygame.image.load(r'C:\Users\Admin\Documents\code\Engine Pro\images\logochess.png')
    global font
    running = True
    font = pygame.font.Font(None, 50)
    button_rect = pygame.Rect(200, 400, 200, 50)  # Position du bouton

    while running:
        window.fill(WHITE)
        window.blit(logo, (240, 140))

        # Dessiner le bouton
        mouse_pos = pygame.mouse.get_pos()
        button_color = BUTTON_HOVER if button_rect.collidepoint(mouse_pos) else BUTTON_COLOR
        pygame.draw.rect(window, button_color, button_rect)
        text = font.render("Jouer", True, WHITE)
        text_rect = text.get_rect(center=button_rect.center)
        window.blit(text, text_rect)
        
        credits = font.render("Fait Par Nassit Youssef Ismail", True, (255, 255, 102))
        textpos = (50, 50)

        window.blit(credits, textpos )
        fontName = pygame.font.SysFont("Sigmar One", 70)
        Name = fontName.render("Engine Sk AI", True, (255, 0, 29))
        Namepos = (50, 270)
        window.blit(Name, Namepos)

        schooltext = font.render("Pour L'école Ali", True, (0,0,255))
        schooltextpos = (170, 490)
        window.blit(schooltext, schooltextpos)


        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(mouse_pos):
                    running = False
        

# Fonction principale du jeu
def game_loop():
    global board
    selected_square = None
    running = True

    # Configurer l'IA max
    STOCKFISH_PATH = r"C:\Users\Admin\Documents\code\Engine Pro\stockfish\stockfish-windows-x86-64-sse41-popcnt"
    engine = configure_ai(STOCKFISH_PATH, 3190)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Tour des noirs (joueur humain)
            if board.turn == chess.BLACK:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    col, row = pos[0] // TILE_SIZE, pos[1] // TILE_SIZE
                    selected_square = chess.square(col, row)

                if event.type == pygame.MOUSEBUTTONUP and selected_square is not None:
                    pos = pygame.mouse.get_pos()
                    col, row = pos[0] // TILE_SIZE, pos[1] // TILE_SIZE
                    target_square = chess.square(col, row)

                    move = chess.Move(selected_square, target_square)
                    if move in board.legal_moves:
                        board.push(move)
                    selected_square = None

            # Tour des blancs (IA)
            else:
                result = engine.play(board, chess.engine.Limit(time=2.9, nodes="10000000", depth="20",))  # Temps de réflexion 
                board.push(result.move)

        # Dessiner le plateau
        draw_board(window, board, pieces, TILE_SIZE, selected_square)
        pygame.display.flip()

        # Vérifier la fin de la partie
        if board.is_game_over():
            result = board.result()  # Obtenir le résultat de la partie
            print("Fin de la partie :", result)
            pygame.time.delay(3900)
            engine.quit()  # Fermer le moteur d'échecs
            end_screen(result)  # Afficher l'écran de fin de partie
            running = False  # Quitter la boucle de jeu
            

    pygame.quit()
    sys.exit()

def check_king_positions(board):
    white_king_square = board.king(chess.WHITE)  # Case du roi blanc
    black_king_square = board.king(chess.BLACK)  # Case du roi noir

    # Vérifier la couleur des cases
    white_king_color = (chess.square_rank(white_king_square) + chess.square_file(white_king_square)) % 2
    black_king_color = (chess.square_rank(black_king_square) + chess.square_file(black_king_square)) % 2

    if white_king_color == black_king_color:
        print("Erreur : Les rois sont sur des cases de la même couleur !")
    else:
        print("Les rois sont correctement placés sur des cases de couleurs opposées.")

def end_screen(result):
    """
    Affiche un écran de fin de partie avec le résultat.
    """
    font = pygame.font.Font(None, 74)  # Police pour le message principal
    small_font = pygame.font.Font(None, 50)  # Police pour le bouton

    # Définir le message en fonction du résultat
    if result == "1-0":
        message = "L'ia a gagné !"
    elif result == "0-1":
        message = "Tu as gagné !"
    elif result == "1/2-1/2":
        message = "Match nul (pat) !"
    else:
        message = "Partie terminée !"

    # Bouton pour rejouer
    button_rect = pygame.Rect(200, 400, 200, 50)  # Position et taille du bouton
    button_text = "Rejouer"

    running = True
    while running:
        window.fill(WHITE)  # Fond blanc

        # Afficher le message
        text_surface = font.render(message, True, BLACK)
        text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
        window.blit(text_surface, text_rect)

        # Dessiner le bouton "Rejouer"
        mouse_pos = pygame.mouse.get_pos()
        button_color = BUTTON_HOVER if button_rect.collidepoint(mouse_pos) else BUTTON_COLOR
        pygame.draw.rect(window, button_color, button_rect)
        text_surface = small_font.render(button_text, True, WHITE)
        text_rect = text_surface.get_rect(center=button_rect.center)
        window.blit(text_surface, text_rect)

        pygame.display.flip()

        # Gérer les événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(mouse_pos):
                    running = False  # Quitter l'écran de fin et recommencer

if __name__ == "__main__":
    start_screen()
    board = initialize_board()  # Initialiser le plateau
    check_king_positions(board)  # Vérifier la disposition des rois
    game_loop()