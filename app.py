import os
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.album import Album

from flask import Flask, request

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==


@app.route('/albums', methods=['POST'])
def post_albums():
    title = request.form.get('title')
    release_year = request.form.get('release_year')
    artist_id = request.form.get('artist_id')

    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    album = Album(
        None,
        request.form['title'],
        request.form['release_year'],
        request.form['artist_id'])
    repository.create(album)

    # repository.add(title, release_year, artist_id)
    return '', 200


@app.route('/albums', methods=['GET'])
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)

    albums = repository.all()
    albums_str = "\n".join(
        [f"Album('{album.title}', {album.release_year}, {album.artist_id})" for album in albums])

    return albums_str, 200


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
