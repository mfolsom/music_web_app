from lib.album import Album


class AlbumRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM albums")
        albums = []
        for row in rows:
            album = Album(
                row["id"], row["title"], row["release_year"], row["artist_id"])
            albums.append(album)
        return albums

    def create(self, album):
        # SQL query to insert a new album into the database
        query = """
        INSERT INTO albums (title, release_year, artist_id)
        VALUES (%s, %s, %s);
        """
        self._connection.execute(
            query, (album.title, album.release_year, album.artist_id))

        return None
