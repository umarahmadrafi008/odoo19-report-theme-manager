from odoo import models, fields


class ResCompany(models.Model):
    _inherit = 'res.company'

    active_theme_id = fields.Many2one(
        'report.theme.profile',
        string='Active Report Theme',
        help='This theme will be applied to all PDF reports for this company'
    )