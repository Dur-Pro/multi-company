from odoo import models, fields


class ResCompany(models.Model):
    _inherit = 'res.company'

    email_reply_to = fields.Char(string='Reply-To Email')
