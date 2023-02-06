from mip_simplex import algoritmo_simplex_otimizacao_mip
from algoritmo_guloso import algoritmo_guloso

my_capital = 1000000
descriptions = ['Ampliação da capacidade do armazém ZDP em 5%', 'Ampliação da capacidade do armazém MGL em 7%',
                'Compra de empilhadeira', 'Projeto de P&D I', 'Projeto de P&D II', 'Aquisição de novos equipamentos',
                'Capacitação de funcionários', 'Ampliação da estrutura de carga rodoviária']
costs = [470000, 400000, 170000, 270000, 340000, 230000, 50000, 440000]
returns = [410000, 330000, 140000, 250000, 320000, 320000, 90000, 190000]
restrictions = ((4, 'nao, se', 0), (3, 'se', 1))

resultado_guloso = algoritmo_guloso(my_capital, costs, returns, restrictions)
restulado_mip = algoritmo_simplex_otimizacao_mip(my_capital, costs, returns)


def mostrar_resultados(capital, descricoes, custos, retornos, selecionados):
    custo_total = 0
    retorno_total = 0
    print(f'Indices escolhidos: {selecionados}\n')

    for i in selecionados:
        print(f'Opção: {i + 1}, Custo: {custos[i]}, Retorno: {retornos[i]}, Razão: {retornos[i] / custos[i]:.3f}, '
              f'Descrição: {descricoes[i]}')
        custo_total += custos[i]
        retorno_total += retornos[i]

    print(f'\nCapital inicial: {capital}, Custo total: {custo_total} Retorno total: {retorno_total}\n')
    print('\n')


mostrar_resultados(my_capital, descriptions, costs, returns, resultado_guloso)
mostrar_resultados(my_capital, descriptions, costs, returns, restulado_mip)
