# -*- coding: utf-8 -*-
{
    'name': "custom_kuantik",

    'summary': """
        Personalizaciones de Kuantik""",

    'description': """
        Campo Profesion Res_partner
    """,

    'author': "Andrés Gaviria",
    'website': "http://www.intresco.co",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'custom',
    'version': '0.0',

    # any module necessary for this one to work correctly
    'depends': ['base','payment_report_co'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/res_partner.xml',
        'views/templates.xml',
        'views/paper_format_pos.xml',
        'report/sale_order_report.xml',
        'report/payment_receipt_pos_inherit.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
