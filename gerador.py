from itertools import product
from modelo import pares_de
def gerar_pairwise(params):
    candidatos = list(product(*params))
    pares_do_candidato = {c: pares_de([c]) for c in candidatos}
    faltam = pares_de(candidatos)
    escolhidos = []
    while faltam:
        melhor = max(candidatos, key=lambda c: len(pares_do_candidato[c] & faltam))
        escolhidos.append(melhor)
        faltam -= pares_do_candidato[melhor]
    return escolhidos