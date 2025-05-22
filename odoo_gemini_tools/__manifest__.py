
{
    'name': "Odoo Gemini Tools",
    'summary': "Odoo Gemini IA Integration",
    'author': "Yhasmani Valdes Migenes, OCTUPUS TECHNOLOGIES S.L",
    'category': 'Tools',
    'version': '17.0.1.0.1',
    'depends': ['base', 'web'],
    'license': 'LGPL-3',
    'external_dependencies': {
        'python': ['google-generativeai'],
    },
    'data': [
        'views/views.xml',
    ],
    'assets': {
        'web_editor.backend_assets_wysiwyg': [
            'odoo_gemini_tools/static/src/js/wysiwyg/**/*',
        ],
        'web_editor.assets_wysiwyg': [
            'odoo_gemini_tools/static/src/lib/showdown.min.js',
        ],
    },
}

