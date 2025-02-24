import chess
import chess.engine

# Chemin vers le moteur Stockfish que jvais programmer
# IL est dur ce truc

def configure_ai(engine_path, elo):
    """
    Configure le moteur d'échecs avec un niveau Elo spécifique.
    """
    global STOCKFISH_PATH
    engine = chess.engine.SimpleEngine.popen_uci(engine_path)
    STOCKFISH_PATH = r"C:\Users\Admin\Documents\code\Engine Pro\stockfish\stockfish-windows-x86-64-sse41-popcnt"

    # Configurer le niveau Elo (si pris en charge par le moteur)
    if "UCI_LimitStrength" in engine.options:
        engine.configure({
        "UCI_LimitStrength": True, "UCI_Elo": elo,
        "Skill Level": 20,  # max
        "Hash": 1024,       # hash de 1024 Mo, 
        "Threads": 4
        })

    else:
        print("Le moteur ne supporte pas la configuration Elo. Utilisation du niveau par défaut.")
    
    return engine
