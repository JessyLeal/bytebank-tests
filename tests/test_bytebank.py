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
    # @mark.skip
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

    @mark.wage
    def test_when_wage_receive_10000_should_return_10000(self):
        input = 10000
        expected = 10000

        staff_test = Funcionario('Test_name', '11/11/2000', input)
        output = staff_test.salario

        assert output == expected
    
    @mark.wage
    def test_when_wage_receive_2000_should_return_2000(self):
        input = 2000
        expected = 2000

        staff_test = Funcionario('Test_name', '11/11/2000', input)
        output = staff_test.salario
        assert output == expected

    @mark.name
    def test_when_name_receive_juliana_should_return_juliana(self):
        input = 'Juliana'
        expected = 'Juliana'

        staff_test = Funcionario(input, '11/11/2000', 11111)
        output = staff_test.nome

        assert output == expected

    @mark.name
    def test_when_name_receive_flavinha_should_return_flavinha(self):
        input = 'Flavinha'
        expected = 'Flavinha'

        staff_test = Funcionario(input, '11/11/2000', 11111)
        output = staff_test.nome

        assert output == expected

    def test_return_str(self):
        input_name, input_birth, input_wage = 'test_name', '11/11/1989', 1000
        expected = "Funcionario(test_name, 11/11/1989, 1000)"

        staff_test = Funcionario(input_name, input_birth, input_wage)
        output = staff_test.__str__()

        assert output == expected
