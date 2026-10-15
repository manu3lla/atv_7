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


#respostas
#a)existem 3×3×2×3 = 54 combinações completas. O mínimo de um conjunto pairwise é 9 casos. Cada caso cobre só uma combinação de valores de cada par de parâmetros, e o par transportadora×embalagem (3×3) já exige 9 linhas
#b)o allpairspy gerou 10 casos, um acima do mínimo, porque usa heurística
#c) e d) os testes acima conferem os 45 pares e mostram que 3 casos deixam muitos pares descobertos