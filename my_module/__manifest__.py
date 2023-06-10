{
    'name': 'My Test Module',
    'version': '16.0',
    'summary': 'Short module summary',
    'description': 'Detailed Test module description',
    'category': 'Uncategorized',
    'author': 'Thomas Dyer',
    'depends': ['base'],  # Add dependencies if needed
    'data': [
        'security/ir.model.access.csv',
        'views/my_model_views.xml',
    ],
    'installable': True,
    'application': True,
}
