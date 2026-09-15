def test_signup_success(client):
    response = client.post("/activities/Chess Club/signup", params={"email": "newstudent@mergington.edu"})
    assert response.status_code == 200
    assert "newstudent@mergington.edu" in response.json()["message"]

    activities_response = client.get("/activities").json()
    assert "newstudent@mergington.edu" in activities_response["Chess Club"]["participants"]


def test_signup_duplicate_returns_400(client):
    email = "michael@mergington.edu"  # already seeded participant
    response = client.post("/activities/Chess Club/signup", params={"email": email})
    assert response.status_code == 400
    assert "already signed up" in response.json()["detail"]


def test_signup_unknown_activity_returns_404(client):
    response = client.post("/activities/Not A Real Club/signup", params={"email": "student@mergington.edu"})
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_signup_activity_full_returns_400(client):
    # Soccer Team starts with 0 participants and a max of 22
    for i in range(22):
        response = client.post("/activities/Soccer Team/signup", params={"email": f"student{i}@mergington.edu"})
        assert response.status_code == 200

    response = client.post("/activities/Soccer Team/signup", params={"email": "onemore@mergington.edu"})
    assert response.status_code == 400
    assert response.json()["detail"] == "Activity is full"
