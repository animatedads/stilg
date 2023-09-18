# __manifest__.py

{
    'name': 'Tender Management',
    'version': '1.0',
    'summary': 'Module to allow portal users to manage tenders',
    'description': 'This module enables portal users to create tenders and submit bids for tenders.',
    'category': 'Sales',
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'depends': ['base', 'portal'],
    'data': [
        'security/ir.model.access.csv',
        'views/tender_views.xml',
        'views/bid_views.xml',
        'views/templates.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
