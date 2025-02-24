# hook.py
from PyInstaller.utils.hooks import collect_data_files

# Inclure les fichiers supplémentaires
datas = [
    ("images/*", "images"),  # Inclure le dossier "images"
    ("piecespro.py", "."),      # Inclure le fichier pieces.py
    ("enginepro.py", "."),      # Inclure le fichier engine.py
    ("stockfish/*", "stockfish"),  # Inclure le dossier "stockfish"
    ("stockfish/windows/*", "stockfish/windows"),  # Inclure le dossier "stockfish/windows"
]