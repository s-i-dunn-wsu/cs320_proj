# Samuel Dunn
# CS 320, Fall 2019

from hashlib import md5
import os
import json
import cherrypy

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

    def get_user_data_dir(self, username):
        if not self.check_for_user_exist(username):
            return None

        u, _, _ = self._get_checksums(username, 'unused')

        return os.path.join(self._here, 'users', u)

    def cp_authenticate(self, realm, user, pswd):
        """
        This is a mere passthrough to self.authenticate, which doens't care
        for the 'realm' parameter.
        """
        return self.authenticate(user, pswd)

    def authenticate(self, user, pswd):
        """
        Verifies the users credentials (or at least it would)
        and then supplies an Authentication Token that can be
        used to access user associations.
        """
        if not self.check_for_user_exist(user):
            return False # easy out.

        # Again, we're not here to be serious, we just need a
        # demoable way to track and associate data to users.
        u, p, c = self._get_checksums(user, pswd)

        user_folder = os.path.join(self._here, 'users', u)
        if os.path.exists(user_folder):
            with open(os.path.join(user_folder, '.cred1')) as fd:
                if fd.read() != p:
                    return False
            with open(os.path.join(user_folder, '.cred2')) as fd:
                if fd.read() != c:
                    return False

            # if we made it here, then both cred1 and cred2 checked out
            return True

        return False # did not find matching credentials.

    def create_user(self, user, pswd):
        """
        Creates a user entry.
        """
        if self.check_for_user_exist(user):
            raise UsernameTaken()

        u, p, c = self._get_checksums(user, pswd)

        user_folder = os.path.join(self._here, 'users', u)
        # Ensure there isn't a conflict with the md5
        if os.path.exists(user_folder):
            raise cherrypy.HTTPError(500, "Stale records or MD5 checksum clash. :(")

        # would have raised an exception already if it existed.
        os.makedirs(user_folder)

        with open(os.path.join(user_folder, '.cred1'), 'w') as fd:
            fd.write(p)
        with open(os.path.join(user_folder, '.cred2'), 'w') as fd:
            fd.write(c)

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
        u, _, _ = self._get_checksums(user, pswd)
        if self.authenticate(user, pswd):
            import shutil
            shutil.rmtree(os.path.join(self._here, 'users', u))

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
