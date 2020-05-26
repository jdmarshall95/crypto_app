from odoo.tests.common import TransactionCase

class TestBlock(TransactionCase):
    def setUp(self, *args, **kwargs):
        result = super().setUp(*args, **kwargs)
        self.Block = self.env['crypto.block']
        self.block_ode = self.Block.create({
        'keypair_name': 'Test crypto block',
        'keypair_path': '/test/path'})
        return result
    def test_create(self):
        "Test Ketpairs are active by default"
        self.assertEqual(self.block_ode.active, True)
