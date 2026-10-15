from collections import deque
import pytest
from hypothesis import given
import hypothesis.strategies as st
from fila import FilaCircular
CAPACIDADE = 3
@given(st.lists(st.integers(-1, 9)))
def test_fila_igual_ao_oraculo_deque(operacoes):
    fila = FilaCircular(CAPACIDADE)
    oraculo = deque()
    for op in operacoes:
        if op >= 0: 
            if len(oraculo) == CAPACIDADE:
                with pytest.raises(OverflowError):
                    fila.enfileirar(op)
            else:
                fila.enfileirar(op)
                oraculo.append(op)
        else: 
            if not oraculo:
                with pytest.raises(IndexError):
                    fila.desenfileirar()
            else:
                assert fila.desenfileirar() == oraculo.popleft()
        assert fila.tamanho == len(oraculo)