from audio_manager import AudioManager

class GameEngine:
    def __init__(self, story):
        print("Inicializando el motor del juego...")  # Depuración
        self.story = story
        self.audio_manager = AudioManager()

    def start(self):
        print("Iniciando el juego...")  # Depuración
        print("Bienvenido a 'El Misterio del Bosque Sombrío'.")
        print("Presiona Enter para avanzar en la historia...\n")
        current_section = "inicio"

        while True:
            lines = self.story.get_section(current_section)
            if not lines:
                print("El juego ha terminado. ¡Gracias por jugar!")
                break

            for line in lines:
                print(line.strip())

                # Reproducir el sonido correspondiente a la línea (si aplica)
                self.audio_manager.play_sound_for_line(line)

                # Si la línea es una pregunta, manejar las opciones
                if line.startswith("¿Qué decides hacer?"):
                    next_section = self.get_player_choice(lines)
                    if next_section:
                        current_section = next_section
                        self.audio_manager.stop_sound()  # Detener el sonido antes de continuar
                    break
            else:
                input("Presiona Enter para continuar...\n")

    def get_player_choice(self, lines):
        """Obtener la elección del jugador y devolver la sección correspondiente."""
        # Las opciones empiezan en la línea después de la pregunta
        options = [line.strip() for line in lines if line.strip().startswith("1.") or line.strip().startswith("2.")]

        if not options:
            print("No hay opciones válidas disponibles.")
            return None

        # Mostrar las opciones correctas
        for option in options:
            print(option)

        while True:
            choice = input(f"¿Qué decides hacer? (1-{len(options)}): ")

            try:
                choice_index = int(choice) - 1
                if 0 <= choice_index < len(options):
                    # Extrae la opción y determina la siguiente sección basada en la elección
                    selected_option = options[choice_index]
                    # La sección debe estar bien definida en el formato del archivo `story.txt`
                    if "1." in selected_option:
                        return f"opcion_1_{choice_index + 1}"
                    elif "2." in selected_option:
                        return f"opcion_2_{choice_index + 1}"
                else:
                    print("Opción inválida. Intenta nuevamente.")
            except ValueError:
                print("Por favor ingresa un número válido.")
