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
        "Album('Waterloo', 1974, 2)\n" \
        "Album('Super Trouper', 1980, 2)\n" \
        "Album('Bossanova', 1990, 1)\n" \
        "Album('Lover', 2019, 3)\n" \
        "Album('Folklore', 2020, 3)\n" \
        "Album('I Put a Spell on You', 1965, 4)\n" \
        "Album('Baltimore', 1978, 4)\n" \
        "Album('Here Comes the Sun', 1971, 4)\n" \
        "Album('Fodder on My Wings', 1982, 4)\n" \
        "Album('Ring Ring', 1973, 2)\n" \
        "Album('Two Hands', 2019, 5)\n" \
        "Album('Masterpiece', 2016, 5)"
