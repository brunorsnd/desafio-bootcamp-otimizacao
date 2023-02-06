from mip import Model, xsum, maximize, BINARY


def algoritmo_simplex_otimizacao_mip(capital, custos, retornos, restricoes_ligadas=True):
    modelo = Model('Investimentos')
    num_itens = range(len(custos))
    binarios = [modelo.add_var(var_type=BINARY) for _ in num_itens]
    modelo.objective = maximize(xsum(retornos[i] * binarios[i] for i in num_itens))
    modelo += xsum(custos[i] * binarios[i] for i in num_itens) <= capital
    if restricoes_ligadas:
        modelo.add_lazy_constr(binarios[0] + binarios[4] <= 1)
        modelo.add_lazy_constr(binarios[3] >= binarios[1])

    modelo.verbose = 0
    modelo.optimize()

    selecionados = [i for i in num_itens if binarios[i].x == 1]

    return selecionados
