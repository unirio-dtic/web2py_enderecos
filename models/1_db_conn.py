#coding:utf-8

#db = DAL('postgres://postgres:devdtic2@teste.sistemas.unirio.br/pesquisa', pool_size=10, driver_args={'connect_timeout': 5})
#
# db = DAL(myconf.take('db.uri'), pool_size=myconf.take('db.pool_size', cast=int), check_reserved=['all'])
# api = UNIRIOAPIRequest(kAPIKey,APIServer.LOCAL,cache=current.cache.ram)
#
# # ===== configure email =====
# # auth = Auth(db)
# # mail = auth.settings.mailer
# # mail.settings.server = 'smtp.gmail.com:587'
# # mail.settings.sender = 'naoresponder.projetos@unirio.br'
# # mail.settings.login = 'naoresponder.projetos@unirio.br:8mx-SvY-fQh-SV9'
# #
# # current.mail = mail
# # current.auth = auth
# current.kAPIKey = kAPIKey
# # current.db = db
# current.api = api