# -*- coding: utf-8 -*-
{
    'name': "infame2",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        fils and games INFAME2
    """,

    'author': "Mario Munoz Fuentes",
    'website': "https://github.com/MarioMunozFuentes",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    # PONEMOS QUE ES DE TIPO APLICACION
    'application': True,
    #DECIMOS QUE ES DE TIPO MARKETING
    'category': 'Marketing',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded --> LO DESCOMENTAMOS
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
