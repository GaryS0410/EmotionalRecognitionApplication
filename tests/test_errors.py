def test_404(client):
    response = client.get('/page_not_found')

    assert response.status_code == 404
    assert b"404 Error Encountered"

# def test_401(client):
#     response = client.get('/therapist_dash')

#     assert response.status_code == 401
#     assert b"401 Error Encountered"

# def test_500(client):
#     response = client.post('/questionnaires_page')

#     assert response.status_code == 500