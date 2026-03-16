from odoo import models, fields


class ResCompany(models.Model):
    _inherit = 'res.company'

    active_theme_id = fields.Many2one(
        'report.theme.profile',
        string='Active Report Theme',
        help='This theme will be applied to all PDF reports for this company'
    )


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    active_theme_id = fields.Many2one(
        related='company_id.active_theme_id',
        string='Active Report Theme',
        readonly=False,
    )

    def action_open_report_themes(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Report Themes',
            'res_model': 'report.theme.profile',
            'view_mode': 'list,form',
            'target': 'current',
        }