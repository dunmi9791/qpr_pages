# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'SMERP Website Pages',
    'version': '1.0',
    'category': 'hidden',
    'sequence': 6,
    'summary': 'Website Pages',
    'description': """

=======================

SMERP Website Pages

""",
    'depends': ['artesia', 'website_animate'],
    'data': [
        'views/template.xml',
        'views/homepage.xml',
        #'views/why.xml',
        'views/pricing.xml',
        'views/faqs.xml',
        'views/about.xml',
        'views/footer.xml',
    ],
    'installable': True,
    'auto_install': False,
}
