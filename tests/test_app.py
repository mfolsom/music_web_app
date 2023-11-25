def test_post_albums(db_connection, web_client):
    db_connection.seed('seeds/music_library.sql')
    post_response = web_client.post('/albums', data={
        'title': 'Masterpiece',
        'release_year': '2016',
        'artist_id': '5'
    })
    assert post_response.status_code == 200
    assert post_response.data.decode('utf-8') == ""
    get_response = web_client.get("/albums")
    assert get_response.status_code == 200
    get_response = web_client.get("/albums")
    assert get_response.data.decode('utf-8') == "" \
        "Album('Doolittle', 1989, 1)\n" \
        "Album('Surfer Rosa', 1988, 1)\n" \
        "Album('Masterpiece', 2016, 5)"
    db_connection.seed('seeds/music_empty.sql')
