# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class IrMailServer(models.Model):
    _order = 'sequence'
    _inherit = "ir.mail_server"

    company_id = fields.Many2one("res.company", "Company")
    sequence = fields.Integer(default=10,
        help="Gives the sequence of this line when displaying the warehouses.")

    def build_email(self, email_from, email_to, subject, body, email_cc=None, email_bcc=None, reply_to=False,
                    attachments=None, message_id=None, references=None, object_id=False, subtype='plain',
                    headers=None, body_alternative=None, subtype_alternative='plain'):

        current_company = self.env.company
        if not reply_to and current_company.email_reply_to:
            reply_to = current_company.email_reply_to

        return super(IrMailServerCustom, self).build_email(email_from, email_to, subject, body, email_cc, email_bcc,
                                                           reply_to, attachments, message_id, references, object_id,
                                                           subtype, headers, body_alternative, subtype_alternative)
