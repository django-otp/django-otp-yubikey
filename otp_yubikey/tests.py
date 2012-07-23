from binascii import unhexlify

from django.test import TestCase

from otp_yubikey.models import YubikeyDevice
from yubiotp.otp import encode_otp, YubiKey


class YubikeyTest(TestCase):
    fixtures = ['tests/alice_and_bob']

    alice_public = 'cccccccb'
    alice_aes = unhexlify('fb362a0853be5e5306d5cc2483f279cb')
    alice_key = YubiKey(unhexlify('5dc30490956b'), 6, 0)

    bob_public = 'cccccccd'
    bob_key = YubiKey(unhexlify('326f70826d31'), 11, 0)
    bob_aes = unhexlify('11080a0e7a56d0a1546f327f20626308')

    def setUp(self):
        self.alice_device = YubikeyDevice.objects.get(user__username='alice')
        self.bob_device = YubikeyDevice.objects.get(user__username='bob')

    def test_verify_alice(self):
        _, token = self.alice_token()
        ok = self.alice_device.verify_token(token)

        self.assert_(ok)

    def test_counter_increment(self):
        otp, token = self.alice_token(5, 7)
        ok = self.alice_device.verify_token(token)

        self.assert_(ok)
        self.assertEqual(self.alice_device.session, 5)
        self.assertEqual(self.alice_device.counter, 7)

    def test_no_verify_mismatch(self):
        _, token = self.alice_token()
        ok = self.bob_device.verify_token(token)

        self.assert_(not ok)

    def test_replay(self):
        otp, token = self.alice_token()
        ok1 = self.alice_device.verify_token(token)
        ok2 = self.alice_device.verify_token(token)

        self.assert_(ok1)
        self.assert_(not ok2)
        self.assertEqual(self.alice_device.session, otp.session)
        self.assertEqual(self.alice_device.counter, otp.counter)

    def test_bad_public_id(self):
        self.alice_public = self.bob_public
        otp, token = self.alice_token()
        ok = self.alice_device.verify_token(token)

        self.assert_(not ok)

    def test_bad_private_id(self):
        alice_key = YubiKey(unhexlify('2627dc624cbd'), 6, 0)
        otp = alice_key.generate()
        token = encode_otp(otp, self.alice_aes, self.alice_public)
        ok = self.alice_device.verify_token(token)

        self.assert_(not ok)

    def test_session_replay(self):
        otp, token = self.alice_token(4, 0)
        ok = self.alice_device.verify_token(token)

        self.assert_(not ok)

    def test_counter_replay(self):
        otp, token = self.alice_token(5, 0)
        ok = self.alice_device.verify_token(token)

        self.assert_(not ok)

    def test_bad_decrypt(self):
        otp = self.alice_key.generate()
        token = encode_otp(otp, self.bob_aes, self.alice_public)
        ok = self.alice_device.verify_token(token)

        self.assert_(not ok)

    def test_bogus_token(self):
        ok = self.alice_device.verify_token('completelybogus')

        self.assert_(not ok)


    def alice_token(self, session=None, counter=None):
        otp = self.alice_key.generate()

        if session is not None:
            otp.session = session

        if counter is not None:
            otp.counter = counter

        return otp, encode_otp(otp, self.alice_aes, self.alice_public)
