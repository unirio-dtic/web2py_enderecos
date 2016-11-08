from pydal import Field
from gluon import SQLFORM
from endereco_utils import remover_acentos


class ProcedureFormFactory:
    types = {
        "<type 'int'>": 'integer',
        "<type 'str'>": 'string',
        "<type 'unicode'>": 'string'
    }

    def __init__(self, initial_values, fields=None):
        """
        :type fields: list or tuple
        :type initial_values: dict
        """
        self.initial_values = initial_values
        self.__fields = fields or initial_values.keys()

    def get_type(self, t):
        """
        :rtype: str
        """
        return self.types.get(type(t), 'string')

    @property
    def fields(self):
        for key in self.__fields:
            value = self.initial_values.get(key)
            if isinstance(value, (str, unicode)):
                value = remover_acentos(value)

            yield Field(key, self.get_type(value), default=value)

    def form(self):
        return SQLFORM.factory(*self.fields)