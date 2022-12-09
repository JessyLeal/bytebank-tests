from codigo.bytebank import Funcionario
import pytest
from pytest import mark

class TestClass:
    def test_when_age_receive_13_03_2002_should_return_22(self):
        input = '13/03/2002'  #Given-contexto
        expected = 20

        staff_test = Funcionario('Teste', input, 1111)
        output = staff_test.idade() #when-ação
        assert output == expected #Then-desfecho
    
    def test_when_lastname_receive_Lucas_Carvalho_should_return_Carvalho(self):
        input = 'Lucas Carvalho'
        expected = 'Carvalho'

        lucas = Funcionario(input, '11/11/2000', 1111)
        output = lucas.sobrenome()

        assert output == expected
    # @mark.skip
    def test_when_wage_decrease_receive_10000_should_return_9000(self):
        input_salario = 100000
        input_nome ='Paulo Bragança'
        expected = 90000

        staff_test = Funcionario (input_nome, '11/11/2000', input_salario)

        staff_test.decrescimo_salario()
        output = staff_test._salario

        assert output == expected

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
