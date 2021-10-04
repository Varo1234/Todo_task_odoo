# -*- coding: utf-8 -*-
{
    'name': "Garaje",

    'summary': """
        Aplication test""",

    'description': """
        It's only a test
    """,

    'author': "Alvaro Gutierrez",
    'website': "https://www.voblakye.com",

    'category': 'Uncategorized',
    'version': '0.1',

    # Aplication
    'application': True,

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
