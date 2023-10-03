# __manifest__.py

{
    'name': 'Portal Product Creation',
    'version': '16.11',
    'summary': 'Allows portal users to create products on the Odoo online shop',
    'description': 'This module enables portal users to add new products with relevant details.',
    'category': 'Website',
    'author': 'Thomas Dyer',
    'website': 'https://www.allservices.cy',
    'depends': ['website_sale'],
    'data': [
        'views/product_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': True,
}
