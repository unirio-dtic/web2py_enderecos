# coding=utf-8
from gluon.tools import Auth, Service, PluginManager

auth = Auth(db)
service = Service()
plugins = PluginManager()

## create all tables needed by auth if not custom tables
auth.define_tables(username=True, signature=False)
auth.settings.actions_disabled = [
    'register',
    'retrieve_username',
    'profile',
    'lost_password',
    'request_reset_password',
    'change_password'
]

db.auth_user.username.label = 'CPF'

from gluon.contrib.login_methods.ldap_auth import ldap_auth
auth.settings.login_methods=[ldap_auth(mode='uid', server=UNIRIOLDAP.LDAP_TESTE, base_dn='ou=people,dc=unirio,dc=br')]
# auth.settings.login_onaccept.append(login_helper.adiciona_info_pessoa_logada)

## configure email
mail = auth.settings.mailer
mail.settings.server = 'logging' if request.is_local else myconf.take('smtp.server')
mail.settings.sender = myconf.take('smtp.sender')
mail.settings.login = myconf.take('smtp.login')


current.mailer = EmailBasico(mail, response.render)

## configure auth policy
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True


def popula_sessao(form):
    usuario = api.get_single_result("v_projetos_pessoas", {"cpf": form.vars.username}, cache_time=12000)
    first_name = usuario["nome"].split()[0].title()
    auth.user.update(first_name=first_name)
    session.profile = usuario

auth.settings.login_onaccept = [popula_sessao]

