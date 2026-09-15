def test_unregister_success(client):
    email = "michael@mergington.edu"  # already seeded participant of Chess Club

    response = client.post("/activities/Chess Club/unregister", params={"email": email})
    assert response.status_code == 200
    assert email in response.json()["message"]

    activities_response = client.get("/activities").json()
    assert email not in activities_response["Chess Club"]["participants"]


def test_unregister_not_registered_returns_400(client):
    response = client.post("/activities/Chess Club/unregister", params={"email": "notregistered@mergington.edu"})
    assert response.status_code == 400
    assert response.json()["detail"] == "Student is not signed up for this activity"


def test_unregister_unknown_activity_returns_404(client):
    response = client.post("/activities/Not A Real Club/unregister", params={"email": "student@mergington.edu"})
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"
