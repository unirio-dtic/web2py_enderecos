import unittest

import requests

from unirio.api import UNIRIOAPIRequest, APIServer
from unirio.api.exceptions import *
import json


KEY = "CORRIJA PARA O VALOR CORRETO, MAS NAO ME ENVIE PARA O REPOSITORIO"


class ProcedureMockedTest(unittest.TestCase):
    @property
    def procedure(self):
        raise NotImplementedError("Should be implemented on subclass.")

    @property
    def mock_file(self):
        raise NotImplementedError("Should be implemented on subclass.")

    def setUp(self):
        self.api = UNIRIOAPIRequest(KEY, server=APIServer.LOCAL.value)
        with open(self.mock_file) as fp:
            self.mocks = json.load(fp)


class CriarEnderecoTest(ProcedureMockedTest):
    procedure = 'CriarEndereco'
    mock_file = './enderecos.json'

    def test_server_up(self):
        response = requests.get(self.api.server)
        assert response.status_code == 200

    def test_it_works_with_servidor_aluno(self):
        valid_mock = self.mocks['valid']['servidor_aluno']
        response = self.api.call_procedure(self.procedure, [valid_mock])

        assert len(response.content['id_endereco']) == 2

    def test_it_works_with_aluno(self):
        valid_mock = self.mocks['valid']['aluno']
        response = self.api.call_procedure(self.procedure, [valid_mock])
        assert len(response.content['id_endereco']) == 1

    def test_it_works_with_servidor(self):
        valid_mock = self.mocks['valid']['servidor']
        response = self.api.call_procedure(self.procedure, [valid_mock])

        assert len(response.content['id_endereco']) == 1

    def test_it_fails_with_empty_dataset(self):
        with self.assertRaises(MissingRequiredFieldsException):
            self.api.call_procedure(self.procedure, [{}])

    def test_it_fails_with_missing_parameters_in_dataset(self):
        with self.assertRaises(MissingRequiredFieldsException):
            self.api.call_procedure(self.procedure, [])
