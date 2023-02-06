my_capital = 1000000
descriptions = ['Ampliação da capacidade do armazém ZDP em 5%', 'Ampliação da capacidade do armazém MGL em 7%',
                'Compra de empilhadeira', 'Projeto de P&D I', 'Projeto de P&D II', 'Aquisição de novos equipamentos',
                'Capacitação de funcionários', 'Ampliação da estrutura de carga rodoviária']
costs = [470000, 400000, 170000, 270000, 340000, 230000, 50000, 440000]
returns = [410000, 330000, 140000, 250000, 320000, 320000, 90000, 190000]
restrictions = [(1, 'nao, se', 4), (3, 'se', 1)]  # 1 + 4 <= 1    3 >= 1

capital2 = 150
custos2 = [50, 50, 50]
retornos2 = [60, 50, 40]
restricoes2 = [(1, 'nao, se', 2)]


def algoritmo_guloso(capital, custos, retornos, restricoes=None):
    razoes = []

    for indice, custo in enumerate(custos):
        razao_atual = retornos[indice] / custos[indice]
        razoes.append((indice, razao_atual))  # Guarda o índice da razão para saber depois à qual opção ele pertence
    razoes.sort(key=lambda i: i[1], reverse=True)

    selecionados = []
    descartados = []
    for indice, razao in razoes:
        if restricoes is not None:
            for a, tipo, b in restricoes:
                if a == indice and tipo == 'nao, se' and b in selecionados:
                    descartados.append(a)
                if b == indice and tipo == 'nao, se' and a in selecionados:
                    if b not in descartados:
                        descartados.append(b)
                if a == indice and tipo == 'se' and a in descartados:
                    if b not in descartados:
                        descartados.append(b)
                if b == indice and tipo == 'se' and a not in descartados and a not in selecionados:
                    if capital - (custos[indice] + custos[a]) >= 0:
                        capital -= custos[a]
                        selecionados.append(a)
                    else:
                        descartados.append(b)

        if capital >= custos[indice] and indice not in descartados and indice not in selecionados:
            selecionados.append(indice)
            capital -= custos[indice]

    selecionados.sort()

    return selecionados
