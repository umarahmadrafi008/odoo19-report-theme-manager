{
    'name': 'Report Theme Manager',
    'version': '19.0.1.0.0',
    'category': 'Reporting',
    'summary': 'Manage multi-theme profiles for QWeb PDF reports with RTL support',
    'description': """
        Report Theme Manager allows you to create and manage multiple branding
        theme profiles for your PDF reports (Invoice, Sale Order, Purchase Order).
        Features include per-company themes, RTL/Arabic support, watermarks,
        custom fonts, and header/footer control — all from a single config screen.
    """,
    'author': 'Umar Ahmad Rafi',
    'website': 'https://github.com/umarahmadrafi008/odoo19-report-theme-manager',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'account',
        'sale',
        'purchase',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/default_theme_data.xml',
        'views/report_theme_profile_views.xml',
        'views/res_config_settings_views.xml',
        # 'report/report_base_template.xml',
        'report/report_invoice_inherit.xml',
        'report/report_sale_order_inherit.xml',
        'report/report_purchase_order_inherit.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}