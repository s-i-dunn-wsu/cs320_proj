# CS 320
# Fall 2019

import time
import uuid

class AuthenticationToken(object):
    """
    An auth token can be used to access user information
    and can be serialized to URL-capable format.
    """
    _instances = {}

    @classmethod
    def get_token_by_uuid(cls, uid):
        if uid in cls._instances:
            if cls._instances[uid].is_still_valid:
                cls._instances[uid].extend_lease()
                return cls._instances[uid]
            else:
                del cls._instances[uid] # no longer valid, evict it.

    def __init__(self, user_token, user_data_path):
        self._user_token = user_token
        self._uuid = uuid.uuid4().hex
        self._last_used = time.time()
        self._user_data_path = user_data_path

        AuthenticationToken._instances[self._uuid] = self

    @property
    def is_still_valid(self):
        """
        Indicates if this token can still be trusted (ish, its not secure to begin with)
        """
        if time.time() - self._last_used < 900:  # 900 is 15 minutes
            return True

        else:
            return False

    @property
    def user_dir(self):
        """
        Returns an absolute path to the users's data directory.
        """
        return self._user_data_path

    def extend_lease(self):
        """
        Extends the 'timeout' on this token. Calling this
        function indicates that this token is being actively used.
        """
        self._last_used = time.time()