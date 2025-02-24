# pieces.py
import pygame

# Charger les images des pièces avec des chemins spécifiques
def load_pieces():
    pieces = {
        'r': pygame.image.load(r"C:\Users\Admin\Documents\code\Engine Pro\images\black-rook.png"),
        'n': pygame.image.load(r"C:\Users\Admin\Documents\code\Engine Pro\images\black-knight.png"),
        'b': pygame.image.load(r"C:\Users\Admin\Documents\code\Engine Pro\images\black-bishop.png"),
        'q': pygame.image.load(r"C:\Users\Admin\Documents\code\Engine Pro\images\black-queen.png"),
        'k': pygame.image.load(r"C:\Users\Admin\Documents\code\Engine Pro\images\black-king.png"),
        'p': pygame.image.load(r"C:\Users\Admin\Documents\code\Engine Pro\images\black-pawn.png"),
        'R': pygame.image.load(r"C:\Users\Admin\Documents\code\Engine Pro\images\white-rook.png"),
        'N': pygame.image.load(r"C:\Users\Admin\Documents\code\Engine Pro\images\white-knight.png"),
        'B': pygame.image.load(r"C:\Users\Admin\Documents\code\Engine Pro\images\white-bishop.png"),
        'Q': pygame.image.load(r"C:\Users\Admin\Documents\code\Engine Pro\images\white-queen.png"),
        'K': pygame.image.load(r"C:\Users\Admin\Documents\code\Engine Pro\images\white-king.png"),
        'P': pygame.image.load(r"C:\Users\Admin\Documents\code\Engine Pro\images\white-pawn.png")
    }
    return pieces