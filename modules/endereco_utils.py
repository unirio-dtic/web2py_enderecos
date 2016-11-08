# coding=utf-8
from unicodedata import normalize


def remover_acentos(txt, codif='utf-8'):
    if isinstance(txt, unicode):
        txt = txt.encode('utf-8')
    return normalize('NFKD', txt.decode(codif)).encode('ASCII', 'ignore')


def lista_opcoes(api, cod_tabela):
    '''
     Consulta o endpoint tab_estruturada e retorna uma lista de
     descrições referentes a cod_tabela
    '''
    semana = 1209600
    where = {
        'cod_tabela': cod_tabela,
        'item_tabela_min': 0,  # descarta a descricao
        'ind_ativo': 'S',
        'lmin': 1,
        'lmax': 999
    }
    resultados = api.get('tab_estruturada', where, ['descricao'], cache_time=semana)
    return [remover_acentos(resultado['descricao'].strip()) for resultado in resultados]