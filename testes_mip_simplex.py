from unittest import main, TestCase
from mip_simplex import algoritmo_simplex_otimizacao_mip


class TesteMipSimplex(TestCase):
    def teste_se_funciona_sem_restricoes(self):
        capital = 60
        custos = [50]
        retornos = [60]
        resultado = algoritmo_simplex_otimizacao_mip(capital, custos, retornos, restricoes_ligadas=False)
        esperado = [0]

        self.assertEqual(resultado, esperado)

    def teste_se_funciona_sem_investimentos(self):
        capital = 0
        custos = []
        retornos = []
        resultado = algoritmo_simplex_otimizacao_mip(capital, custos, retornos, restricoes_ligadas=False)
        esperado = []

        self.assertEqual(resultado, esperado)

    def teste_se_escolhe_o_unico_investimento(self):
        capital = 100
        custos = [80]
        retornos = [120]
        resultado = algoritmo_simplex_otimizacao_mip(capital, custos, retornos, restricoes_ligadas=False)
        esperado = [0]

        self.assertEqual(resultado, esperado)

    def teste_se_nao_escolhe_investimento_com_custo_maior_que_o_capital(self):
        capital = 60
        custos = [150, 50, 50, 50]
        retornos = [200, 60, 60, 60]
        resultado = algoritmo_simplex_otimizacao_mip(capital, custos, retornos, restricoes_ligadas=False)

        self.assertNotIn(0, resultado)

    def teste_se_escolhe_o_item_de_melhor_razao_custo_retorno(self):
        capital = 60
        custos = [50, 50, 50, 50]
        retornos = [60, 60, 140, 60]
        resultado = algoritmo_simplex_otimizacao_mip(capital, custos, retornos, restricoes_ligadas=False)

        self.assertIn(2, resultado)


if __name__ == '__testes_mip_simplex__':
    main()
