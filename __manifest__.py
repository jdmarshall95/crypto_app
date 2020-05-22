{
    'name': 'Crypto App',
    'description': 'Sign files and validate signed files',
    'author': 'Kumiko Hiraetari',
    'depends': ['base'],
    'application': 'true',
    'data': [
        'security/crypto_security.xml',
        'security/ir.model.access.csv',
        'views/crypto_menu.xml',
        'views/keypair_view.xml',
    ],
}
