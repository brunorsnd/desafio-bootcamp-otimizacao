from unittest import main, TestCase
from algoritmo_guloso import algoritmo_guloso


class TesteGuloso(TestCase):
    def teste_se_funciona_sem_investimentos(self):
        capital = 0
        custos = []
        retornos = []
        resultado = algoritmo_guloso(capital, custos, retornos)
        esperado = []

        self.assertEqual(resultado, esperado)

    def teste_se_escolhe_o_unico_investimento(self):
        capital = 100
        custos = [80]
        retornos = [120]
        resultado = algoritmo_guloso(capital, custos, retornos)
        esperado = [0]

        self.assertEqual(resultado, esperado)

    def teste_se_nao_escolhe_investimento_com_custo_maior_que_o_capital(self):
        capital = 60
        custos = [150, 50, 50, 50]
        retornos = [200, 60, 60, 60]
        resultado = algoritmo_guloso(capital, custos, retornos)

        self.assertNotIn(0, resultado)

    def teste_se_escolhe_o_item_de_melhor_razao_custo_retorno(self):
        capital = 60
        custos = [50, 50, 50, 50]
        retornos = [60, 60, 140, 60]
        resultado = algoritmo_guloso(capital, custos, retornos)

        self.assertIn(2, resultado)

    def teste_se_funciona_sem_restricoes(self):
        capital = 60
        custos = [50]
        retornos = [60]
        resultado = algoritmo_guloso(capital, custos, retornos)
        esperado = [0]
        restricoes = []

        self.assertEqual(resultado, esperado)

    # (3, 'se', 2) -> binary 3 >= 2
    def teste_se_a_restricao_do_tipo_SE_funciona(self):
        capital = 100
        custos = [50, 50, 50, 50]
        retornos = [60, 50, 40, 30]
        restricoes = [(2, 'se', 0), (3, 'se', 0)]
        resultado = algoritmo_guloso(capital, custos, retornos, restricoes)
        esperado = [1, 2]

        self.assertEqual(resultado, esperado)

    # (3, 'nao, se', 2) -> binary 3 + 2 <= 1
    def teste_se_a_restricao_do_tipo_NAO_SE_funciona(self):
        capital = 100
        custos = [50, 50, 50, 50]
        retornos = [60, 50, 40, 30]
        restricoes = [(1, 'nao, se', 0), (0, 'nao, se', 2)]
        resultado = algoritmo_guloso(capital, custos, retornos, restricoes)
        esperado = [0, 3]

        self.assertEqual(resultado, esperado)


if __name__ == '__testes_algoritmo_guloso__':
    main()
