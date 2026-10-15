from itertools import combinations, product
PARAMS = [
    ["Correios", "Jadlog", "Loggi"],
    ["caixa", "envelope", "tubo"],
    ["com seguro", "sem seguro"],
    ["normal", "expressa", "agendada"],
]
def pares_de(casos):
    pares = set()
    for caso in casos:
        for (i, vi), (j, vj) in combinations(enumerate(caso), 2):
            pares.add(((i, vi), (j, vj)))
    return pares