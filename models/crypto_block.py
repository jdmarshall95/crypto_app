from odoo import fields, models

class Block(models.Model):
    _name = 'crypto.block'
    _description = 'Block'

    name = fields.Char('Name', required=True)
    keypair_path = fields.Char()
    active = fields.Boolean('Active?', default=True)
    date_generated = fields.Date()
