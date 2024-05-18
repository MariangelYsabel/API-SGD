# API-SGD
API de Sistema de Gestión de Discografica 
# Artistas
  # Post
  http://mariangelysabel.pythonanywhere.com/artistas
    JSON: {"nombre": valor}
  # get
  http://mariangelysabel.pythonanywhere.com/artistas/id_artista
  # put
  http://mariangelysabel.pythonanywhere.com/artistas/id_artista
    JSON: {"nombre": valor}
  # Delete
  http://mariangelysabel.pythonanywhere.com/artistas/id_artista

# Albums
  # Post
  http://mariangelysabel.pythonanywhere.com/albums
    JSON: {"titulo": valor, "ano_publicacion": valor, "artista_id": valor}
  # get
  http://mariangelysabel.pythonanywhere.com/albums/id_album
  # put
  http://mariangelysabel.pythonanywhere.com/albums/id_album
    JSON: {"titulo": valor, "ano_publicacion": valor, "artista_id": valor}
  # Delete
  http://mariangelysabel.pythonanywhere.com/albums/id_album

# Canciones
  # Post
  http://mariangelysabel.pythonanywhere.com/canciones
    JSON: {"titulo": valor, "duracion": valor, "album_id": valor}
  # get
  http://mariangelysabel.pythonanywhere.com/canciones/id_cancion
  # put
  http://mariangelysabel.pythonanywhere.com/canciones/id_cancion
    JSON: {"titulo": valor, "duracion": valor, "album_id": valor}
  # Delete
  http://mariangelysabel.pythonanywhere.com/canciones/id_cancion
