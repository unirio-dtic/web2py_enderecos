# coding=utf-8
from procedure_form import ProcedureFormFactory
from endereco_utils import lista_opcoes


@auth.requires_login()
def alterar():
    query = {"id_pessoa": session.profile["id_pessoa"]}
    endereco = api.get_single_result("v_pessoas_enderecos", query)

    endereco = api.get_single_result("enderecos", {
        "id_endereco": max(endereco['id_endereco_alu'],
                           endereco['id_endereco_fun'])
    })

    paises = lista_opcoes(api, PAISES_OPCAO)
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

    form = ProcedureFormFactory(required_fields, endereco).form()

    if form.process().accepted:
        try:
            data = form.vars
            data.update({
                'cpf': session.profile.cpf,
                # 'cod_operador': session.profile.id_usuario
                'cod_operador': 666
            })
            result = api.call_procedure('CriarEndereco', [form.vars])
            session.form_result = result.content
        except Exception as e:
            response.flash = "Alguma de errado aconteçou durante a " \
                             "atualização de endereço. Contate o suporte " \
                             "ao usuário"
    elif form.errors:
        response.flash = "Ta fazendo merda. Tenta de novo"

    return dict(form=form)
