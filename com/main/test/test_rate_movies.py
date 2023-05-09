from com.main.constants.BaseSetup import BaseSetup
from com.main.constants.StatusCode import StatusCode

apiKey = "6548ec0b96aa5e49daca0ddffe8b24ed"


def test_verify_rate_movies():
    resp = BaseSetup().getRatedMovies(apiKey)
    movieId = resp.json()["results"][0]["id"]
    resp = BaseSetup().getNewGuestSessionId(apiKey)

    assert resp.status_code == StatusCode.SUCCESSFUL, "get new guest session has failed"
    guestSessionId = resp.json()['guest_session_id']
    payload = {
        "value": 8.5}
    res = BaseSetup().postRateMovie(movieId, payload, apiKey, guestSessionId)

    assert res.status_code == StatusCode.CREATED, "Post rate movies has failed"
    assert res.json()['status_message'] == 'Success.'


def test_verify_rate_movies_without_api_key():
    resp = BaseSetup().getRatedMovies(apiKey)
    movieId = resp.json()["results"][0]["id"]
    resp = BaseSetup().getNewGuestSessionId(apiKey)

    assert resp.status_code == StatusCode.SUCCESSFUL, "get new guest session has failed"
    guestSessionId = resp.json()['guest_session_id']
    payload = {
        "value": 8.5}
    res = BaseSetup().postRateMovie(movieId, payload, '', guestSessionId)

    assert res.status_code == StatusCode.NOT_AUTHORIZED, "Post rate moview has failed"
    assert res.json()['status_message'] == 'Invalid API key: You must be granted a valid key.'


def test_verify_rate_movies_withou_guest_session():
    resp = BaseSetup().getRatedMovies(apiKey)
    movieId = resp.json()["results"][0]["id"]
    payload = {
        "value": 8.5}
    res = BaseSetup().postRateMovie(movieId, payload, apiKey, 'test')

    assert res.status_code == StatusCode.NOT_AUTHORIZED, "Post rate moview has failed"
    assert res.json()['status_message'] == 'Authentication failed: You do not have permissions to access the service.'
