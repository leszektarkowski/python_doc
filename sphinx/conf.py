# -*- coding: utf-8 -*-

import sys, os

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

# General information about the project.
project = u'Zaawansowane programowanie w języku Python'
copyright = u'2014, Leszek Tarkowski'

# The short X.Y version.
version = ''
# The full version, including alpha/beta/rc tags.
release = ''

language = 'en'
today = None
today_fmt = '%Y'
exclude_patterns = ['_build', '_old']
add_module_names = False
pygments_style = 'sphinx'
# -- Options for HTML output ---------------------------------------------------
html_theme = 'default'
#html_theme = 'bootstrap'
#html_theme = 'infotraining'
#html_theme = "sphinx_rtd_theme"

# html_theme_options = {
#     'navbar_title': "Infotraining",
#     'navbar_site_name': "Index",
#     'navbar_sidebarrel': False,
#     'navbar_pagenav': False,
#     'globaltoc_depth': 2,
#     'globaltoc_includehidden': "true",
#     #'navbar_class': "navbar navbar-inverse",
#     'navbar_fixed_top': "false",
#     # Options are "nav" (default), "footer" or anything else to exclude.
#     'source_link_position': "footer",
#     # Bootswatch (http://bootswatch.com/) theme.
#     #
#     # Options are nothing with "" (default) or the name of a valid theme
#     # such as "amelia" or "cosmo".
#     #'bootswatch_theme': "readable",
#     #'bootswatch_theme': "cerulean",
#     'bootswatch_theme': "lumen",
#     #'bootswatch_theme': "yeti",
#     'bootstrap_version': "3",
# }
html_theme_path = ["./theme"]

html_title = u'Zaawansowane programowanie w języku Python'
html_short_title = u'Zaawansowany Python'
#html_logo = None
#html_favicon = None
# html_static_path = ['_static']
#html_domain_indices = True
#html_use_index = True
#html_split_index = False
html_show_sourcelink = False
#html_show_sphinx = True
#html_show_copyright = True
#html_use_opensearch = ''
htmlhelp_basename = 'python_TDD'

# -- Options for LaTeX output --------------------------------------------------
latex_elements = {
    #The paper size ('letterpaper' or 'a4paper').
    'papersize': 'a4paper',
    'releasename': "",
    #The font size ('10pt', '11pt' or '12pt').
    'pointsize': '11pt',
    #'inputenc': '',
    'utf8extra': '',
    #'printindex': '\\printindex',
    'printindex': '',
    #Additional stuff for the LaTeX preamble.
    #\usepackage{libertine}

    'preamble': r"""
\usepackage{gentium}
\usepackage{inconsolata}
\usepackage[utf8]{inputenc}
\usepackage[table]{xcolor}
\usepackage{polski}
\definecolor{VerbatimColor}{rgb}{0.99,0.99,0.99}
\definecolor{VerbatimBorderColor}{rgb}{0.3,0.3,0.3}
\addtolength{\oddsidemargin}{1cm}
\addtolength{\evensidemargin}{1cm}
\addtolength{\textwidth}{-2cm}
\addtolength{\topmargin}{1cm}
\addtolength{\textheight}{-2cm}

\usepackage{newunicodechar}


\definecolor{foo}{rgb}{0.91,0.91,0.95}
\definecolor{bar}{rgb}{1,1,1}

\let\newtabular\tabular
\let\newendtabular\endtabular
\renewenvironment{tabular}{\rowcolors{2}{foo}{bar}\newtabular}{\newendtabular}
""",
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
    ('index', 'adv_python_2014.tex',
     u'Zaawansowane programowanie w języku Python'
     u'Leszek Tarkowski', 'manual', True),
]

latex_logo = "logo-large.png"
