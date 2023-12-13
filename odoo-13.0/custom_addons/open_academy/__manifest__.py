{
    'name': 'Open Academy',
    'version': '13.0',
    'summary': 'Manage academy',
    'sequence': 1,
    'depends': ['mail', 'base', 'board', 'web'],
    'category': 'Open Academy/Session',
    'license': 'AGPL-3',
    'author': 'Heinrich von Helmholtz',
    'data': [
        'views/course.xml',
        'views/session.xml',
        'views/inherit_view.xml',
        'views/dashboard.xml',
        'security/security.xml',    
        'security/ir.model.access.csv',
        'wizard/wizard.xml',
        'reports/report.xml',
        'reports/report_view.xml',
        ],
    'demo': [],
    'application': True,
    'installable': True,
    'auto_install': False
}