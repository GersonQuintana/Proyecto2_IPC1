from flask import Flask, jsonify, request
from flask_cors import CORS
import json
from Usuarios import Usuario
from Canciones import Cancion
from Comentarios import Comentario
from Playlist import Lista
from CancionesSolicitadas import CancionSol

app = Flask(__name__)
CORS(app)

Usuarios = []
Canciones = []
Comentarios = []
Playlists = []
CancionesPedidas = []

Usuarios.append(Usuario('Usuario','Maestro','admin','admin',"1"))

@app.route('/', methods=['GET'])
def inicio():
    return ('<h1>PAGINA PRINCIPAL</h1>')

#METODO - LOGIN
@app.route('/Login', methods=['POST'])
def login():
    global Usuarios
    usarme = request.json['usuario']
    password = request.json['password']
    for usuario in Usuarios:
        if usuario.getUsuario() == usarme and usuario.getContrasena() == password:
            Dato = {
                'tipoUs': usuario.getTipoUs(),
                'message': 'Succes',
                'usuario': usuario.getUsuario()
            }
            break
        else:
            Dato = {
                'message': 'Failed',
                'usuario': ' '
            }
    respuesta = jsonify(Dato)
    return (respuesta)

#METODO - REGISTRAR USUARIO TIPO CLIENTE
@app.route('/Registrar', methods=['POST'])
def RegistrarUsuario():
    global Usuarios
    nombre = request.json['nombre']
    apellido = request.json['apellido']
    usarme = request.json['username']
    contrasena = request.json['contrasena']
    encontrado = False
    for usuario in Usuarios:
        if usuario.getUsuario() == usarme:
            encontrado = True
            print(usuario.getUsuario())
            print("si entro", usarme)
            break
    if encontrado:
        return jsonify({
            'message': 'Failed'
            #'reason': 'El usuario ha sido registrado'
        })
    else:
        Usuarios.append(Usuario(nombre,apellido,usarme,contrasena,"2"))
        #Usuarios.append(nuevo)        
        return jsonify({
            'message': 'Succes'
            #'reason': 'Se agregó el usuario'
        })

#METODO - REGISTRAR USUARIO TIPO CLIENTE
@app.route('/RegistrarAdmin', methods=['POST'])
def RegistrarUsuarioAdmin():
    global Usuarios
    nombre = request.json['nombre']
    apellido = request.json['apellido']
    usarme = request.json['username']
    contrasena = request.json['contrasena']
    encontrado = False
    for usuario in Usuarios:
        if usuario.getUsuario() == usarme:
            encontrado = True
            print(usuario.getUsuario())
            print("si entro", usarme)
            break
    if encontrado:
        return jsonify({
            'message': 'Failed'
        })
    else:
        Usuarios.append(Usuario(nombre,apellido,usarme,contrasena,"1"))
        return jsonify({
            'message': 'Succes'
        })
        
@app.route('/RecuperarContrasena', methods=['POST'])
def RecuperarContrasena():
    global Usuarios
    usarme = request.json['usuario']
    contrasena = ""
    encontrado = False
    for username in Usuarios:
        print(username)
        if username.getUsuario() == usarme:
            encontrado = True
            contrasena = username.getContrasena()
            break
    if encontrado:
        return jsonify({
            'message': 'Succes',
            'contrasena': contrasena
        })
    else:
        print("entro a no recuperado",usarme)
        return jsonify({
            'message': 'Failed',
            'contrasena': contrasena
        })

@app.route('/Registrar', methods=['GET'])
def obtenerUsuarios():
    global Usuarios
    Datos = []
    for usuario in Usuarios:
            Dato = {
             'nombre': usuario.getNombre(), 
             'apellido': usuario.getApellido(), 
             "usuario": usuario.getUsuario(),
             "password": usuario.getContrasena()
             }
            print("Si entro aqui", usuario.getContrasena())
            Datos.append(Dato)
    respuesta = jsonify(Datos)
    return(respuesta)

@app.route('/Usuario/<string:nombre>', methods=['GET'])
def ObtenerUsuario(nombre):
    print("Si entro aqui")
    global Usuarios
    Dato =""
    for usuario in Usuarios:
        if usuario.getUsuario() == nombre:
            Dato = {
                'nombre': usuario.getNombre(),
                'apellido': usuario.getApellido(),
                'usuario': usuario.getUsuario(),
                'contrasena': usuario.getContrasena()
                }
            print("Si entro aquí a Usuario/nombre")
            break
    respuesta = jsonify(Dato)
    print(Dato)
    return (respuesta)

@app.route('/Usuarios/<string:usuario>',methods=['DELETE'])
def EliminarUsuario(usuario):
    print("Si entra al metodo DELETE usuario")
    global Usuarios
    for i in range(len(Usuarios)):
        if Usuarios[i].getUsuario() == usuario:
            del Usuarios[i]
            break
    return jsonify({'message': 'Se eliminó el usuarios exitosamente.'})

