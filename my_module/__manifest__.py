{
    'name': 'My Module',
    'version': '1.0',
    'summary': 'Short module summary',
    'description': 'Detailed module description',
    'category': 'Uncategorized',
    'author': 'Your Name',
    'depends': ['base'],  # Add dependencies if needed
    'data': [
        'security/ir.model.access.csv',
        'views/my_model_views.xml',
    ],
    'installable': True,
    'application': True,
}
