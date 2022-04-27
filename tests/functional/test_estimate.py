def test_estimate_route(app, client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/estimate' route is requested (POST)
    THEN check that the response is valid
    """
    with app.test_client() as test_client:
    estimate = {"radius":"180", "height":"360"}
    res = test_client.post('/estimate', data=estimate)
    assert res.status_code == 200
    assert b"The estimate for painting is $143100" in res.data