from codigo.bytebank import Funcionario
import pytest
from pytest import mark

class TestClass:
    def test_quando_idade_recebe_13_03_2002_deve_retornar_22(self):
        entrada = '13/03/2002'  #Given-contexto
        esperado = 20

        Funcionario_teste = Funcionario('Teste', entrada, 1111)
        resultado = Funcionario_teste.idade() #when-ação
        assert resultado == esperado #Then-desfecho
    
    def test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_Carvalho(self):
        entrada = 'Lucas Carvalho'
        esperado = 'Carvalho'

        lucas = Funcionario(entrada, '11/11/2000', 1111)
        resultado = lucas.sobrenome()

        assert resultado == esperado
    @mark.skip
    def test_quando_decrescimo_salario_recebe_10000_deve_retornar_9000(self):
        entrada_salario = 100000
        entrada_nome ='Paulo Bragança'
        esperado = 90000

        funcionario_teste = Funcionario (entrada_nome, '11/11/2000', entrada_salario)

        funcionario_teste.decrescimo_salario()
        resultado = funcionario_teste ._salario

        assert resultado == esperado

    @mark.bonus_wage
    def test_when_bonus_wage_receive_1000_should_return_100(self):
        input = 1000
        expected = 100

        staff_test = Funcionario('Julinho', '11/11/2000', input)
        output = staff_test.calcular_bonus()

        assert output == expected

    @mark.bonus_wage
    def test_when_bonus_wage_receive_1000000000_should_return_exception(self):
        with pytest.raises(Exception):
            input = 100000000

            staff_test = Funcionario('Julinho', '11/11/2000', input)
            output = staff_test.calcular_bonus()

            assert output
