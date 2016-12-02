# -*- coding: utf-8 -*-

###########################################################################
#    Module Writen to odoo
#
#    Copyright (c) 2015 Medma - http://www.medma.net
#    Copyright (C) 2016 - Today Turkesh Patel. <http://www.turkeshpatel.odoo.com>
#
#    Coded by: Turkesh Patel (turkesh.patel@medma.in)
#    Coded by: Ankit Gauri (ankit.gauri@medma.in)
#    @author Turkesh Patel (turkesh4friends@gmail.com)
#
##############################################################################


{
    'name': 'Countdown',
    'version': '1.0',
    'category': 'Website',
    'summary': 'Website Countdown Widget',
    'description':"""Countdown Widget""",
    'author': 'Turkesh Patel, Medma Infomatix',
    'depends': ['website'],
    'website': 'http://turkeshpatel.odoo.com, http://www.medma.net',
    'data': ['views/countdown.xml', 'views/templates.xml'],
    'demo_xml': [],
    'images': [
        'static/description/icon.png',
    ],
    'css': [ 'static/src/css/*.css' ],
    'js': ['static/src/js/*.js' ],
    'installable': True,
    'active': True,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
