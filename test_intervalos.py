from hypothesis import given
import hypothesis.strategies as st
from intervalos import mesclar
pares = st.lists(st.tuples(st.integers(0, 50), st.integers(0, 50)))
def normalizar(lista):
    return [(min(a, b), max(a, b)) for a, b in lista]
@given(pares)
def test_idempotencia(lista):
    r = mesclar(normalizar(lista))
    assert mesclar(r) == r
@given(pares)
def test_resultado_em_ordem_e_sem_sobreposicao(lista):
    r = mesclar(normalizar(lista))
    for (ini1, fim1), (ini2, fim2) in zip(r, r[1:]):
        assert ini1 <= fim1
        assert fim1 < ini2
@given(pares)
def test_entrada_contida_no_resultado(lista):
    entrada = normalizar(lista)
    r = mesclar(entrada)
    for ini, fim in entrada:
        assert any(a <= ini and fim <= b for a, b in r)