# -*- coding: utf-8 -*-
{
    "name": "Project Wise Tasks Calendar View Color ",
    "version": "14.0.0.0.1",
    "category": "Projects",
    "depends": ['base', 'project'],
    "author": "Mediod Consulting",
    'maintainer': 'Zahid Mehmood',
    "website": "https://mediodconsulting.com/",
    'description': """By Default, in <b>My task</b> Calendar view, tasks are colored by asignees.
			This module help you to change it from asignees to project.
            Task related to same project will have same color""",
    'summary': 'Project Wise Tasks Color on Calendar View ',
    "data": [
        'views/project_view.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    "images":['static/description/Banner.png'],
}
