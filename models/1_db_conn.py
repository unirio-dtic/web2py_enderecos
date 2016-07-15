# coding:utf-8

from gluon import current
from unirio.api import UNIRIOAPIRequest

api = UNIRIOAPIRequest(myconf.take('api.key'), myconf.take('api.server'), debug=False, cache=current.cache.ram)
