from itertools import product
from allpairspy import AllPairs
from gerador import gerar_pairwise
from modelo import PARAMS, pares_de
CHAVES = [[0, 1]] * 10
def test_gerador_cobre_modelo_do_exercicio_1():
    casos = gerar_pairwise(PARAMS)
    assert pares_de(casos) == pares_de(product(*PARAMS))
def test_gerador_cobre_dez_chaves():
    casos = gerar_pairwise(CHAVES)
    assert pares_de(casos) == pares_de(product(*CHAVES))
def test_comparacao_de_tamanhos():
    for nome, params, minimo in [("ex1", PARAMS, 9), ("chaves", CHAVES, 6)]:
        meu = len(gerar_pairwise(params))
        lib = len(list(AllPairs(params)))
        print(f"{nome}: guloso={meu} allpairspy={lib} minimo={minimo}")
        assert meu >= minimo and lib >= minimo