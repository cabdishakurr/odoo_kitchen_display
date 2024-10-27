{
    'name': 'Kitchen Display',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Kitchen display for restaurant orders',
    'depends': ['sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/kitchen_order_views.xml',
    ],
    'installable': True,
    'application': True,
}
