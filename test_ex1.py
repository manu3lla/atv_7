from itertools import product
from allpairspy import AllPairs
from modelo import PARAMS, pares_de
def test_total_de_combinacoes():
    assert len(list(product(*PARAMS))) == 3 * 3 * 2 * 3 == 54
def test_pairwise_tem_quantidade_razoavel():
    casos = list(AllPairs(PARAMS))
    print("casos pairwise:", len(casos))
    assert 9 <= len(casos) < 54  # 9 = 3x3, o minimo teorico
def test_pairwise_cobre_todos_os_pares():
    casos = list(AllPairs(PARAMS))
    universo = pares_de(product(*PARAMS))
    assert len(universo) == 45
    assert pares_de(casos) == universo
def test_verificador_aponta_pares_descobertos():
    casos = list(AllPairs(PARAMS))
    universo = pares_de(product(*PARAMS))
    descobertos = universo - pares_de(casos[:3])
    assert len(descobertos) > 0
