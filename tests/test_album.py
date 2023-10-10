from lib.album import Album

'''
constructs with an id, title, release date and artist id
'''


def test_constructs():
    album = Album(1, "Test Title", 1000, 2)
    assert album.id == 1
    assert album.title == "Test Title"
    assert album.release_year == 1000
    assert album.artist_id == 2


def test_compares():
    album1 = Album(1, "Test Title", 1000, 2)
    album2 = Album(1, "Test Title", 1000, 2)
    assert album1 == album2


def test_stringifying():
    album = Album(1, "Test Title", 1000, 2)
    assert str(album) == "Album(1, Test Title, 1000, 2)"
