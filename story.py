class Story:
    def __init__(self, file_path):
        print(f"Cargando la historia desde {file_path}...")  # Depuración
        self.file_path = file_path
        self.story = self.load_story()

    def load_story(self):
        """Cargar la historia desde el archivo de texto."""
        story = {}
        with open(self.file_path, 'r', encoding='utf-8') as file:
            section = None
            for line in file:
                line = line.strip()
                if line.startswith("#"):  # Identificador de secciones
                    section = line[1:].strip()
                    print(f"Sección detectada: {section}")  # Depuración
                    story[section] = []
                elif section:
                    story[section].append(line)
        return story

    def get_section(self, section_name):
        """Obtener la sección correspondiente a la elección del jugador."""
        return self.story.get(section_name, [])

    def get_next_line(self, section_name):
        """Devolver la siguiente línea de la sección de la historia."""
        if section_name in self.story:
            if self.story[section_name]:  # Verifica que haya más líneas en la sección
                return self.story[section_name].pop(0)
            else:
                return None  # Sección sin más líneas
        return None
