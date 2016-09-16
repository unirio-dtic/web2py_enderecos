# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.logo = DIV(A(IMG(_src=URL("static", "images/unirio/dtic-emblema-branco.png"), _class="small_logo_dtic"),
                      _href="http://www.unirio.br/dtic"),
                    A("DTIC/UNIRIO", _class="brand", _href="http://www.unirio.br/dtic"))
response.title = 'Boilerplate - UNIRIO'
response.subtitle = 'Boilerplate'

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'DTIC - Sistemas <sistemas.tic@unirio.br>'
response.meta.description = 'Sistema modelo'
response.meta.keywords = 'web2py, python, framework'
response.meta.generator = 'Web2py Web Framework'

## your http://google.com/analytics id
response.google_analytics_id = None

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################

response.menu = [
    (T('Home'), False, URL('default', 'index'), [])
]

DEVELOPMENT_MENU = True
