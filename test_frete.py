from itertools import product
import pytest
from allpairspy import AllPairs
import frete as modulo_frete
PARAMS_FRETE = [
    ["leve", "medio", "pesado"],
    ["normal", "expressa"],
    [False, True],
    ["sul", "sudeste", "norte"],
]
def esperado(peso, urgencia, seguro, regiao):
    valor = {"leve": 10, "medio": 20, "pesado": 40}[peso]
    if regiao == "norte":
        valor += 8
    if urgencia == "expressa":
        valor *= 1.5
    if seguro:
        valor += 5
    return round(valor, 2)
PAIRWISE = [tuple(c) for c in AllPairs(PARAMS_FRETE)]
COMPLETO = list(product(*PARAMS_FRETE))
@pytest.mark.parametrize("peso,urgencia,seguro,regiao", PAIRWISE)
def test_frete_pairwise(peso, urgencia, seguro, regiao):
    assert modulo_frete.frete(peso, urgencia, seguro, regiao) == esperado(
        peso, urgencia, seguro, regiao
    )
@pytest.mark.parametrize("peso,urgencia,seguro,regiao", COMPLETO)
def test_frete_completo(peso, urgencia, seguro, regiao):
    assert modulo_frete.frete(peso, urgencia, seguro, regiao) == esperado(
        peso, urgencia, seguro, regiao
    )