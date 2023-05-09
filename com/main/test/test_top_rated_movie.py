from com.main.constants.StatusCode import StatusCode
from com.main.constants.BaseSetup import BaseSetup

apiKey = "6548ec0b96aa5e49daca0ddffe8b24ed"


def test_top_rated_movie_with_invalid_api_key():
    resp = BaseSetup().getRatedMovies('testvalie')

    assert resp.status_code == StatusCode.NOT_AUTHORIZED,print(
        "Got wrong status code, expected is: {}, actual is  {}".format(StatusCode.NOT_AUTHORIZED, resp.status_code))

    assert resp.json()['status_message'] == "Invalid API key: You must be granted a valid key."


def test_top_rated_movie_with_valid_api_key():
    resp = BaseSetup().getRatedMovies(apiKey)

    assert resp.status_code == StatusCode.SUCCESSFUL,print(
        "Got wrong status code, expected is: {}, actual is  {}".format("200", resp.status_code))

    response_data = resp.json()

    assert response_data['page'] == 1, "Page should be 1 only"
