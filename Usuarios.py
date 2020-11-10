class Usuario:

#Si se recibe como tipoUs un 1 -> administrador, un 2 -> cliente
    def __init__(self,nombre,apellido,usuario,contrasena,tipoUs):
        self.nombre = nombre
        self.apellido = apellido
        self.usuario = usuario
        self.contrasena = contrasena
        self.tipoUs = tipoUs

#METODOS - GET
    
    def getNombre(self):
        return self.nombre
    
    def getApellido(self):
        return self.apellido

    def getUsuario(self):
        return self.usuario

    def getContrasena(self):
        return self.contrasena
    
    def getTipoUs(self):
        return self.tipoUs


#METODOS - SET

    def setNombre(self,nombre):
        self.nombre = nombre
    
    def setApellido(self,apellido):
        self.apellido = apellido

    def setUsuario(self,usuario):
        self.usuario = usuario
    
    def setContrasena(self,contrasena):
        self.contrasena = contrasena
    
    def setTipoUs(self,tipoUs):
        self.tipoUs = tipoUs
    
    
    
    
    