@app.route('/Usuarios/ModificarUsuario/<string:name>', methods=['PUT'])
def ActualizarUsuario(name):    
    global Usuarios
    print("Si entro aqui a ModificarUsuario",name)
    for i in range(len(Usuarios)):
        if name == Usuarios[i].getUsuario():
            return jsonify({'message':'Error'})
            break
        else:
            Usuarios[i].setNombre(request.json['nombre'])
            Usuarios[i].setApellido(request.json['apellido'])
            Usuarios[i].setUsuario(request.json['usuario'])
            Usuarios[i].setContrasena(request.json['contrasena'])
            return jsonify({'message': 'Succes'})
            break

# RUTA - PARA MODIFICAR UN USUARIO MEDIA VEZ NO HAYA CAMBIADO EL NOMBRE DE USUARIO (PERFIL.HTML)    
@app.route('/Usuarios/ModificarUsuarioDif/<string:name>', methods=['PUT'])
def ModificarUser(name):    
    global Usuarios
    print("Si entro aqui a ModificarUsuario",name)
    for i in range(len(Usuarios)):
        if name == Usuarios[i].getUsuario():
            Usuarios[i].setNombre(request.json['nombre'])
            Usuarios[i].setApellido(request.json['apellido'])
            Usuarios[i].setUsuario(request.json['usuario'])
            Usuarios[i].setContrasena(request.json['contrasena'])
            return jsonify({'message': 'Succes'})
            break

@app.route('/Musica', methods=['GET'])
def mostrarCanciones():
    global Canciones
    print("Si entro aqui a /Musica")
    Datos = []
    for cancion in Canciones:
        Dato = {
            'nombre': cancion.getNombre(),
            'artista': cancion.getArtista(),
            'album': cancion.getAlbum(),
            'imagen': cancion.getImagen(),
            'fecha': cancion.getFecha(),
            'spotify': cancion.getSpotify(),
            'verDetalles': 'Ver Detalles',
            'agregarPlaylist': 'Agregar a mi playlist'  
        }
        print(cancion.getSpotify())
        Datos.append(Dato)
    respuesta = jsonify(Datos)
    return (respuesta)

# RUTA - PARA VER LA LISTA DE LAS CANCIONES SOLICITADAS
@app.route('/MusicaSolicitada', methods=['GET'])
def mostrarCancionesSolicitadas():
    global CancionesPedidas
    print("Si entro aqui a /Musica")
    Datos = []
    for cancion in CancionesPedidas:
        Dato = {
            'nombre': cancion.getNombre(),
            'artista': cancion.getArtista(),
            'album': cancion.getAlbum(),
            'imagen': cancion.getImagen(),
            'fecha': cancion.getFecha(),
            'spotify': cancion.getSpotify()
        }
        print(cancion.getSpotify())
        Datos.append(Dato)
    respuesta = jsonify(Datos)
    return (respuesta)

# RUTA - PARA ELIMINAR ALGUNA CANCIÓN SOLICITADA
@app.route('/EliminarCancionSolicitada/<string:nombre>',methods=['DELETE'])
def EliminarCancionPedida(nombre):
    print("Si entra al metodo DELETE")
    global CancionesPedidas
    for i in range(len(CancionesPedidas)):
        if CancionesPedidas[i].getNombre() == nombre:
            del CancionesPedidas[i]
            break
    return jsonify({'message': 'Se eliminó la cancion exitosamente la canción solicitada.'})

# RUTA - PARA OBTENER TODOS LOS DATOS DE UNA CANCIÓN SOLICITADA 
@app.route('/CancionesSolicitadas/<string:nombre>', methods=['GET'])
def ObtenerCancionSolicitada(nombre):
    print("Si entro aqui")
    global CancionesPedidas
    for cancion in CancionesPedidas:
        if cancion.getNombre() == nombre:
            Dato = {
                'nombre': cancion.getNombre(),
                'artista': cancion.getArtista(),
                'album': cancion.getAlbum(),
                'imagen': cancion.getImagen(),
                'fecha': cancion.getFecha(),
                'spotify': cancion.getSpotify(),
                'youtube': cancion.getYoutube()
                }
            print("Si entro aqui a /CancionesSolicitadas/", cancion.getNombre())
            break
    respuesta = jsonify(Dato)
    print(Dato)
    return (respuesta)

@app.route('/Musica/<string:nombre>', methods=['GET'])
def ObtenerCancion(nombre):
    print("Si entro aqui")
    global Canciones
    Dato =""
    for cancion in Canciones:
        if cancion.getNombre() == nombre:
            Dato = {
                'nombre': cancion.getNombre(),
                'artista': cancion.getArtista(),
                'album': cancion.getAlbum(),
                'imagen': cancion.getImagen(),
                'fecha': cancion.getFecha(),
                'spotify': cancion.getSpotify(),
                'youtube': cancion.getYoutube()
                }
            print("Si entro aqui", cancion.getNombre())
            break
    respuesta = jsonify(Dato)
    print(Dato)
    return (respuesta)

