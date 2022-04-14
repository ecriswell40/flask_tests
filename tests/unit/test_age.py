import app

def test_calculate_current_age():
    """ 
    GIVEN a user enters the year they were born
    WHEN that year is passed to this function
    THEN the user's age is accurately calculated
    """
    assert app.calculate_current_age(2000) == 22  #will change as the years progress
