from odoo.tests.common import TransactionCase

class TestBlock(TransactionCase):
    def setUp(self, *args, **kwargs):
        result = super().setUp(*args, **kwargs)
        user_admin = self.env.ref('base.user_admin')
        self.env= self.env(user=user_admin)
        self.Block = self.env['crypto.block']
        self.block_ode = self.Block.create({
        'keypair_name': 'Test crypto block',
        'keypair_path': '/test/path'})
        return result
    def test_create(self):
        "Test Ketpairs are active by default"
        self.assertEqual(self.block_ode.active, True)
    def test_check_keypair_name(self):
        "Check valid Keypair Name"
        self.assertTrue(self.block_ode._check_keypair_name)
