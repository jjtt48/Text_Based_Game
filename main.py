from game_engine import GameEngine
from story import Story

def main():
    # Cargar la historia desde un archivo de texto
    story = Story("story.txt")

    # Inicializar el motor del juego con la historia cargada
    game = GameEngine(story)

    # Iniciar el juego
    game.start()

main()
