class Cliente():
    def __init__(self, nombre, identidad, objetivo, patologias, inscripcion, fecha_final):
        self.nombre = nombre
        self.identidad = identidad
        self.objetivo = objetivo
        self.patologias = patologias
        self.inscripcion = inscripcion
        self.fecha_final = fecha_final
        self.permiso = True