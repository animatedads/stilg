{# __manifest__.py

{
    'name': 'Portal Product Creation',
    'version': '1.0',
    'summary': 'Allows portal users to create products on the Odoo online shop',
    'description': 'This module enables portal users to add new products with relevant details.',
    'category': 'Website',
    'author': 'Thomas Dyer',
    'website': 'https://www.example.com',
    'depends': ['website_sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_views.xml',
        'views/templates.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