@app.route('/Musica/Comentario',methods=['POST'])
def ObtenerComentario():
    print("Si está entrando", comentario.getPersona())
    global Comentarios
    Datos = []
    for comentario in Comentarios:
        Dato = {
            'persona': comentario.getPersona(),
            'comentario': comentario.getComentario()
        }
        Datos.append(Dato)
        print("Si está entrando", comentario.getPersona())
    respuesta = jsonify(Datos)
    return (respuesta)

@app.route('/Musica/ComentarioNuevo',methods=['PUT'])
def NuevoComentario():
    global Comentarios
    Comentarios.append(Comentario(request.json['cancion'],request.json['persona'],request.json['comentario']))
    return jsonify({'message':'Se actualizo el dato exitosamente'})

@app.route('/Musica/Comentarios/<string:nombre_cancion>', methods=['GET'])
def Mostrar(nombre_cancion):
    global Comentarios
    print("Si entro aqui a ListasComentarios")
    Datos = []
    for comentario in Comentarios:
        if comentario.getCancion() == nombre_cancion:
            Dato = {
            'cancion': comentario.getCancion(),
            'persona': comentario.getPersona(),
            'comentario': comentario.getComentario()
            }
            print("La cancione es", comentario.getComentario())
            Datos.append(Dato)
    respuesta = jsonify(Datos)
    return (respuesta)
    
@app.route('/Musica/<string:nombre>',methods=['DELETE'])
def EliminarCancion(nombre):
    print("Si entra al metodo DELETE")
    global Canciones
    for i in range(len(Canciones)):
        if Canciones[i].getNombre() == nombre:
            del Canciones[i]
            break
    return jsonify({'message': 'Se eliminó la cancion exitosamente.'})

@app.route('/Musica/ModificarCancion/<string:name>', methods=['PUT'])
def ActualizarCancion(name):
    global Canciones
    for i in range(len(Canciones)):
        if name == Canciones[i].getNombre():
            Canciones[i].setNombre(request.json['nombre'])
            Canciones[i].setArtista(request.json['artista'])
            Canciones[i].setAlbum(request.json['album'])
            Canciones[i].setFecha(request.json['fecha'])
            Canciones[i].setImagen(request.json['imagen'])
            Canciones[i].setSpotify(request.json['spotify'])
            Canciones[i].setYoutube(request.json['youtube'])
            break
    return jsonify({'message':'Se actualizo el dato exitosamente'})

@app.route('/CargarCanciones', methods=['POST'])
def guardarCanciones():
    global Canciones
    nombre = request.json['nombre']
    artist = request.json['artista']
    album = request.json['album']
    fecha = request.json['fecha']
    imagen = request.json['imagen']
    spotify = request.json['spotify']
    youtube = request.json['youtube']
    nuevo = Cancion(nombre, artist, album, fecha, imagen, spotify, youtube)
    Canciones.append(nuevo)
    print("Si entro a CargarCanciones")
    return jsonify({
        'message': 'Succes',
        'reason': 'Se agregó la canción'
    })

@app.route('/SolicitarCancion', methods=['POST'])
def GuardarSolicitudes():
    global CancionesPedidas
    nombre = request.json['nombre']
    artist = request.json['artista']
    album = request.json['album']
    fecha = request.json['fecha']
    imagen = request.json['imagen']
    spotify = request.json['spotify']
    youtube = request.json['youtube']
    nuevo = CancionSol(nombre, artist, album, fecha, imagen, spotify, youtube)
    CancionesPedidas.append(nuevo)
    print("Si entro a CargarSolicitadas")
    return jsonify({
        'message': 'Succes',
        'reason': 'Se agregó la canción'
    })

@app.route('/AgregarPlaylist', methods=['POST'])
def guardarPlaylist():
    global Playlists
    usuario = request.json['usuario']
    nombre = request.json['nombre']
    artist = request.json['artista']
    album = request.json['album']
    fecha = request.json['fecha']
    imagen = request.json['imagen']
    spotify = request.json['spotify']
    youtube = request.json['youtube']
    nuevo = Lista(usuario,nombre, artist, album, fecha, imagen, spotify, youtube)
    Playlists.append(nuevo)
    print("Si entro a /AgregarPlaylist")
    return jsonify({
        'message': 'Succes',
        'reason': 'Se agregó la canción'
    })

@app.route('/MiPlaylist/<string:usuario>', methods=['GET'])
def mostrarPlaylist(usuario):
    global Playlists
    print("Si entro aqui a /MiPlylist", usuario)
    Datos = []
    for user in Playlists:
        if user.getUsuario() == usuario:
            Dato = {
                'usuario': user.getUsuario(),
                'nombre': user.getNombre(),
                'artista': user.getArtista(),
                'album': user.getAlbum(),
                'imagen': user.getImagen(),
                'fecha': user.getFecha(),
                'spotify': user.getSpotify()
            }
            print(user.getSpotify())
            Datos.append(Dato)
    respuesta = jsonify(Datos)
    return (respuesta)
    
if __name__ == "__main__":
    app.run(debug=True)