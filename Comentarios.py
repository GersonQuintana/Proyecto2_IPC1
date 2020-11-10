class Comentario:

    def __init__(self,cancion,persona,comentario):
        self.cancion = cancion
        self.persona = persona
        self.comentario = comentario
        print("La persona es ", persona)
        print("El comentario es ",comentario)

#METODOS - GET
    def getCancion(self):
        return self.cancion

    def getPersona(self):
        return self.persona

    def getComentario(self):
        return self.comentario

#METODOS - SET
    def setCancion(self,cancion):
        self.cancion = cancion

    def setPersona(self,persona):
        self.persona = persona

    def setComentario(self,comentario):
        self.comentario = comentario
    