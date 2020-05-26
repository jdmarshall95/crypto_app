from odoo import fields, models

class Block(models.Model):
    _name = 'crypto.block'
    _description = 'Block'

    keypair_name = fields.Char('Title', required=True)
    keypair_path = fields.Char()
    active = fields.Boolean('Active?', default=True)
    date_generated = fields.Date()
