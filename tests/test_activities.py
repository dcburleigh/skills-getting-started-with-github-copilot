def test_root_redirects_to_static_index(client):
    response = client.get("/", follow_redirects=False)
    assert response.status_code in (307, 308)
    assert response.headers["location"] == "/static/index.html"


def test_get_activities_returns_seeded_data(client):
    response = client.get("/activities")
    assert response.status_code == 200

    data = response.json()
    assert "Chess Club" in data

    chess_club = data["Chess Club"]
    assert chess_club["description"]
    assert chess_club["schedule"]
    assert chess_club["max_participants"] == 12
    assert "michael@mergington.edu" in chess_club["participants"]
