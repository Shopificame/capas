# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Guatemala - CoA',
    'version': '1.2',
    'category': 'Accounting/Localizations/Account Charts',
    'description': """
Localization Module for Guatemala
===========================================

Install Guatemala chart of accounts.
    """,
    'depends': [
        'base',
        'account',
    ],
    'data': [

        # Basic accounting data
        'data/l10n_gt_coa_chart_data.xml',
        'data/account.account.template.csv',
        'data/l10n_gt_coa_chart_post_data.xml',  
        'data/account_data.xml',
        'data/account_tax_data.xml',          
        'data/account_chart_template_data.xml',



        
    ],
    'demo': [

    ],
}