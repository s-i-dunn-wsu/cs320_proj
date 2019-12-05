import unittest
import time
from pofis.auth.authenticator import UsernameTaken, AuthenticationToken, Authenticator

class TestAuthenticator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Ensure a 'test' user exists.
        try:
            Authenticator().create_user('test', 'super secure')
        except Exception:
            pass

    @classmethod
    def tearDownClass(cls):
        Authenticator().delete_user('test', 'super secure')

    def test_login(self):
        token = Authenticator().authenticate('test', 'super secure')
        self.assertTrue(token is not None)

    def test_collision(self):
        """
        Tests if creating a user with the same user name causes a collision regardless of
        password.
        """

        with self.assertRaises(UsernameTaken, msg='Raises an exception with matching pass'):
            Authenticator().create_user('test', 'super secure')

        with self.assertRaises(UsernameTaken, msg='Raises an exception with mismatching passwords'):
            Authenticator().create_user('test', 'different password')

    def test_token_timeout(self):
        """
        """
        token = Authenticator().authenticate('test', 'super secure')
        token._last_used = time.time() - 898

        time.sleep(2)

        self.assertFalse(token.is_still_valid)

    def test_user_removal(self):
        """
        """
        # Test removing with incorrect password.
        Authenticator().delete_user('test', 'incorrect pass')
        self.assertTrue(Authenticator().check_for_user_exist('test'))

        # Now actually remove the user.
        Authenticator().delete_user('test', 'super secure')
        self.assertFalse(Authenticator().check_for_user_exist('test'))

        # if all's gone well we need to re-instance the test user.
        Authenticator().create_user('test', 'super secure')

if __name__ == "__main__":
    unittest.main()