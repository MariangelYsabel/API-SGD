from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///discografica.db'
db = SQLAlchemy(app)

# Definición de modelos/entidades
class Artista(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    albums = db.relationship('Album', backref='artista', lazy=True)

class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    año_publicacion = db.Column(db.Integer, nullable=False)
    artista_id = db.Column(db.Integer, db.ForeignKey('artista.id'), nullable=False)
    canciones = db.relationship('Cancion', backref='album', lazy=True)

class Cancion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    duracion = db.Column(db.Integer, nullable=False)  # Duración en segundos
    album_id = db.Column(db.Integer, db.ForeignKey('album.id'), nullable=False)

# Crear la base de datos
@app.before_first_request
def crear_tablas():
    db.create_all()

# Métodos CRUD para Artista
@app.route('/artistas', methods=['POST'])
def agregar_artista():
    data = request.get_json()
    nuevo_artista = Artista(nombre=data['nombre'])
    db.session.add(nuevo_artista)
    db.session.commit()
    return jsonify({'mensaje': 'Artista agregado exitosamente'}), 201

@app.route('/artistas/<int:id>', methods=['GET'])
def obtener_artista(id):
    artista = Artista.query.get(id)
    if artista:
        return jsonify({'id': artista.id, 'nombre': artista.nombre})
    else:
        return jsonify({'mensaje': 'Artista no encontrado'}), 404

@app.route('/artistas/<int:id>', methods=['PUT'])
def actualizar_artista(id):
    artista = Artista.query.get(id)
    if artista:
        data = request.get_json()
        artista.nombre = data['nombre']
        db.session.commit()
        return jsonify({'mensaje': 'Artista actualizado exitosamente'})
    else:
        return jsonify({'mensaje': 'Artista no encontrado'}), 404

@app.route('/artistas/<int:id>', methods=['DELETE'])
def eliminar_artista(id):
    artista = Artista.query.get(id)
    if artista:
        db.session.delete(artista)
        db.session.commit()
        return jsonify({'mensaje': 'Artista eliminado exitosamente'})
    else:
        return jsonify({'mensaje': 'Artista no encontrado'}), 404

# Métodos CRUD para Album
@app.route('/albums', methods=['POST'])
def agregar_album():
    data = request.get_json()
    nuevo_album = Album(titulo=data['titulo'], año_publicacion=data['año_publicacion'], artista_id=data['artista_id'])
    db.session.add(nuevo_album)
    db.session.commit()
    return jsonify({'mensaje': 'Álbum agregado exitosamente'}), 201

@app.route('/albums/<int:id>', methods=['GET'])
def obtener_album(id):
    album = Album.query.get(id)
    if album:
        return jsonify({'id': album.id, 'titulo': album.titulo, 'año_publicacion': album.año_publicacion, 'artista_id': album.artista_id})
    else:
        return jsonify({'mensaje': 'Álbum no encontrado'}), 404

@app.route('/albums/<int:id>', methods=['PUT'])
def actualizar_album(id):
    album = Album.query.get(id)
    if album:
        data = request.get_json()
        album.titulo = data['titulo']
        album.año_publicacion = data['año_publicacion']
        album.artista_id = data['artista_id']
        db.session.commit()
        return jsonify({'mensaje': 'Álbum actualizado exitosamente'})
    else:
        return jsonify({'mensaje': 'Álbum no encontrado'}), 404

@app.route('/albums/<int:id>', methods=['DELETE'])
def eliminar_album(id):
    album = Album.query.get(id)
    if album:
        db.session.delete(album)
        db.session.commit()
        return jsonify({'mensaje': 'Álbum eliminado exitosamente'})
    else:
        return jsonify({'mensaje': 'Álbum no encontrado'}), 404

# Métodos CRUD para Cancion
@app.route('/canciones', methods=['POST'])
def agregar_cancion():
    data = request.get_json()
    nueva_cancion = Cancion(titulo=data['titulo'], duracion=data['duracion'], album_id=data['album_id'])
    db.session.add(nueva_cancion)
    db.session.commit()
    return jsonify({'mensaje': 'Canción agregada exitosamente'}), 201

@app.route('/canciones/<int:id>', methods=['GET'])
def obtener_cancion(id):
    cancion = Cancion.query.get(id)
    if cancion:
        return jsonify({'id': cancion.id, 'titulo': cancion.titulo, 'duracion': cancion.duracion, 'album_id': cancion.album_id})
    else:
        return jsonify({'mensaje': 'Canción no encontrada'}), 404

@app.route('/canciones/<int:id>', methods=['PUT'])
def actualizar_cancion(id):
    cancion = Cancion.query.get(id)
    if cancion:
        data = request.get_json()
        cancion.titulo = data['titulo']
        cancion.duracion = data['duracion']
        cancion.album_id = data['album_id']
        db.session.commit()
        return jsonify({'mensaje': 'Canción actualizada exitosamente'})
    else:
        return jsonify({'mensaje': 'Canción no encontrada'}), 404

@app.route('/canciones/<int:id>', methods=['DELETE'])
def eliminar_cancion(id):
    cancion = Cancion.query.get(id)
    if cancion:
        db.session.delete(cancion)
        db.session.commit()
        return jsonify({'mensaje': 'Canción eliminada exitosamente'})
    else:
        return jsonify({'mensaje': 'Canción no encontrada'}), 404

if __name__ == '__main__':
    app.run(debug=True)
