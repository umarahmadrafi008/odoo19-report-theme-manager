from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ReportThemeProfile(models.Model):
    _name = 'report.theme.profile'
    _description = 'Report Theme Profile'
    _order = 'name asc'

    name = fields.Char(
        string='Theme Name',
        required=True,
        help='e.g. Corporate Blue, Gulf Arabic, Minimal Clean'
    )
    company_id = fields.Many2one(
        'res.company',
        string='Company',
        required=True,
        default=lambda self: self.env.company,
    )
    is_default = fields.Boolean(
        string='Set as Default',
        default=False,
        help='Only one theme can be default per company'
    )

    # --- Branding ---
    primary_color = fields.Char(
        string='Primary Color',
        default='#1a73e8',
        help='Used for headings and table headers'
    )
    secondary_color = fields.Char(
        string='Secondary Color',
        default='#f0f0f0',
        help='Used for alternating rows and backgrounds'
    )

    # --- Typography ---
    font_family = fields.Selection(
        selection=[
            ('Roboto', 'Roboto'),
            ('Lato', 'Lato'),
            ('Cairo', 'Cairo (Arabic/Latin)'),
            ('Tajawal', 'Tajawal (Arabic)'),
            ('Amiri', 'Amiri (Arabic Formal)'),
        ],
        string='Font Family',
        default='Roboto',
    )
    font_size_body = fields.Integer(
        string='Body Font Size (pt)',
        default=10,
    )
    font_size_heading = fields.Integer(
        string='Heading Font Size (pt)',
        default=14,
    )

    # --- Header / Footer ---
    show_header = fields.Boolean(string='Show Header', default=True)
    show_footer = fields.Boolean(string='Show Footer', default=True)
    header_text = fields.Html(
        string='Header Text',
        help='Supports Arabic/Urdu text'
    )
    footer_text = fields.Html(
        string='Footer Text',
        help='Supports Arabic/Urdu text'
    )

    # --- RTL Support ---
    is_rtl = fields.Boolean(
        string='Enable RTL Layout',
        default=False,
        help='Enable for Arabic or Urdu reports'
    )
    rtl_font = fields.Selection(
        selection=[
            ('Tajawal', 'Tajawal'),
            ('Cairo', 'Cairo'),
            ('Amiri', 'Amiri'),
        ],
        string='RTL Font',
        help='Font used when RTL is enabled'
    )

    # --- Watermark ---
    show_watermark = fields.Boolean(string='Show Watermark', default=False)
    watermark_text = fields.Char(
        string='Watermark Text',
        help='e.g. DRAFT, PAID, CONFIDENTIAL'
    )
    watermark_opacity = fields.Float(
        string='Watermark Opacity',
        default=0.15,
        help='Value between 0.05 and 0.5'
    )

    # --- Report Assignment ---
    apply_to_invoice = fields.Boolean(string='Apply to Invoices', default=True)
    apply_to_sale = fields.Boolean(string='Apply to Sale Orders', default=True)
    apply_to_purchase = fields.Boolean(string='Apply to Purchase Orders', default=True)

    # --- Constraints ---
    @api.constrains('is_default', 'company_id')
    def _check_single_default(self):
        for record in self:
            if record.is_default:
                duplicate = self.search([
                    ('is_default', '=', True),
                    ('company_id', '=', record.company_id.id),
                    ('id', '!=', record.id),
                ])
                if duplicate:
                    raise ValidationError(
                        'Only one default theme is allowed per company. '
                        'Please unset the current default first.'
                    )

    @api.constrains('watermark_opacity')
    def _check_watermark_opacity(self):
        for record in self:
            if not (0.05 <= record.watermark_opacity <= 0.5):
                raise ValidationError(
                    'Watermark opacity must be between 0.05 and 0.5'
                )

    @api.constrains('font_size_body', 'font_size_heading')
    def _check_font_sizes(self):
        for record in self:
            if record.font_size_body < 6 or record.font_size_body > 20:
                raise ValidationError('Body font size must be between 6 and 20.')
            if record.font_size_heading < 8 or record.font_size_heading > 30:
                raise ValidationError('Heading font size must be between 8 and 30.')