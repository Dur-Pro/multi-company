# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class FetchMailServer(models.Model):
    _order = 'sequence'
    _inherit = "fetchmail.server"

    company_id = fields.Many2one("res.company", "Company")
    sequence = fields.Integer(default=10,
        help="Gives the sequence of this line when displaying the warehouses.")
