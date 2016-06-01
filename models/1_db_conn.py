#coding:utf-8
from gluon import current
from unirio.api import UNIRIOAPIRequest
from unirio.api import APIServer

# db = DAL('postgres://postgres:devdtic2@teste.sistemas.unirio.br/pesquisa', pool_size=10, driver_args={'connect_timeout': 5})

api = UNIRIOAPIRequest(myconf.take('api.key'), APIServer.LOCAL, debug=False, cache=current.cache.ram)


