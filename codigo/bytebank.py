from datetime import date

class Funcionario:
    def __init__(self, nome, data_nascimento, salario):
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._salario = salario

    @property
    def nome(self):
        return self._nome
    
    def sobrenome(self):
        nome_quebrado = self._nome.split(' ')
        sobrenome = nome_quebrado[-1]

        return sobrenome
    
    def eh_socio(self):
        sobrenomes = ['Bragança', 'Windsor', 'Bourbon', 'Yamato', 'Al Saud', 'Khan', 'Tudor', 'Ptolomeu']

        return ((self._salario >= 100000) and (self.sobrenome() in sobrenomes))

    @property
    def salario(self):
        return self._salario

    def decrescimo_salario(self):
            if self.eh_socio():
                self._salario = (self._salario*0.9)

    def idade(self):
        data_nascimento = self._data_nascimento.split('/')
        ano_atual = date.today().year
        ano_nascimento = int(data_nascimento[-1])
        mes_nascimento = int(data_nascimento[-2])
        dia_nascimento = int(data_nascimento[-3])
        return ano_atual - int(ano_nascimento)

    def calcular_bonus(self):
        valor = self._salario * 0.1
        if valor > 1000:
            raise Exception('O salário é muito alto para receber um bônus.')
        return valor

    def __str__(self):
        return f'Funcionario({self._nome}, {self._data_nascimento}, {self._salario})'