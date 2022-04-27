import pytest

def test_index_route(app, client):
    """ 
    GIVEN a Flask application configured for testing
    WHEN the '/' route is requested (GET)
    THEN check that the response is valid
    """
    with app.test_client() as test_client:
        res = test_client.get('/')
        assert res.status_code == 200
        assert b'Vertical Tank Maintenance' in res.data

def test_about_route(app, client):
    """ 
    GIVEN a Flask application configured for testing
    WHEN the '/about' route is requested (GET)
    THEN check that the response is valid
    """

    with app.test_client() as test_client:
        res = test_client.get('/about')
        assert res.status_code == 200
        assert b'About' in res.data

def test_estimate_route(app, client):
    """ 
    GIVEN a Flask application configured for testing
    WHEN the '/estimate' route is requested (GET)
    THEN check that the response is valid
    """
    with app.test_client() as test_client:
        Total = {"radius":"180", "height":"360"}
        res = test_client.post('/estimate', data=Total)
        assert res.status_code == 200
        assert b "The estimate for painting is $143100" in res.data


  

