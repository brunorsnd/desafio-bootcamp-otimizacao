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
                if a == indice and tipo == 'nao, se' and b in selecionados:  #
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
