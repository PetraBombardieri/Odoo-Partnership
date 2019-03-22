# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'CRM',
    'version': '1.0',
    'category': 'Sales',
    'sequence': 5,
    'summary': 'Track leads and close opportunities',
    'description': "",
    'website': 'https://www.odoo.com/page/crm',
    'depends': [
        'calendar',
        'contacts',
    ],
    'data': [
        'data/res.country.state.csv',
    ],
}