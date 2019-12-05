# Samuel Dunn
# CS 320, Fall 2019

from .auth_token import AuthenticationToken
from hashlib import md5
import os
import json

class UsernameTaken(Exception): pass

class Authenticator(object):
    """
    Traditionally this class would serve as an actual authentication
    agent, verifying user credentials and passing/failing the user auth.

    As all of the context management, connection tracking, etc, are all
    outside the scope of this assignment - and would be in the way of
    other standardized services on campus - we've decided to have a very
    loose expectation for signing in.
    """
    # Authenticator is a borg object.
    _borg_state = None
    def __init__(self):
        if Authenticator._borg_state is None:
            Authenticator._borg_state = self.__dict__

            # Do other one-time init stuff here:
            self._here = os.path.dirname(os.path.abspath(__file__))
            self._user_manifest_path = os.path.join(self._here, 'users_mfst')

            if not os.path.exists(self._user_manifest_path):
                with open(self._user_manifest_path, 'w') as fd:
                    json.dump({}, fd) # use a dict for quicker searching (on an already incredibly slow process.)

        else:
            self.__dict__ = Authenticator._borg_state

    def check_for_user_exist(self, username):
        """
        Checks if the given username exists in username manifest.
        Returns True if it does.
        """
        # TODO: thread-safe this part
        with open(self._user_manifest_path) as fd:
            user_list = json.load(fd)

        return username in user_list


    def authenticate(self, user, pswd) -> AuthenticationToken:
        """
        Verifies the users credentials (or at least it would)
        and then supplies an Authentication Token that can be
        used to access user associations.
        """
        if not self.check_for_user_exist(user):
            return None # easy out.

        # Again, we're not here to be serious, we just need a
        # demoable way to track and associate data to users.
        u, p, c = self._get_checksums(user, pswd)

        group_folder = os.path.join(self._here, 'users', c)

        user_folder = os.path.join(group_folder, u)
        user_cred = os.path.join(user_folder, '.cred')
        if os.path.exists(group_folder) and os.path.isdir(group_folder):
            if os.path.exists(user_folder) and os.path.isdir(user_folder):
                if os.path.exists(user_cred) and os.path.isfile(user_cred):
                    with open(user_cred, 'r') as fd:
                        stored_p_md5 = fd.read()

                    if stored_p_md5 == p:
                        return AuthenticationToken(u, user_folder)

        return None # did not find matching credentials.

    def create_user(self, user, pswd):
        """
        Creates a user entry.
        """
        if self.check_for_user_exist(user):
            raise UsernameTaken()

        u, p, c = self._get_checksums(user, pswd)

        # Ensure the user doesn't already exist
        group_folder = os.path.join(self._here, 'users', c)
        user_folder = os.path.join(group_folder, u)
        if os.path.exists(os.path.join(group_folder, u)):
            raise UsernameTaken()

        # would have raised an exception already if it existed.
        os.makedirs(user_folder)

        with open(os.path.join(user_folder, '.cred'), 'w') as fd:
            fd.write(p)

        # TODO: thread-safen this part.
        # Now update the manifest file
        with open(self._user_manifest_path, 'r') as fd:
            user_dict = json.load(fd)

        user_dict[user] = None # add to dict.
        with open(self._user_manifest_path, 'w') as fd:
            # write back to disk.
            json.dump(user_dict, fd)



    def delete_user(self, user, pswd):
        """
        .. warning::
            This method exists essentially entirely for test purposes.
            steer clear of its use outside of test cases.
        """
        token = self.authenticate(user, pswd)
        if token:
            import shutil
            shutil.rmtree(token.user_dir)

            # TODO: make thread (and multiprocess) safe
            with open(self._user_manifest_path) as fd:
                user_dict = json.load(fd)

            del user_dict[user]
            with open(self._user_manifest_path, 'w') as fd:
                json.dump(user_dict, fd)

    def _get_checksums(self, user: str, pswd: str):
        """
        returns the 3 checksums used actively through out 'authentication'
        The checksums are returned as hex strings.
        """
        user = user.encode('utf-8')
        pswd = pswd.encode('utf-8')

        u_md5 = md5()
        u_md5.update(user)

        p_md5 = md5()
        p_md5.update(pswd)

        c_md5 = md5()
        c_md5.update(user + pswd)

        return u_md5.hexdigest(), p_md5.hexdigest(), c_md5.hexdigest()
