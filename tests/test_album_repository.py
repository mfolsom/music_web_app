from lib.album_repository import AlbumRepository
from lib.album import Album

'''
When I call #all
I get all the albums in the albums table
'''


def test_all(db_connection):
    db_connection.seed('seeds/music_library.sql')
    repository = AlbumRepository(db_connection)
    assert repository.all() == [
        Album(1, 'Doolittle', 1989, 1),
        Album(2, 'Surfer Rosa', 1988, 1),]
    db_connection.seed('seeds/music_empty.sql')

def test_add_a_new_album(db_connection):
    db_connection.seed('seeds/music_library.sql')
    repository = AlbumRepository(db_connection)
    album = Album(None, "Test Title", 1000, 2)
    repository.create(album)
    assert repository.all() == [
        Album(1, 'Doolittle', 1989, 1),
        Album(2, 'Surfer Rosa', 1988, 1),
        Album(3, 'Test Title', 1000, 2)]
    db_connection.seed('seeds/music_empty.sql')
