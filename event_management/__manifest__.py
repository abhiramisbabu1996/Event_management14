# -*- coding: utf-8 -*-

{
    'name': 'Event Management',
    'version': '16.0.1.0.0',
    'summary': """Core Module for Managing Different Types Of Events.""",
    'description': """Core Module for Managing Different Types Of Events""",
    "category": "Industry",
    'author': 'Hiworth Solutions',
    'company': 'Hiworth Solutions',
    'maintainer': 'Hiworth Solutions',
    'website': "https://www.https://hiworthsolutions.com",
    'depends': ['product', 'account'],
    'data': ['security/event_security.xml',
             'security/ir.model.access.csv',
             'views/event_management_view.xml',
             'views/event_type_view.xml',
             'views/customer_enquiry_details.xml',
             'views/dashboard.xml',
             'data/event_management.xml',
             'reports/event_management_pdf_report.xml',
             'reports/pdf_report_template.xml',
             'wizards/event_management_wizard.xml',
             ],
    'assets': {
        'web.assets_backend': [
            "event_management/static/src/css/event_dashboard.css",
            "event_management/static/src/js/action_manager.js"
        ],
    },
    'images': ['static/description/banner.png'],
    'license': 'AGPL-3',
    'installable': True,
    'application': True,
}
