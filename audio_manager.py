import openal

class AudioManager:
    def __init__(self):
        openal.oalInit()
        self.sounds = self.load_sounds()
        self.current_sound = None  # Variable para almacenar el sonido que se está reproduciendo
    def load_sounds(self):
        """Cargar todos los sonidos necesarios para el juego."""
        return {
            "river": openal.oalOpen("sounds/river_right_far.wav"),
            "horse_distant": openal.oalOpen("sounds/galloping_horse_far.wav"),
            "footsteps": openal.oalOpen("sounds/footsteps.wav"),
            #"branch_snap": openal.oalOpen("sounds/branch_snap.wav"),
            #"thunder": openal.oalOpen("sounds/thunder.wav"),
            #"whisper": openal.oalOpen("sounds/whisper.wav"),
            #"scream": openal.oalOpen("sounds/scream.wav"),
            #"water_splash": openal.oalOpen("sounds/water_splash.wav"),
        }

    def play_sound_for_line(self, line):

        """Reproducir el sonido apropiado basado en el contenido de la línea."""
        if self.current_sound:
            self.stop_sound()  # Detiene cualquier sonido anterior antes de reproducir uno nuevo

        """Reproducir el sonido apropiado basado en el contenido de la línea."""
        if "río" in line:
            self.sounds["river"].play()

        elif "caballo" in line:
            self.sounds["horse_distant"].play()

        elif "pisadas" in line:
            self.sounds["footsteps"].play()

        #elif "rama romperse" in line:
            #self.sounds["branch_snap"].play()
        #elif "trueno" in line:
            #self.sounds["thunder"].play()
        #elif "susurro" in line:
            #self.sounds["whisper"].play()
        #elif "grito" in line:
            #self.sounds["scream"].play()
        #elif "chapoteo" in line:
            #self.sounds["water_splash"].play()


    def stop_sound(self):
        """Detener el sonido actual."""
        if self.current_sound:
           self.current_sound.stop()  # Detiene el sonido actual
           self.current_sound = None  # Reiniciar la variable current_sound


