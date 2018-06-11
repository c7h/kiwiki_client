import requests
import logging
import datetime

_LOGGER = logging.getLogger(__name__)

BASE_URL = 'https://api.kiwi.ki'
API_AUTH_URL = BASE_URL + '/pre/session/'
API_LIST_DOOR_URL = BASE_URL + '/pre/sensors/'
API_OPEN_DOOR_URL = BASE_URL + '/pre/sensors/{}/act/open'

DEFAULT_TIMEOUT = 4


class KiwiClient:
    """Client for KIWI service."""

    def __init__(self, username, password, timeout=DEFAULT_TIMEOUT):
        """Initiale the client.

        :param username: valid KIWI username. Hint: your signup email address.
        :param password: your KIWI account password.
        """
        self.__username = username
        self.__password = password
        self.__session_key = None
        self.__session_expires = None
        self.__timeout = timeout

        # get a new session token on client startup
        self._renew_sessionkey()

    def _with_valid_session(self):
        """Check if the session is valid; renew if necessary."""
        now = datetime.datetime.now(tz=datetime.timezone.utc)
        if not self.__session_expires or (now >= self.__session_expires):
            _LOGGER.debug("no valid session found - renewing session key")
            self._renew_sessionkey()

    def _renew_sessionkey(self):
        """Update the clients session key."""
        import dateutil.parser
        _LOGGER.info(
            "authentication for user %s started.",
            self.__username)

        auth_response = requests.post(
            API_AUTH_URL,
            json={
                "username": self.__username,
                "password": self.__password
            },
            headers={"Accept": "application/json"},
            timeout=self.__timeout
        )

        if not auth_response.ok:
            _LOGGER.error(
                "could not authenticate at KIWI:\n%s",
                auth_response.json())

            raise KiwiException(
                "Authentication failed",
                {'status_code': auth_response.status_code},
            )

        self.__session_key = auth_response.json()['result']['session_key']
        self.__session_expires = dateutil.parser.parse(
            auth_response.json()['result']['session']['expires'])

    def get_locks(self):
        """Return a list of kiwi locks."""
        self._with_valid_session()
        sensor_list = requests.get(
            API_LIST_DOOR_URL,
            params={"session_key": self.__session_key},
            headers={"Accept": "application/json"},
            timeout=self.__timeout
        )
        if not sensor_list.ok:
            _LOGGER.error("could not get your KIWI doors.")
            return []

        doors = sensor_list.json()['result']['sensors']
        return doors

    def open_door(self, door_id):
        """Open the kiwi door lock."""
        self._with_valid_session()
        open_response = requests.post(
            API_OPEN_DOOR_URL.format(door_id),
            headers={"Accept": "application/json"},
            params={"session_key": self.__session_key},
            timeout=self.__timeout
        )
        if not open_response.ok:
            raise KiwiException(
                "Could not open door",
                {'status_code': open_response.status_code}
            )


class KiwiException(Exception):
    pass
