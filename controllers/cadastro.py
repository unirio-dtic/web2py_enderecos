# coding=utf-8
from unirio.api.exceptions import NoContentException


@auth.requires_login()
def dados():
    try:
        result = api.get_single_result("v_pessoas_enderecos", {"id_pessoa": session.profile["id_pessoa"]})

        id_enderecos = []
        for field in ['id_endereco_alu', 'id_endereco_fun']:
            if result[field]:
                id_enderecos.append(result[field])

        enderecos = []
        session.enderecos = {}

        for id in id_enderecos:
            endereco = api.get_single_result("enderecos", {"id_endereco": id})
            enderecos.append(endereco)
            session.enderecos[id] = endereco

        return dict(enderecos=enderecos)
    except NoContentException:
        pass


@auth.requires_login()
def alterar():
    id_endereco = int(request.args[0])
    endereco = session.enderecos[id_endereco]

    paises = lista_opcoes(PAISES_OPCAO)
    paises.sort()

    required_fields = [
        'fone_residencial',
        'fone_celular',
        'fone_comercial',
        'descr_rua',
        'descr_numero',
        'descr_complemento',
        'descr_bairro',
        'descr_municipio',
        'descr_estado',
        'descr_pais',
        'descr_uf',
        'descr_cep',
        'descr_mail'
    ]

    types = {
        "<type 'int'>": 'integer',
        "<type 'str'>": 'string',
        "<type 'unicode'>": 'string'
    }

    def get_type(t):
        return types.get(t, 'string')

    fields = [Field(key, get_type(endereco[key]), default=remover_acentos(endereco[key]) if endereco[key] else None) for key in required_fields]
    form = SQLFORM.factory(*fields)

    if form.process().accepted:
        # todo: adicionar chave tipo_endereco
        # todo: atualizar IND_CORRESP do endereco corrent
        # todo: adicionar novo endereço
        # todo: mandar o cara pra outra tela
        pass
    elif form.errors:
        response.flash = "Ta fazendo merda. Tenta de novo"

    return dict(form=form)