# coding:utf-8

from gluon import current
from unirio.api import UNIRIOAPIRequest

# db = DAL('postgres://postgres:devdtic2@teste.sistemas.unirio.br/pesquisa', pool_size=10, driver_args={'connect_timeout': 5})

api = UNIRIOAPIRequest(myconf.take('api.key'), myconf.take('api.server'), debug=False, cache=current.cache.ram)
